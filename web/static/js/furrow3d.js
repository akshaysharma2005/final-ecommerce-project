/* NEXUS.AI — 3D Topographic Survey Map & Optical Loupe Engine
 * Directly inspired by Hallmark Furrow (Fieldbook) marching-squares survey map
 * Enhanced with 3D isometric terrain relief, fold-lit drafting creases, and live 1.9x magnifying loupe
 */
(() => {
  const hero = document.getElementById('furrow-hero');
  if (!hero) return;

  const canvas = document.getElementById('survey-canvas');
  const loupe = document.getElementById('survey-loupe');
  const mapLayer = document.getElementById('survey-map-layer');
  const routePath = document.getElementById('route-line');
  const pins = [...document.querySelectorAll('.survey-pin')];
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Furrow Ink & Material Tokens
  const PAPER = '#f6f2ea';
  const PAPER2 = '#fefdf9';
  const INK = (a = 1) => `rgba(30, 27, 24, ${a})`;
  const CONTOUR = (a = 1) => `rgba(165, 125, 90, ${a})`;
  const WATER = (a = 1) => `rgba(94, 134, 156, ${a})`;
  const HEDGE = (a = 1) => `rgba(60, 122, 82, ${a})`;
  const TANGERINE = (a = 1) => `rgba(245, 103, 56, ${a})`;

  // Seeded Perlin Noise & fBm
  const rng = (a) => () => {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  const perlin = (seed) => {
    const r = rng(seed);
    const perm = new Uint8Array(512);
    const base = [...Array(256).keys()];
    for (let i = 255; i > 0; i--) {
      const j = Math.floor(r() * (i + 1));
      [base[i], base[j]] = [base[j], base[i]];
    }
    for (let i = 0; i < 512; i++) perm[i] = base[i & 255];
    const g = (h, x, y) => {
      switch (h & 7) {
        case 0: return x + y; case 1: return -x + y; case 2: return x - y; case 3: return -x - y;
        case 4: return x; case 5: return -x; case 6: return y; default: return -y;
      }
    };
    const f = (t) => t * t * t * (t * (t * 6 - 15) + 10);
    return (x, y) => {
      const xi = Math.floor(x), yi = Math.floor(y);
      const X = xi & 255, Y = yi & 255;
      x -= xi; y -= yi;
      const u = f(x), v = f(y);
      const a = perm[X] + Y, b = perm[X + 1] + Y;
      const n00 = g(perm[a], x, y), n10 = g(perm[b], x - 1, y);
      const n01 = g(perm[a + 1], x, y - 1), n11 = g(perm[b + 1], x - 1, y - 1);
      return (n00 + u * (n10 - n00)) + v * ((n01 + u * (n11 - n01)) - (n00 + u * (n10 - n00)));
    };
  };
  const fbm = (n, x, y, oct = 4) => {
    let s = 0, a = 0.5, f = 1;
    for (let i = 0; i < oct; i++) { s += a * n(x * f, y * f); f *= 2.03; a *= 0.5; }
    return s;
  };

  // Sample Territory Geometry (Brazilian E-Commerce Macro-Regions mapped as a Surveyor Holding)
  const A = 1.25;
  const V = {
    a: [0.04, 0.12], b: [0.34, 0.05], c: [0.64, 0.08], d: [0.91, 0.16], k: [0.94, 0.42], e: [0.96, 0.58],
    p: [0.94, 0.74], f: [0.89, 0.91], g: [0.60, 0.95], h: [0.37, 0.92], i: [0.10, 0.87], s: [0.04, 0.66], j: [0.03, 0.39],
    m: [0.31, 0.34], l: [0.66, 0.38], q: [0.65, 0.57], r: [0.39, 0.58], t: [0.22, 0.62], u: [0.41, 0.77], w: [0.22, 0.79]
  };
  const FIELDS = [
    { name: 'Northeast Corridor', ring: 'abcdklmj', at: [0.60, 0.21], size: 12.5 },
    { name: 'Central-West', ring: 'lkeq', at: [0.80, 0.46], size: 12 },
    { name: 'Southeast Core', ring: 'mlqr', at: [0.50, 0.51], size: 13 },
    { name: 'São Paulo Hub', ring: 'jmrts', at: [0.16, 0.56], size: 12 },
    { name: 'Fulfillment Yard', ring: 'truw', at: [0.27, 0.73], size: 11 },
    { name: 'South Basin', ring: 'rqepfghu', at: [0.49, 0.86], size: 12.5 },
    { name: 'North Frontier', ring: 'stwuhi', at: [0.15, 0.82], size: 11.5 }
  ];
  const HOLDING = 'abcdkepfghisj';
  const WALLS = new Set(['a-b', 'b-c', 'c-d', 'd-k']);
  const STREAM = [[0.8, 1.35], [0.62, 1.1], [0.42, 1.01], [0.24, 0.985], [0.07, 1.03], [-0.15, 1.1], [-0.45, 1.06]];
  const LANE = [[0.31, 1.3], [0.35, 1.06], [0.37, 0.92], [0.41, 0.77]];
  const BUILDINGS = [[0.28, 0.66, 0.065, 0.032], [0.355, 0.645, 0.032, 0.056], [0.345, 0.725, 0.052, 0.024]];

  // Helpers
  const segDist = (px, py, ax, ay, bx, by) => {
    const dx = bx - ax, dy = by - ay;
    const t = Math.max(0, Math.min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)));
    return Math.hypot(px - ax - t * dx, py - ay - t * dy);
  };
  const chaikin = (pts, closed, iter = 2) => {
    let p = pts;
    for (let k = 0; k < iter; k++) {
      const o = [], L = p.length;
      if (!closed) o.push(p[0]);
      for (let i = 0; i < (closed ? L : L - 1); i++) {
        const a = p[i], b = p[(i + 1) % L];
        o.push([a[0] * 0.75 + b[0] * 0.25, a[1] * 0.75 + b[1] * 0.25], [a[0] * 0.25 + b[0] * 0.75, a[1] * 0.25 + b[1] * 0.75]);
      }
      if (!closed) o.push(p[L - 1]);
      p = o;
    }
    return p;
  };
  const plen = (pts) => {
    let s = 0;
    for (let i = 1; i < pts.length; i++) s += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]);
    return s;
  };
  const pathOf = (pts, closed = false) => {
    const p = new Path2D();
    p.moveTo(pts[0][0], pts[0][1]);
    for (let i = 1; i < pts.length; i++) p.lineTo(pts[i][0], pts[i][1]);
    if (closed) p.closePath();
    return p;
  };

  // Marching Squares Contour Tracer
  const EDGES = [[], [[3, 2]], [[2, 1]], [[3, 1]], [[0, 1]], null, [[0, 2]], [[3, 0]], [[3, 0]], [[0, 2]], null, [[0, 1]], [[3, 1]], [[2, 1]], [[3, 2]], []];
  function trace(field, nx, ny, cell, step) {
    const buckets = new Map();
    const pt = (i, j, e, v0, v1, v2, v3, t) => {
      switch (e) {
        case 0: return [(i + (t - v0) / (v1 - v0)) * cell, j * cell];
        case 1: return [(i + 1) * cell, (j + (t - v1) / (v2 - v1)) * cell];
        case 2: return [(i + (t - v3) / (v2 - v3)) * cell, (j + 1) * cell];
        default: return [i * cell, (j + (t - v0) / (v3 - v0)) * cell];
      }
    };
    const key = (i, j, e) => (e === 0 ? (j * nx + i) * 2 : e === 2 ? ((j + 1) * nx + i) * 2 : e === 1 ? (j * nx + i + 1) * 2 + 1 : (j * nx + i) * 2 + 1);
    for (let j = 0; j < ny - 1; j++) {
      for (let i = 0; i < nx - 1; i++) {
        const v0 = field[j * nx + i], v1 = field[j * nx + i + 1], v2 = field[(j + 1) * nx + i + 1], v3 = field[(j + 1) * nx + i];
        const lo = Math.min(v0, v1, v2, v3), hi = Math.max(v0, v1, v2, v3);
        for (let k = Math.ceil(lo / step); k * step < hi; k++) {
          const t = k * step;
          const code = (v0 > t ? 8 : 0) | (v1 > t ? 4 : 0) | (v2 > t ? 2 : 0) | (v3 > t ? 1 : 0);
          let segs = EDGES[code];
          if (segs === null) {
            const c = (v0 + v1 + v2 + v3) / 4 > t;
            segs = code === 5 ? (c ? [[3, 0], [2, 1]] : [[3, 2], [0, 1]]) : (c ? [[0, 1], [3, 2]] : [[3, 0], [2, 1]]);
          }
          if (!segs.length) continue;
          let b = buckets.get(k);
          if (!b) buckets.set(k, (b = { pts: new Map(), adj: new Map(), segs: [] }));
          for (const [ea, eb] of segs) {
            const ka = key(i, j, ea), kb = key(i, j, eb);
            if (!b.pts.has(ka)) b.pts.set(ka, pt(i, j, ea, v0, v1, v2, v3, t));
            if (!b.pts.has(kb)) b.pts.set(kb, pt(i, j, eb, v0, v1, v2, v3, t));
            const s = b.segs.length;
            b.segs.push([ka, kb]);
            (b.adj.get(ka) || b.adj.set(ka, []).get(ka)).push(s);
            (b.adj.get(kb) || b.adj.set(kb, []).get(kb)).push(s);
          }
        }
      }
    }
    const out = [];
    for (const [k, b] of buckets) {
      const used = new Uint8Array(b.segs.length);
      const walk = (from) => {
        const keys = [];
        let cur = from;
        for (;;) {
          const nxt = b.adj.get(cur).find((x) => !used[x]);
          if (nxt === undefined) break;
          used[nxt] = 1;
          const [a, c] = b.segs[nxt];
          cur = a === cur ? c : a;
          keys.push(cur);
        }
        return keys;
      };
      for (let s = 0; s < b.segs.length; s++) {
        if (used[s]) continue;
        used[s] = 1;
        const [ka, kb] = b.segs[s];
        const fwd = walk(kb), back = walk(ka);
        const keys = [...back.reverse(), ka, kb, ...fwd];
        const closed = keys[0] === keys[keys.length - 1];
        const pts = keys.map((q) => b.pts.get(q));
        if (closed) pts.pop();
        if (pts.length < 4) continue;
        out.push({ k, closed, pts });
      }
    }
    return out;
  }

  let W = 0, H = 0, dpr = 1, F = null;
  let cachedScene = null;
  let offscreen = null;
  const noise = perlin(11);
  const wob = perlin(47);
  const toPx = ([u, v]) => [F.x + u * F.w, F.y + v * F.h];

  // 3D Elevation & Tilt offset state
  window.furrow3D = {
    tiltX: 0,
    tiltY: 0,
    reliefDepth: 1.0, // Controlled by notebook relief switch
    loupeEnabled: true
  };

  function layout() {
    const hr = hero.getBoundingClientRect();
    W = Math.round(hr.width); H = Math.round(hr.height);
    dpr = Math.min(2, window.devicePixelRatio || 1);
    const mobile = W < 960;
    let ax = mobile ? -W * 0.04 : W * 0.36;
    let ay = mobile ? H * 0.32 : H * 0.09;
    let aw = mobile ? W * 1.08 : W * 0.62;
    let ah = mobile ? H * 0.48 : H * 0.82;
    let fw = Math.max(120, Math.min(aw, ah * A));
    let fh = fw / A;
    F = { x: ax + (aw - fw) / 2, y: ay + (ah - fh) / 2, w: fw, h: fh };

    if (mapLayer) {
      mapLayer.style.setProperty('--fx', `${F.x}px`);
      mapLayer.style.setProperty('--fy', `${F.y}px`);
      mapLayer.style.setProperty('--fw', `${F.w}px`);
      mapLayer.style.setProperty('--fh', `${F.h}px`);
    }
  }

  function buildScene() {
    const cell = 6;
    const nx = Math.ceil(W / cell) + 2, ny = Math.ceil(H / cell) + 2;
    const field = new Float32Array(nx * ny);
    const streamIso = STREAM.map(([u, v]) => [u * A, v]);
    const hx = 0.52 * A;
    for (let j = 0; j < ny; j++) {
      for (let i = 0; i < nx; i++) {
        const X = (i * cell - F.x) / F.h, Y = (j * cell - F.y) / F.h;
        let d = Infinity;
        for (let s = 1; s < streamIso.length; s++) d = Math.min(d, segDist(X, Y, streamIso[s - 1][0], streamIso[s - 1][1], streamIso[s][0], streamIso[s][1]));
        const hill = 0.44 * Math.exp(-(((X - hx) ** 2) * 1.1 + ((Y + 0.08) ** 2) * 2.6) / 0.3);
        field[j * nx + i] = -0.92 * Y + 0.18 * X + 0.42 * fbm(noise, X * 1.35 + 11.3, Y * 1.35 + 4.1) + hill - 0.2 * Math.exp(-((d / 0.075) ** 2));
      }
    }

    const step = Math.max(0.015, 17 / F.h);
    const lines = trace(field, nx, ny, cell, step);
    let kmin = Infinity;
    for (const l of lines) kmin = Math.min(kmin, l.k);
    const contours = [];
    for (const l of lines) {
      const pts = chaikin(l.pts, l.closed, 2);
      const len = plen(pts);
      if (len < (l.closed ? 85 : 30)) continue;
      const index = (l.k - kmin) % 5 === 0;
      contours.push({ pts, index, len, level: l.k - kmin, value: 125 + 5 * (l.k - kmin), p: pathOf(pts, l.closed) });
    }

    const P = {};
    for (const n in V) P[n] = toPx(V[n]);
    const holding = [...HOLDING].map((n) => P[n]);
    const edgeSeen = new Map();
    for (const fld of FIELDS) {
      const r = [...fld.ring];
      for (let i = 0; i < r.length; i++) {
        const a = r[i], b = r[(i + 1) % r.length];
        const id = a < b ? `${a}-${b}` : `${b}-${a}`;
        if (!edgeSeen.has(id)) edgeSeen.set(id, [a < b ? a : b, a < b ? b : a]);
      }
    }

    const edges = [];
    let seed = 1;
    for (const [id, [a, b]] of edgeSeen) {
      const A0 = P[a], B0 = P[b];
      const len = Math.hypot(B0[0] - A0[0], B0[1] - A0[1]);
      const n = Math.max(2, Math.ceil(len / 12));
      const nxp = -(B0[1] - A0[1]) / len, nyp = (B0[0] - A0[0]) / len;
      const sd = seed++ * 3.7;
      const pts = [];
      for (let i = 0; i <= n; i++) {
        const t = i / n;
        const o = 2.2 * wob(sd, t * 3.1) * Math.sin(Math.PI * t);
        pts.push([A0[0] + (B0[0] - A0[0]) * t + nxp * o, A0[1] + (B0[1] - A0[1]) * t + nyp * o]);
      }
      edges.push({ id, pts, wall: WALLS.has(id), p: pathOf(pts) });
    }

    cachedScene = { contours, holding, edges, P };
    renderBaseCanvas();
  }

  function renderBaseCanvas() {
    if (!cachedScene) return;
    canvas.width = Math.round(W * dpr);
    canvas.height = Math.round(H * dpr);
    const ctx = canvas.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    // 1. Paper Base
    ctx.fillStyle = PAPER;
    ctx.fillRect(0, 0, W, H);

    // Subtle Drafting Fold Creases (for physical paper 3D depth)
    const foldX = W * 0.65;
    const gradFold = ctx.createLinearGradient(foldX - 18, 0, foldX + 18, 0);
    gradFold.addColorStop(0, 'rgba(30,27,24,0)');
    gradFold.addColorStop(0.46, 'rgba(30,27,24,0.035)');
    gradFold.addColorStop(0.50, 'rgba(255,255,255,0.45)');
    gradFold.addColorStop(1, 'rgba(30,27,24,0)');
    ctx.fillStyle = gradFold;
    ctx.fillRect(foldX - 18, 0, 36, H);

    const foldY = H * 0.52;
    const gradFoldY = ctx.createLinearGradient(0, foldY - 12, 0, foldY + 12);
    gradFoldY.addColorStop(0, 'rgba(30,27,24,0)');
    gradFoldY.addColorStop(0.5, 'rgba(30,27,24,0.025)');
    gradFoldY.addColorStop(0.52, 'rgba(255,255,255,0.35)');
    gradFoldY.addColorStop(1, 'rgba(30,27,24,0)');
    ctx.fillStyle = gradFoldY;
    ctx.fillRect(0, foldY - 12, W, 24);

    // 2. 3D Extruded Contour Lines (with Parallax elevation offset for 3D depth!)
    const relief = window.furrow3D.reliefDepth;
    const tx = window.furrow3D.tiltX * 14 * relief;
    const ty = window.furrow3D.tiltY * 14 * relief;

    for (const c of cachedScene.contours) {
      const zFactor = (c.level - 8) * 0.35; // Higher elevation lines shift more in 3D parallax!
      ctx.save();
      ctx.translate(tx * zFactor * 0.14, ty * zFactor * 0.14);

      // Soft 3D elevation drop shadow on index contours
      if (c.index && relief > 0.2) {
        ctx.save();
        ctx.translate(1.5, 2.5);
        ctx.strokeStyle = 'rgba(165, 125, 90, 0.12)';
        ctx.lineWidth = 1.6;
        ctx.stroke(c.p);
        ctx.restore();
      }

      ctx.strokeStyle = c.index ? CONTOUR(0.56) : CONTOUR(0.28);
      ctx.lineWidth = c.index ? 1.15 : 0.72;
      ctx.stroke(c.p);

      // Elevation number labels on major index contours
      if (c.index && c.pts.length > 25 && c.len > 180) {
        const idx = Math.floor(c.pts.length * 0.42);
        const pt = c.pts[idx];
        if (pt[0] > W * 0.34 && pt[0] < W * 0.94 && pt[1] > 70 && pt[1] < H - 40) {
          ctx.font = '500 9.5px "Red Hat Mono", monospace';
          ctx.fillStyle = PAPER;
          const label = String(c.value);
          const tw = ctx.measureText(label).width;
          ctx.fillRect(pt[0] - tw / 2 - 3, pt[1] - 6, tw + 6, 12);
          ctx.fillStyle = CONTOUR(0.88);
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(label, pt[0], pt[1]);
        }
      }
      ctx.restore();
    }

    // 3. Stream / Trade Canal
    const sPts = chaikin(STREAM.map(toPx), false, 2);
    ctx.strokeStyle = WATER(0.62);
    ctx.lineWidth = 2.4;
    ctx.stroke(pathOf(sPts));

    // 4. Tangerine Territory Boundary (Edged like a surveyor title plan)
    const hPath = pathOf(cachedScene.holding, true);
    ctx.fillStyle = TANGERINE(0.055);
    ctx.fill(hPath);
    ctx.strokeStyle = TANGERINE(0.24);
    ctx.lineWidth = 7;
    ctx.stroke(hPath);
    ctx.strokeStyle = INK(0.82);
    ctx.lineWidth = 1.4;
    ctx.stroke(hPath);

    // 5. Internal Hedged Parcel Boundaries & Architectural Hatching
    for (const e of cachedScene.edges) {
      ctx.strokeStyle = e.wall ? INK(0.75) : HEDGE(0.62);
      ctx.lineWidth = e.wall ? 1.5 : 1.05;
      ctx.setLineDash(e.wall ? [] : [3, 4]);
      ctx.stroke(e.p);
    }
    ctx.setLineDash([]);

    // Logistics Hub Buildings (Hatched Blocks)
    for (const [bx, by, bw, bh] of BUILDINGS) {
      const [px, py] = toPx([bx, by]);
      const pw = bw * F.w, ph = bh * F.h;
      ctx.fillStyle = PAPER2;
      ctx.fillRect(px, py, pw, ph);
      ctx.strokeStyle = INK(0.75);
      ctx.lineWidth = 1.1;
      ctx.strokeRect(px, py, pw, ph);
      // 45-deg surveyor hatching
      ctx.beginPath();
      for (let d = -ph; d < pw; d += 5) {
        ctx.moveTo(px + Math.max(0, d), py + Math.max(0, -d));
        ctx.lineTo(px + Math.min(pw, d + ph), py + Math.min(ph, pw - d));
      }
      ctx.strokeStyle = INK(0.25);
      ctx.lineWidth = 0.7;
      ctx.stroke();
    }

    // 6. Field / Region Labels
    ctx.font = '500 11.5px "Red Hat Text", sans-serif';
    ctx.fillStyle = INK(0.68);
    ctx.textAlign = 'center';
    for (const f of FIELDS) {
      const [lx, ly] = toPx(f.at);
      ctx.fillText(f.name, lx, ly);
    }

    // Snapshot offscreen for 1.9x Optical Loupe magnification
    offscreen = document.createElement('canvas');
    offscreen.width = canvas.width;
    offscreen.height = canvas.height;
    offscreen.getContext('2d').drawImage(canvas, 0, 0);
  }

  // Interactive 1.9x Magnifying Optical Loupe
  let lx = 0, ly = 0, tlx = 0, tly = 0, loupeSize = 152;
  function initLoupe() {
    if (!loupe) return;
    loupe.width = loupeSize * dpr;
    loupe.height = loupeSize * dpr;
    // Default position over Southeast Core / Gate
    if (F) {
      tlx = lx = F.x + F.w * 0.28;
      tly = ly = F.y + F.h * 0.44;
    }
  }

  hero.addEventListener('pointermove', (e) => {
    const r = hero.getBoundingClientRect();
    const mx = e.clientX - r.left;
    const my = e.clientY - r.top;
    tlx = mx;
    tly = my;
    window.furrow3D.tiltX = (mx / W - 0.5) * 2;
    window.furrow3D.tiltY = (my / H - 0.5) * 2;
  });

  function animateLoupe() {
    if (!reduce && window.furrow3D.loupeEnabled && loupe && offscreen) {
      lx += (tlx - lx) * 0.14;
      ly += (tly - ly) * 0.14;

      // Only show loupe prominently over the map area
      const overMap = lx > W * 0.25 && ly > 50;
      loupe.style.opacity = overMap ? '1' : '0';
      loupe.style.transform = `translate3d(${(lx - loupeSize / 2).toFixed(1)}px, ${(ly - loupeSize / 2).toFixed(1)}px, 0)`;

      const lctx = loupe.getContext('2d');
      lctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      lctx.clearRect(0, 0, loupeSize, loupeSize);

      lctx.save();
      lctx.beginPath();
      lctx.arc(loupeSize / 2, loupeSize / 2, loupeSize / 2 - 2, 0, Math.PI * 2);
      lctx.clip();

      // 1.9x Optical Zoom
      const zoom = 1.9;
      const srcR = (loupeSize / 2) / zoom;
      lctx.drawImage(
        offscreen,
        (lx - srcR) * dpr, (ly - srcR) * dpr, srcR * 2 * dpr, srcR * 2 * dpr,
        0, 0, loupeSize, loupeSize
      );

      // Glass radial specular lens curvature
      const lensGrad = lctx.createRadialGradient(loupeSize * 0.35, loupeSize * 0.3, 4, loupeSize / 2, loupeSize / 2, loupeSize / 2);
      lensGrad.addColorStop(0, 'rgba(255,255,255,0.32)');
      lensGrad.addColorStop(0.6, 'rgba(255,255,255,0.02)');
      lensGrad.addColorStop(1, 'rgba(30,27,24,0.16)');
      lctx.fillStyle = lensGrad;
      lctx.fillRect(0, 0, loupeSize, loupeSize);

      // Precision Surveyor Crosshair Reticle
      lctx.strokeStyle = 'rgba(30,27,24,0.38)';
      lctx.lineWidth = 0.8;
      lctx.beginPath();
      lctx.moveTo(loupeSize / 2 - 12, loupeSize / 2); lctx.lineTo(loupeSize / 2 + 12, loupeSize / 2);
      lctx.moveTo(loupeSize / 2, loupeSize / 2 - 12); lctx.lineTo(loupeSize / 2, loupeSize / 2 + 12);
      lctx.stroke();
      lctx.restore();

      // Machined Outer Bezel Ring
      lctx.beginPath();
      lctx.arc(loupeSize / 2, loupeSize / 2, loupeSize / 2 - 2, 0, Math.PI * 2);
      lctx.strokeStyle = 'rgba(30, 27, 24, 0.78)';
      lctx.lineWidth = 1.5;
      lctx.stroke();
    }

    requestAnimationFrame(animateLoupe);
  }

  // Pin selection logic (updates Fieldbook Notebook card & route!)
  const pinData = {
    se: { kind: 'Southeast Hub', date: 'Active Core', time: '64.6%', cells: [['Gross Rev', 'R$ 10.23M'], ['Orders', '67,706'], ['Regional AOV', 'R$ 151.13'], ['Freight Share', '13.14%']] },
    ne: { kind: 'Northeast Corridor', date: 'Logistics Alert', time: '11.9%', cells: [['Gross Rev', 'R$ 1.88M'], ['Orders', '9,336'], ['Regional AOV', 'R$ 201.46'], ['Freight Share', '17.83%']] },
    ml: { kind: 'ML Churn Core', date: 'GBDT Classifier', time: '0.9998', cells: [['Accuracy', '99.28%'], ['Precision', '98.98%'], ['Recall', '99.83%'], ['Profiles', '95,458']] }
  };

  window.selectSurveyPin = (id) => {
    const info = pinData[id] || pinData.se;
    pins.forEach(p => {
      const on = p.dataset.pin === id;
      p.classList.toggle('is-on', on);
    });
    const elKind = document.getElementById('fb-kind');
    const elDate = document.getElementById('fb-date');
    const elTime = document.getElementById('fb-time');
    if (elKind) elKind.textContent = info.kind;
    if (elDate) elDate.textContent = info.date;
    if (elTime) elTime.textContent = info.time;
    info.cells.forEach(([dt, dd], idx) => {
      const dtEl = document.getElementById(`fb-dt-${idx}`);
      const ddEl = document.getElementById(`fb-dd-${idx}`);
      if (dtEl) dtEl.textContent = dt;
      if (ddEl) ddEl.textContent = dd;
    });
  };

  pins.forEach(p => {
    p.addEventListener('click', () => window.selectSurveyPin(p.dataset.pin));
  });

  // Initialize & Re-build on Resize
  function init() {
    layout();
    buildScene();
    initLoupe();
  }
  init();
  window.addEventListener('resize', init);
  requestAnimationFrame(animateLoupe);
})();

