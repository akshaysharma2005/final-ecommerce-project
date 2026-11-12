/* NEXUS.AI 3D Telemetry Point Cloud Engine
 * Adapted from Hallmark Vantage WebGL spatial architecture
 * Renders interactive 3D terrain, stacked order clusters, and sweeping scan planes
 */
(() => {
  const canvas = document.getElementById('cloud-canvas');
  if (!canvas) return;

  const gl = canvas.getContext('webgl', {
    antialias: false,
    premultipliedAlpha: true,
    alpha: true,
    powerPreference: 'high-performance'
  });
  if (!gl) return;

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const DPR = Math.min(window.devicePixelRatio || 1, 2);

  // Live reactive parameters controlled by Ribbon 3D Login Faders
  window.nexus3D = {
    density: 0.98,   // Fader 1: Data Depth (0..1)
    luminance: 0.72, // Fader 2: Scan Sweep Intensity (0..1)
    horizon: 0.45    // Fader 3: 3D Pitch Horizon (0..1)
  };

  // Seeded procedural PRNG + 2D Value Noise (for organic e-commerce spatial topology)
  let seed = 20261112;
  const rnd = () => {
    seed |= 0;
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  const P = new Uint8Array(512);
  {
    const p = [...Array(256).keys()];
    for (let i = 255; i > 0; i--) {
      const j = Math.floor(rnd() * (i + 1));
      [p[i], p[j]] = [p[j], p[i]];
    }
    for (let i = 0; i < 512; i++) P[i] = p[i & 255];
  }
  const fade = (t) => t * t * (3 - 2 * t);
  const hash = (x, y) => P[(P[x & 255] + y) & 255] / 255;
  function vnoise(x, y) {
    const xi = Math.floor(x), yi = Math.floor(y);
    const xf = x - xi, yf = y - yi;
    const u = fade(xf), v = fade(yf);
    const a = hash(xi, yi), b = hash(xi + 1, yi);
    const c = hash(xi, yi + 1), d = hash(xi + 1, yi + 1);
    return (a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v) * 2 - 1;
  }
  const fbm = (x, y) => vnoise(x, y) * 0.55 + vnoise(x * 2.1, y * 2.1) * 0.28 + vnoise(x * 4.3, y * 4.3) * 0.12;
  const smooth = (a, b, x) => {
    const t = Math.max(0, Math.min(1, (x - a) / (b - a)));
    return t * t * (3 - 2 * t);
  };

  const W = 115, D = 88, PAD = 41.25;
  const PILE = { x: 34, z: -12, r: 16, h: 9.5 }; // High-density lime cluster peak in open view

  function ground(x, z) {
    let h = 39.0 + 0.035 * x + 0.022 * z + fbm(x * 0.017 + 3, z * 0.017 - 2) * 8.5 + fbm(x * 0.07, z * 0.07) * 0.7;
    const dx = Math.max(-44 - x, 0, x - 38), dz = Math.max(-32 - z, 0, z - 28);
    h = PAD + (h - PAD) * smooth(0, 11, Math.hypot(dx, dz));
    return h;
  }

  function pile(x, z) {
    const d = Math.hypot(x - PILE.x, z - PILE.z) / PILE.r;
    return d < 1 ? PILE.h * Math.pow(1 - d, 1.25) * (1 + 0.06 * vnoise(x * 0.4, z * 0.4)) : 0;
  }

  const pos = [], cls = [], rr = [], sh = [];
  const add = (x, y, z, c, h = 0.9) => {
    pos.push(x, y, z);
    cls.push(c);
    rr.push(rnd());
    sh.push(h);
  };

  const small = window.innerWidth < 768;
  const ROW = small ? 1.35 : 0.88;
  const STEP = small ? 0.45 : 0.34;

  const hs = (x, z) => {
    const e = 0.6;
    const gx = (ground(x + e, z) + pile(x + e, z) - ground(x - e, z) - pile(x - e, z)) / (2 * e);
    const gz = (ground(x, z + e) + pile(x, z + e) - ground(x, z - e) - pile(x, z - e)) / (2 * e);
    const n = [-gx * 2.2, 1, -gz * 2.2];
    const l = Math.hypot(...n);
    return Math.max(0, (n[0] * -0.55 + n[1] * 0.62 + n[2] * -0.56) / l);
  };

  // Terrain rows
  for (let z = -D; z <= D; z += ROW) {
    const bend = Math.sin(z * 0.013) * 1.8;
    for (let x = -W; x <= W; x += STEP * (0.7 + rnd() * 0.6)) {
      const zz = z + bend * (x / W) + (rnd() - 0.5) * 0.18;
      const p = pile(x, zz);
      add(x, ground(x, zz) + p + (rnd() - 0.5) * 0.06, zz, p > 0.35 ? 3 : 0, hs(x, zz));
    }
  }

  // Central Marketplace Data Core (Architectural Wireframe Lattice)
  const core = { x0: -20, x1: 6, z0: -14, z1: 8, top: PAD + 14.5 };
  for (let i = 0; i < 4800; i++) {
    const y = PAD + rnd() * (core.top - PAD);
    const t = rnd();
    const s = Math.floor(rnd() * 4);
    const x = s < 2 ? core.x0 + t * (core.x1 - core.x0) : (s === 2 ? core.x0 : core.x1);
    const z = s < 2 ? (s ? core.z1 : core.z0) : core.z0 + t * (core.z1 - core.z0);
    add(x, y, z, 1, 0.95);
  }
  // Core floor slabs
  for (let level = 1; level <= 3; level++) {
    const ly = PAD + level * 4.2;
    for (let x = core.x0; x <= core.x1; x += 0.75) {
      for (let z = core.z0; z <= core.z1; z += 0.75) {
        if (rnd() > 0.25) add(x, ly, z, 1, 0.85);
      }
    }
  }

  // Telemetry Spire / Crane Antenna
  const CR = { x: 14, z: -12, top: PAD + 36 };
  const line = (a, b, step) => {
    const L = Math.hypot(b[0] - a[0], b[1] - a[1], b[2] - a[2]);
    const n = Math.ceil(L / step);
    for (let i = 0; i <= n; i++) {
      const t = i / n;
      add(
        a[0] + (b[0] - a[0]) * t + (rnd() - 0.5) * 0.12,
        a[1] + (b[1] - a[1]) * t,
        a[2] + (b[2] - a[2]) * t + (rnd() - 0.5) * 0.12,
        1,
        1.0
      );
    }
  };
  const legs = [[-0.8, -0.8], [0.8, -0.8], [0.8, 0.8], [-0.8, 0.8]];
  legs.forEach(([lx, lz]) => line([CR.x + lx, PAD, CR.z + lz], [CR.x + lx, CR.top, CR.z + lz], 0.18));
  line([CR.x - 10, CR.top, CR.z], [CR.x + 40, CR.top, CR.z], 0.18);
  line([CR.x, CR.top, CR.z], [CR.x, CR.top + 7, CR.z], 0.18);
  line([CR.x, CR.top + 7, CR.z], [CR.x + 34, CR.top, CR.z], 0.24);
  line([CR.x, CR.top + 7, CR.z], [CR.x - 9, CR.top, CR.z], 0.24);

  const N = cls.length;
  const POS = new Float32Array(pos);
  const CLS = new Float32Array(cls);
  const RND = new Float32Array(rr);
  const SHD = new Float32Array(sh);

  // Shaders
  const VS = `
    attribute vec3 p;
    attribute float c;
    attribute float r;
    attribute float sh;
    uniform mat4 m;
    uniform vec2 off;
    uniform float dpr, size, sweep, alpha, density, lum, near, far;
    uniform vec3 lo, mid, hi, acc;
    uniform vec2 hr, ext;
    varying vec4 col;
    void main() {
      if (r > density) {
        gl_Position = vec4(3.0, 3.0, 3.0, 1.0);
        col = vec4(0.0);
        return;
      }
      vec4 q = m * vec4(p, 1.0);
      q.xy += off * q.w;
      gl_Position = q;

      float h = clamp((p.y - hr.x) / (hr.y - hr.x), 0.0, 1.0);
      vec3 k = h < 0.5 ? mix(lo, mid, h * 2.0) : mix(mid, hi, (h - 0.5) * 2.0);
      k *= (0.52 + 0.65 * sh);

      float d = sweep - p.x;
      float w = d >= 0.0 ? 0.6 * exp(-d / 2.6) + 0.4 * exp(-d / 22.0) : exp(d / 0.8);
      k = mix(k, hi * 1.25, min(1.0, w * lum * 1.3));

      if (c > 2.5) k = mix(k, acc, 0.92);
      float pop = c > 2.5 ? 1.0 : 0.0;

      float fd = clamp(1.0 - (q.w - near) / (far - near), 0.25, 1.0);
      float edge = smoothstep(1.0, 0.72, length(p.xz / ext));
      gl_PointSize = clamp(size * dpr * 260.0 / q.w * (0.8 + 0.4 * r) * (1.0 + 0.35 * w), 1.0 * dpr, 3.8 * dpr);
      col = vec4(k, mix(fd * edge * min(1.0, 0.72 + 0.5 * w), edge, pop) * alpha);
    }
  `;

  const FS = `
    precision mediump float;
    varying vec4 col;
    void main() {
      vec2 d = gl_PointCoord - 0.5;
      float e = dot(d, d);
      if (e > 0.25) discard;
      float a = col.a * smoothstep(0.25, 0.12, e);
      gl_FragColor = vec4(col.rgb * a, a);
    }
  `;

  const mk = (t, s) => {
    const x = gl.createShader(t);
    gl.shaderSource(x, s);
    gl.compileShader(x);
    return x;
  };
  const pr = gl.createProgram();
  gl.attachShader(pr, mk(gl.VERTEX_SHADER, VS));
  gl.attachShader(pr, mk(gl.FRAGMENT_SHADER, FS));
  gl.linkProgram(pr);
  gl.useProgram(pr);

  const buf = (data, name) => {
    const b = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, b);
    gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
    const l = gl.getAttribLocation(pr, name);
    gl.enableVertexAttribArray(l);
    gl.vertexAttribPointer(l, data === POS ? 3 : 1, gl.FLOAT, false, 0, 0);
  };
  buf(POS, 'p'); buf(CLS, 'c'); buf(RND, 'r'); buf(SHD, 'sh');

  const U = {};
  ['m', 'off', 'dpr', 'size', 'sweep', 'alpha', 'density', 'lum', 'near', 'far', 'lo', 'mid', 'hi', 'acc', 'hr', 'ext']
    .forEach(n => U[n] = gl.getUniformLocation(pr, n));

  // Vantage Colorway Tokens (Deep Steel -> Pale Steel -> Chromatic Lime)
  gl.uniform3fv(U.lo, [0.22, 0.30, 0.42]);
  gl.uniform3fv(U.mid, [0.58, 0.67, 0.78]);
  gl.uniform3fv(U.hi, [0.92, 0.96, 1.00]);
  gl.uniform3fv(U.acc, [0.80, 0.98, 0.25]); // Chromatic Lime (#cbf644)
  gl.uniform2f(U.hr, 35, 56);
  gl.uniform2f(U.ext, W + 4, D + 4);
  gl.uniform1f(U.dpr, DPR);

  gl.enable(gl.BLEND);
  gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
  gl.disable(gl.DEPTH_TEST);

  // Matrix helpers
  const persp = (fov, asp, n, f) => {
    const t = 1 / Math.tan(fov / 2);
    return [t / asp, 0, 0, 0, 0, t, 0, 0, 0, 0, (f + n) / (n - f), -1, 0, 0, (2 * f * n) / (n - f), 0];
  };
  const lookAt = (e, c) => {
    let zx = e[0] - c[0], zy = e[1] - c[1], zz = e[2] - c[2];
    let l = Math.hypot(zx, zy, zz);
    zx /= l; zy /= l; zz /= l;
    let xx = zz, xy = 0, xz = -zx;
    l = Math.hypot(xx, xy, xz);
    xx /= l; xz /= l;
    const yx = zy * xz - zz * xy, yy = zz * xx - zx * xz, yz = zx * xy - zy * xx;
    return [xx, yx, zx, 0, xy, yy, zy, 0, xz, yz, zz, 0, -(xx * e[0] + xy * e[1] + xz * e[2]), -(yx * e[0] + yy * e[1] + yz * e[2]), -(zx * e[0] + zy * e[1] + zz * e[2]), 1];
  };
  const mul = (a, b) => {
    const o = new Array(16);
    for (let i = 0; i < 4; i++)
      for (let j = 0; j < 4; j++) {
        let s = 0;
        for (let k = 0; k < 4; k++) s += a[k * 4 + j] * b[i * 4 + k];
        o[i * 4 + j] = s;
      }
    return o;
  };

  let w = 0, h = 0, yaw = 0.58, px = 0, py = 0, tpx = 0, tpy = 0, alpha = 0;
  let mvp = null;
  let currentOff = [-0.15, -0.05];

  function resize() {
    const r = canvas.getBoundingClientRect();
    w = r.width; h = r.height;
    canvas.width = Math.round(w * DPR);
    canvas.height = Math.round(h * DPR);
    gl.viewport(0, 0, canvas.width, canvas.height);
  }
  resize();
  window.addEventListener('resize', resize);

  window.addEventListener('pointermove', (e) => {
    tpx = (e.clientX / window.innerWidth - 0.5) * 2;
    tpy = (e.clientY / window.innerHeight - 0.5) * 2;
  });

  // Floating 3D Callout Tags projected directly onto 3D Coordinates
  const callout1 = document.getElementById('callout-gmv');
  const callout2 = document.getElementById('callout-auc');
  function project(p) {
    if (!mvp) return null;
    const x = mvp[0] * p[0] + mvp[4] * p[1] + mvp[8] * p[2] + mvp[12];
    const y = mvp[1] * p[0] + mvp[5] * p[1] + mvp[9] * p[2] + mvp[13];
    const w_ = mvp[3] * p[0] + mvp[7] * p[1] + mvp[11] * p[2] + mvp[15];
    if (w_ <= 0) return null;
    return [((x / w_ + currentOff[0]) * 0.5 + 0.5) * w, (1 - ((y / w_ + currentOff[1]) * 0.5 + 0.5)) * h];
  }

  let t0 = performance.now(), last = performance.now();
  function render(now) {
    const dt = Math.min(0.05, (now - last) / 1000);
    last = now;
    const t = (now - t0) / 1000;

    if (!reduce) yaw += dt * ((Math.PI * 2) / 105);
    alpha = Math.min(1, alpha + dt * 1.4);
    px += (tpx - px) * Math.min(1, 3 * dt);
    py += (tpy - py) * Math.min(1, 3 * dt);

    const pitch = (0.28 + window.nexus3D.horizon * 0.45) + py * 0.05;
    const dist = w < 960 ? 270 : 240;
    const tg = [14, 46, -6];
    const effYaw = yaw + px * 0.09;
    const eye = [tg[0] + dist * Math.cos(pitch) * Math.sin(effYaw), tg[1] + dist * Math.sin(pitch), tg[2] + dist * Math.cos(pitch) * Math.cos(effYaw)];

    currentOff = w < 960 ? [0.0, -0.3] : [-0.02, -0.05];
    mvp = mul(persp(0.62, w / (h || 1), 20, 900), lookAt(eye, tg));

    // Sweep wave crosses terrain every 7s
    const period = 7.2, cross = 5.6;
    const k = (t % period) / cross;
    const e = k <= 1 ? (k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2) : 999;
    const sweepVal = k <= 1 ? -W - 12 + e * (2 * W + 24) : 999;

    gl.clearColor(0, 0, 0, 0);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.uniformMatrix4fv(U.m, false, mvp);
    gl.uniform2fv(U.off, currentOff);
    gl.uniform1f(U.size, 1.35);
    gl.uniform1f(U.alpha, alpha);
    gl.uniform1f(U.density, 0.25 + window.nexus3D.density * 0.75);
    gl.uniform1f(U.lum, 0.4 + window.nexus3D.luminance * 0.9);
    gl.uniform1f(U.near, dist - 165);
    gl.uniform1f(U.far, dist + 165);
    gl.uniform1f(U.sweep, sweepVal);

    gl.drawArrays(gl.POINTS, 0, N);

    // Update 3D projected callouts in clear center gap
    if (callout1) {
      const p1 = project([14, CR.top - 4, -12]);
      if (p1 && w >= 960 && p1[0] > w * 0.36 && p1[0] < w * 0.60) {
        callout1.style.transform = `translate3d(${p1[0].toFixed(1)}px, ${p1[1].toFixed(1)}px, 0)`;
        callout1.style.opacity = alpha;
      } else {
        callout1.style.opacity = 0;
      }
    }
    if (callout2) {
      const p2 = project([PILE.x, ground(PILE.x, PILE.z) + PILE.h, PILE.z]);
      if (p2 && w >= 960 && p2[0] > w * 0.36 && p2[0] < w * 0.62) {
        callout2.style.transform = `translate3d(${p2[0].toFixed(1)}px, ${p2[1].toFixed(1)}px, 0)`;
        callout2.style.opacity = alpha;
      } else {
        callout2.style.opacity = 0;
      }
    }

    if (!reduce) requestAnimationFrame(render);
  }
  requestAnimationFrame(render);
})();
