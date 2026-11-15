"""
World Monitor Telemetry & Intelligence Data Provider
Integrates global situational awareness from worldmonitor-main:
- Strategic Maritime Chokepoints & Mega-Ports
- Global Consumer Prices & Retail Inflation Baskets
- Country Instability Index (CII v14) & Sourcing Risk
- Digital Infrastructure, Subsea Cables & Logistics Incidents

Fully parameterized by operating year (2016, 2017, 2018, all).
"""

def get_chokepoints_data(year="all"):
    """Returns canonical maritime chokepoints and top container mega-ports telemetry parameterized by year."""
    y = str(year)

    if y == "2016":
        chokepoints = [
            {"id": "suez", "name": "Suez Canal", "region": "Egypt / Red Sea", "lat": 30.5, "lon": 32.3, "daily_transits": 68, "baseline_transits": 70, "flow_pct": 97.1, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "New parallel canal expansion recently opened; nominal passage", "reroute_name": "Cape of Good Hope", "reroute_days": "+0.0 days", "reroute_cost": "$0 (Standard Route)", "annual_teu": "17.2M TEU normal", "key_routes": ["China → Europe", "Gulf → Europe"]},
            {"id": "bab_el_mandeb", "name": "Bab el-Mandeb", "region": "Yemen / Djibouti", "lat": 12.58, "lon": 43.33, "daily_transits": 62, "baseline_transits": 64, "flow_pct": 96.9, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "International naval anti-piracy patrols active; commercial flow uninterrupted", "reroute_name": "Cape of Good Hope", "reroute_days": "+0.0 days", "reroute_cost": "$0 (Standard Route)", "annual_teu": "21.0M TEU normal", "key_routes": ["Asia → Mediterranean", "Asia → Europe"]},
            {"id": "malacca_strait", "name": "Strait of Malacca", "region": "Singapore / Malaysia", "lat": 1.43, "lon": 102.89, "daily_transits": 225, "baseline_transits": 230, "flow_pct": 97.8, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Navigational density; standard littoral radar monitoring", "reroute_name": "Sunda Strait", "reroute_days": "+3.0 days", "reroute_cost": "+$180,000 / voyage", "annual_teu": "84M TEU", "key_routes": ["East Asia → Europe", "China → Brazil"]},
            {"id": "hormuz_strait", "name": "Strait of Hormuz", "region": "Oman / Iran", "lat": 26.56, "lon": 56.25, "daily_transits": 130, "baseline_transits": 135, "flow_pct": 96.3, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Post-JCPOA agreement era; commercial tanker transit stable", "reroute_name": "East-West Pipeline", "reroute_days": "+3.8 days", "reroute_cost": "+$250,000 / voyage", "annual_teu": "19M bpd oil", "key_routes": ["Gulf → Asia", "Jebel Ali Hub"]},
            {"id": "panama", "name": "Panama Canal", "region": "Panama", "lat": 9.08, "lon": -79.68, "daily_transits": 36, "baseline_transits": 38, "flow_pct": 94.7, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Inauguration of Neopanamax expanded locks (June 2016)", "reroute_name": "US Intermodal Rail", "reroute_days": "+5.5 days", "reroute_cost": "+$320,000 / voyage", "annual_teu": "12.5M TEU", "key_routes": ["East Asia → US East Coast"]},
            {"id": "bosphorus", "name": "Bosporus Strait", "region": "Turkey", "lat": 41.12, "lon": 29.08, "daily_transits": 40, "baseline_transits": 45, "flow_pct": 88.9, "status": "elevated", "risk_level": "Elevated Vigilance", "primary_issue": "Heightened Turkish naval security inspections following July 2016 event", "reroute_name": "Danube Corridor", "reroute_days": "+4.2 days", "reroute_cost": "+$140,000 / voyage", "annual_teu": "3.1M TEU", "key_routes": ["Black Sea → Mediterranean"]},
            {"id": "dover_strait", "name": "Dover Strait", "region": "UK / France", "lat": 51.10, "lon": 1.45, "daily_transits": 487, "baseline_transits": 490, "flow_pct": 99.4, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Standard English Channel traffic separation scheme", "reroute_name": "North Sea Around Scotland", "reroute_days": "+2.0 days", "reroute_cost": "+$80,000 / voyage", "annual_teu": "34M TEU", "key_routes": ["Atlantic → Rotterdam / Hamburg"]}
        ]
        ports = [
            {"id": "shanghai", "name": "Port of Shanghai", "country": "China", "teu": 37.1, "rank": 1, "dwell_days": 2.3, "status": "nominal", "congestion": "Low"},
            {"id": "singapore", "name": "Port of Singapore", "country": "Singapore", "teu": 30.9, "rank": 2, "dwell_days": 2.7, "status": "nominal", "congestion": "Low"},
            {"id": "ningbo", "name": "Ningbo-Zhoushan", "country": "China", "teu": 21.6, "rank": 3, "dwell_days": 2.5, "status": "nominal", "congestion": "Low"},
            {"id": "shenzhen", "name": "Port of Shenzhen", "country": "China", "teu": 24.0, "rank": 4, "dwell_days": 2.2, "status": "nominal", "congestion": "Low"},
            {"id": "guangzhou", "name": "Port of Guangzhou", "country": "China", "teu": 18.8, "rank": 5, "dwell_days": 2.4, "status": "nominal", "congestion": "Low"},
            {"id": "busan", "name": "Port of Busan", "country": "South Korea", "teu": 19.8, "rank": 6, "dwell_days": 2.6, "status": "nominal", "congestion": "Low"},
            {"id": "rotterdam", "name": "Port of Rotterdam", "country": "Netherlands", "teu": 12.4, "rank": 10, "dwell_days": 3.1, "status": "nominal", "congestion": "Low"},
            {"id": "jebel_ali", "name": "Jebel Ali (Dubai)", "country": "UAE", "teu": 15.2, "rank": 11, "dwell_days": 2.8, "status": "nominal", "congestion": "Low"},
            {"id": "antwerp", "name": "Antwerp-Bruges", "country": "Belgium", "teu": 10.0, "rank": 12, "dwell_days": 3.0, "status": "nominal", "congestion": "Low"},
            {"id": "los_angeles", "name": "Port of Los Angeles", "country": "USA", "teu": 8.8, "rank": 16, "dwell_days": 3.4, "status": "nominal", "congestion": "Moderate"},
            {"id": "long_beach", "name": "Port of Long Beach", "country": "USA", "teu": 6.8, "rank": 17, "dwell_days": 3.2, "status": "nominal", "congestion": "Moderate"},
            {"id": "santos", "name": "Port of Santos", "country": "Brazil", "teu": 3.6, "rank": 38, "dwell_days": 4.1, "status": "nominal", "congestion": "Moderate"}
        ]
        freight_rates = {
            "months": ["Jan 16", "Feb 16", "Mar 16", "Apr 16", "May 16", "Jun 16", "Jul 16", "Aug 16", "Sep 16", "Oct 16", "Nov 16", "Dec 16"],
            "shanghai_rotterdam": [1420, 1310, 1180, 1250, 1380, 1490, 1580, 1620, 1540, 1480, 1590, 1680],
            "shanghai_la": [1280, 1190, 1120, 1180, 1290, 1380, 1450, 1510, 1460, 1410, 1520, 1610],
            "rotterdam_ny": [1120, 1080, 1050, 1090, 1140, 1180, 1210, 1250, 1230, 1190, 1260, 1310],
            "shanghai_santos": [1650, 1580, 1510, 1590, 1720, 1840, 1920, 1980, 1890, 1820, 1950, 2050]
        }
        summary = {"total_daily_transits": 1048, "baseline_daily_transits": 1072, "active_disruptions": 0, "elevated_corridors": 1, "cape_overhead_days": 0.0, "avg_port_dwell": 2.9}

    elif y == "2017":
        chokepoints = [
            {"id": "suez", "name": "Suez Canal", "region": "Egypt / Red Sea", "lat": 30.5, "lon": 32.3, "daily_transits": 70, "baseline_transits": 72, "flow_pct": 97.2, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Strong eastbound container flows; smooth northbound convoys", "reroute_name": "Cape of Good Hope", "reroute_days": "+0.0 days", "reroute_cost": "$0 (Standard Route)", "annual_teu": "18.5M TEU", "key_routes": ["China → Europe", "Gulf → Europe"]},
            {"id": "bab_el_mandeb", "name": "Bab el-Mandeb", "region": "Yemen / Djibouti", "lat": 12.58, "lon": 43.33, "daily_transits": 63, "baseline_transits": 64, "flow_pct": 98.4, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Naval advisory zone; merchant traffic operating normally", "reroute_name": "Cape of Good Hope", "reroute_days": "+0.0 days", "reroute_cost": "$0 (Standard Route)", "annual_teu": "22.5M TEU", "key_routes": ["Asia → Mediterranean"]},
            {"id": "malacca_strait", "name": "Strait of Malacca", "region": "Singapore / Malaysia", "lat": 1.43, "lon": 102.89, "daily_transits": 238, "baseline_transits": 240, "flow_pct": 99.2, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Record high transshipment volumes through Singapore hub", "reroute_name": "Sunda Strait", "reroute_days": "+3.2 days", "reroute_cost": "+$195,000 / voyage", "annual_teu": "88M TEU", "key_routes": ["East Asia → Europe", "China → Brazil"]},
            {"id": "hormuz_strait", "name": "Strait of Hormuz", "region": "Oman / Iran", "lat": 26.56, "lon": 56.25, "daily_transits": 132, "baseline_transits": 135, "flow_pct": 97.8, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Stable petroleum exports powering emerging market growth", "reroute_name": "East-West Pipeline", "reroute_days": "+4.0 days", "reroute_cost": "+$280,000 / voyage", "annual_teu": "20M bpd oil", "key_routes": ["Gulf → Global Markets"]},
            {"id": "panama", "name": "Panama Canal", "region": "Panama", "lat": 9.08, "lon": -79.68, "daily_transits": 38, "baseline_transits": 38, "flow_pct": 100.0, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Neopanamax locks operating at full capacity; record LNG transits", "reroute_name": "US Intermodal Rail", "reroute_days": "+6.0 days", "reroute_cost": "+$360,000 / voyage", "annual_teu": "13.8M TEU", "key_routes": ["East Asia → US East Coast"]},
            {"id": "bosphorus", "name": "Bosporus Strait", "region": "Turkey", "lat": 41.12, "lon": 29.08, "daily_transits": 43, "baseline_transits": 45, "flow_pct": 95.6, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Transit schedule normalized; standard pilotage requirements", "reroute_name": "Danube Corridor", "reroute_days": "+4.5 days", "reroute_cost": "+$150,000 / voyage", "annual_teu": "3.3M TEU", "key_routes": ["Black Sea → Mediterranean"]},
            {"id": "dover_strait", "name": "Dover Strait", "region": "UK / France", "lat": 51.10, "lon": 1.45, "daily_transits": 489, "baseline_transits": 490, "flow_pct": 99.8, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Pre-Brexit customs border free-flow; high maritime velocity", "reroute_name": "North Sea Around Scotland", "reroute_days": "+2.1 days", "reroute_cost": "+$85,000 / voyage", "annual_teu": "35M TEU", "key_routes": ["Atlantic → Rotterdam / Hamburg"]}
        ]
        ports = [
            {"id": "shanghai", "name": "Port of Shanghai", "country": "China", "teu": 40.2, "rank": 1, "dwell_days": 2.5, "status": "nominal", "congestion": "Low"},
            {"id": "singapore", "name": "Port of Singapore", "country": "Singapore", "teu": 33.7, "rank": 2, "dwell_days": 2.9, "status": "nominal", "congestion": "Low"},
            {"id": "ningbo", "name": "Ningbo-Zhoushan", "country": "China", "teu": 24.6, "rank": 3, "dwell_days": 2.7, "status": "nominal", "congestion": "Low"},
            {"id": "shenzhen", "name": "Port of Shenzhen", "country": "China", "teu": 25.2, "rank": 4, "dwell_days": 2.4, "status": "nominal", "congestion": "Low"},
            {"id": "guangzhou", "name": "Port of Guangzhou", "country": "China", "teu": 20.4, "rank": 5, "dwell_days": 2.6, "status": "nominal", "congestion": "Low"},
            {"id": "busan", "name": "Port of Busan", "country": "South Korea", "teu": 20.5, "rank": 6, "dwell_days": 2.8, "status": "nominal", "congestion": "Low"},
            {"id": "rotterdam", "name": "Port of Rotterdam", "country": "Netherlands", "teu": 13.7, "rank": 10, "dwell_days": 3.5, "status": "nominal", "congestion": "Moderate"},
            {"id": "jebel_ali", "name": "Jebel Ali (Dubai)", "country": "UAE", "teu": 15.4, "rank": 11, "dwell_days": 2.9, "status": "nominal", "congestion": "Low"},
            {"id": "antwerp", "name": "Antwerp-Bruges", "country": "Belgium", "teu": 10.5, "rank": 12, "dwell_days": 3.2, "status": "nominal", "congestion": "Moderate"},
            {"id": "los_angeles", "name": "Port of Los Angeles", "country": "USA", "teu": 9.3, "rank": 16, "dwell_days": 3.8, "status": "nominal", "congestion": "Moderate"},
            {"id": "long_beach", "name": "Port of Long Beach", "country": "USA", "teu": 7.5, "rank": 17, "dwell_days": 3.5, "status": "nominal", "congestion": "Moderate"},
            {"id": "santos", "name": "Port of Santos", "country": "Brazil", "teu": 3.9, "rank": 38, "dwell_days": 4.5, "status": "elevated", "congestion": "Moderate"}
        ]
        freight_rates = {
            "months": ["Jan 17", "Feb 17", "Mar 17", "Apr 17", "May 17", "Jun 17", "Jul 17", "Aug 17", "Sep 17", "Oct 17", "Nov 17", "Dec 17"],
            "shanghai_rotterdam": [1780, 1690, 1620, 1750, 1880, 1990, 2080, 2150, 2010, 1940, 2050, 2180],
            "shanghai_la": [1620, 1540, 1480, 1590, 1690, 1780, 1890, 1950, 1860, 1790, 1910, 2020],
            "rotterdam_ny": [1280, 1240, 1210, 1260, 1310, 1350, 1390, 1420, 1380, 1350, 1410, 1460],
            "shanghai_santos": [2120, 2050, 1980, 2090, 2240, 2380, 2490, 2560, 2450, 2380, 2510, 2640]
        }
        summary = {"total_daily_transits": 1073, "baseline_daily_transits": 1076, "active_disruptions": 0, "elevated_corridors": 0, "cape_overhead_days": 0.0, "avg_port_dwell": 3.1}

    elif y == "2018":
        chokepoints = [
            {"id": "suez", "name": "Suez Canal", "region": "Egypt / Red Sea", "lat": 30.5, "lon": 32.3, "daily_transits": 72, "baseline_transits": 72, "flow_pct": 100.0, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Pre-tariff trade front-loading volumes surging through canal", "reroute_name": "Cape of Good Hope", "reroute_days": "+0.0 days", "reroute_cost": "$0 (Standard Route)", "annual_teu": "19.8M TEU", "key_routes": ["China → Europe", "Gulf → Europe"]},
            {"id": "bab_el_mandeb", "name": "Bab el-Mandeb", "region": "Yemen / Djibouti", "lat": 12.58, "lon": 43.33, "daily_transits": 64, "baseline_transits": 64, "flow_pct": 100.0, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Coalition naval patrols maintain safe merchant transit corridors", "reroute_name": "Cape of Good Hope", "reroute_days": "+0.0 days", "reroute_cost": "$0 (Standard Route)", "annual_teu": "23.4M TEU", "key_routes": ["Asia → Mediterranean"]},
            {"id": "malacca_strait", "name": "Strait of Malacca", "region": "Singapore / Malaysia", "lat": 1.43, "lon": 102.89, "daily_transits": 242, "baseline_transits": 240, "flow_pct": 100.8, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Heavy container traffic; front-loading ahead of US tariffs", "reroute_name": "Sunda Strait", "reroute_days": "+3.4 days", "reroute_cost": "+$210,000 / voyage", "annual_teu": "91M TEU", "key_routes": ["East Asia → Europe", "China → Brazil"]},
            {"id": "hormuz_strait", "name": "Strait of Hormuz", "region": "Oman / Iran", "lat": 26.56, "lon": 56.25, "daily_transits": 126, "baseline_transits": 135, "flow_pct": 93.3, "status": "elevated", "risk_level": "Elevated Vigilance", "primary_issue": "US withdrawal from JCPOA (May 2018); sanctions compliance heightened", "reroute_name": "East-West Pipeline", "reroute_days": "+4.2 days", "reroute_cost": "+$310,000 / voyage", "annual_teu": "20.5M bpd oil", "key_routes": ["Gulf → Global Markets"]},
            {"id": "panama", "name": "Panama Canal", "region": "Panama", "lat": 9.08, "lon": -79.68, "daily_transits": 37, "baseline_transits": 38, "flow_pct": 97.4, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Early El Niño advisory; initial Gatun Lake water management protocols", "reroute_name": "US Intermodal Rail", "reroute_days": "+6.2 days", "reroute_cost": "+$390,000 / voyage", "annual_teu": "14.1M TEU", "key_routes": ["East Asia → US East Coast"]},
            {"id": "bosphorus", "name": "Bosporus Strait", "region": "Turkey", "lat": 41.12, "lon": 29.08, "daily_transits": 42, "baseline_transits": 45, "flow_pct": 93.3, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Lira currency crisis; Turkish customs inspection delays", "reroute_name": "Danube Corridor", "reroute_days": "+4.8 days", "reroute_cost": "+$160,000 / voyage", "annual_teu": "3.2M TEU", "key_routes": ["Black Sea → Mediterranean"]},
            {"id": "dover_strait", "name": "Dover Strait", "region": "UK / France", "lat": 51.10, "lon": 1.45, "daily_transits": 486, "baseline_transits": 490, "flow_pct": 99.2, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Brexit preparations; channel ferry contingency planning", "reroute_name": "North Sea Around Scotland", "reroute_days": "+2.2 days", "reroute_cost": "+$90,000 / voyage", "annual_teu": "35M TEU", "key_routes": ["Atlantic → Rotterdam / Hamburg"]}
        ]
        ports = [
            {"id": "shanghai", "name": "Port of Shanghai", "country": "China", "teu": 42.0, "rank": 1, "dwell_days": 2.8, "status": "nominal", "congestion": "Moderate"},
            {"id": "singapore", "name": "Port of Singapore", "country": "Singapore", "teu": 36.6, "rank": 2, "dwell_days": 3.1, "status": "nominal", "congestion": "Moderate"},
            {"id": "ningbo", "name": "Ningbo-Zhoushan", "country": "China", "teu": 26.4, "rank": 3, "dwell_days": 2.9, "status": "nominal", "congestion": "Moderate"},
            {"id": "shenzhen", "name": "Port of Shenzhen", "country": "China", "teu": 25.7, "rank": 4, "dwell_days": 2.6, "status": "nominal", "congestion": "Low"},
            {"id": "guangzhou", "name": "Port of Guangzhou", "country": "China", "teu": 21.9, "rank": 5, "dwell_days": 2.7, "status": "nominal", "congestion": "Low"},
            {"id": "busan", "name": "Port of Busan", "country": "South Korea", "teu": 21.7, "rank": 6, "dwell_days": 3.0, "status": "nominal", "congestion": "Moderate"},
            {"id": "rotterdam", "name": "Port of Rotterdam", "country": "Netherlands", "teu": 14.5, "rank": 10, "dwell_days": 4.1, "status": "elevated", "congestion": "Moderate"},
            {"id": "jebel_ali", "name": "Jebel Ali (Dubai)", "country": "UAE", "teu": 14.9, "rank": 11, "dwell_days": 3.1, "status": "nominal", "congestion": "Low"},
            {"id": "antwerp", "name": "Antwerp-Bruges", "country": "Belgium", "teu": 11.1, "rank": 12, "dwell_days": 3.6, "status": "nominal", "congestion": "Moderate"},
            {"id": "los_angeles", "name": "Port of Los Angeles", "country": "USA", "teu": 9.5, "rank": 16, "dwell_days": 4.4, "status": "elevated", "congestion": "High"},
            {"id": "long_beach", "name": "Port of Long Beach", "country": "USA", "teu": 8.1, "rank": 17, "dwell_days": 4.0, "status": "elevated", "congestion": "High"},
            {"id": "santos", "name": "Port of Santos", "country": "Brazil", "teu": 4.1, "rank": 38, "dwell_days": 5.8, "status": "critical", "congestion": "Severe (Trucker Strike)"}
        ]
        freight_rates = {
            "months": ["Jan 18", "Feb 18", "Mar 18", "Apr 18", "May 18", "Jun 18", "Jul 18", "Aug 18", "Sep 18", "Oct 18", "Nov 18", "Dec 18"],
            "shanghai_rotterdam": [2150, 2020, 1940, 2120, 2350, 2520, 2690, 2810, 2680, 2590, 2750, 2890],
            "shanghai_la": [1980, 1870, 1810, 1950, 2180, 2360, 2540, 2680, 2520, 2440, 2610, 2740],
            "rotterdam_ny": [1450, 1390, 1350, 1420, 1510, 1590, 1650, 1710, 1660, 1620, 1690, 1750],
            "shanghai_santos": [2580, 2460, 2390, 2550, 2790, 2980, 3150, 3280, 3120, 3040, 3210, 3360]
        }
        summary = {"total_daily_transits": 1069, "baseline_daily_transits": 1076, "active_disruptions": 0, "elevated_corridors": 1, "cape_overhead_days": 0.0, "avg_port_dwell": 3.5}

    else: # "all" - Contemporary World Monitor benchmark
        chokepoints = [
            {"id": "suez", "name": "Suez Canal", "region": "Egypt / Red Sea", "lat": 30.5, "lon": 32.3, "daily_transits": 38, "baseline_transits": 72, "flow_pct": 52.8, "status": "elevated", "risk_level": "Elevated Risk", "primary_issue": "Houthi drone/missile activity; partial Cape rerouting", "reroute_name": "Cape of Good Hope", "reroute_days": "+12.4 days", "reroute_cost": "+$840,000 / voyage", "annual_teu": "12.8M TEU diverted", "key_routes": ["China → Europe", "Gulf → Europe", "India → Europe"]},
            {"id": "bab_el_mandeb", "name": "Bab el-Mandeb", "region": "Yemen / Djibouti", "lat": 12.58, "lon": 43.33, "daily_transits": 26, "baseline_transits": 64, "flow_pct": 40.6, "status": "critical", "risk_level": "High Disruption", "primary_issue": "Naval conflict corridor, anti-ship ballistic strikes", "reroute_name": "Cape of Good Hope", "reroute_days": "+14.1 days", "reroute_cost": "+$950,000 / voyage", "annual_teu": "16.4M TEU diverted", "key_routes": ["Asia → Mediterranean", "Asia → Northern Europe"]},
            {"id": "malacca_strait", "name": "Strait of Malacca", "region": "Singapore / Malaysia / Indonesia", "lat": 1.43, "lon": 102.89, "daily_transits": 234, "baseline_transits": 240, "flow_pct": 97.5, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "High traffic density, shallow draft tidal windows", "reroute_name": "Sunda / Lombok Strait", "reroute_days": "+3.5 days", "reroute_cost": "+$210,000 / voyage", "annual_teu": "92M+ TEU total", "key_routes": ["East Asia → Europe", "East Asia → Middle East", "China → Brazil"]},
            {"id": "hormuz_strait", "name": "Strait of Hormuz", "region": "Oman / Iran", "lat": 26.56, "lon": 56.25, "daily_transits": 118, "baseline_transits": 135, "flow_pct": 87.4, "status": "elevated", "risk_level": "Elevated Vigilance", "primary_issue": "IRGC boarding attempts, GPS jamming incidents", "reroute_name": "East-West Pipeline / Fujairah", "reroute_days": "+4.2 days", "reroute_cost": "+$340,000 / voyage", "annual_teu": "21M bpd oil / 14M TEU", "key_routes": ["Persian Gulf → Global Markets", "Dubai Jebel Ali Hub"]},
            {"id": "panama", "name": "Panama Canal", "region": "Panama", "lat": 9.08, "lon": -79.68, "daily_transits": 34, "baseline_transits": 38, "flow_pct": 89.5, "status": "elevated", "risk_level": "Moderate Restrictions", "primary_issue": "Gatun Lake reservoir level draft limits (44ft max)", "reroute_name": "US Intermodal Rail / Cape Horn", "reroute_days": "+7.0 days", "reroute_cost": "+$480,000 / voyage", "annual_teu": "14.2M TEU total", "key_routes": ["East Asia → US East Coast", "South America → US Gulf"]},
            {"id": "bosphorus", "name": "Bosporus Strait", "region": "Turkey", "lat": 41.12, "lon": 29.08, "daily_transits": 42, "baseline_transits": 45, "flow_pct": 93.3, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Black Sea war-risk insurance premiums, daylight transits", "reroute_name": "Rail corridor (Baku-Tbilisi-Kars)", "reroute_days": "+5.8 days", "reroute_cost": "+$180,000 / voyage", "annual_teu": "3.5M TEU / 48M tons grain", "key_routes": ["Black Sea → Mediterranean", "Danube River → Global"]},
            {"id": "dover_strait", "name": "Dover Strait", "region": "UK / France", "lat": 51.10, "lon": 1.45, "daily_transits": 485, "baseline_transits": 490, "flow_pct": 99.0, "status": "normal", "risk_level": "Normal Operations", "primary_issue": "Channel weather squalls, ferry separation schemes", "reroute_name": "North Sea Around Scotland", "reroute_days": "+2.2 days", "reroute_cost": "+$95,000 / voyage", "annual_teu": "35M+ TEU total", "key_routes": ["Atlantic → Rotterdam / Antwerp / Hamburg"]}
        ]
        ports = [
            {"id": "shanghai", "name": "Port of Shanghai", "country": "China", "teu": 47.3, "rank": 1, "dwell_days": 2.8, "status": "nominal", "congestion": "Low"},
            {"id": "singapore", "name": "Port of Singapore", "country": "Singapore", "teu": 37.3, "rank": 2, "dwell_days": 3.4, "status": "nominal", "congestion": "Moderate"},
            {"id": "ningbo", "name": "Ningbo-Zhoushan", "country": "China", "teu": 33.4, "rank": 3, "dwell_days": 3.1, "status": "nominal", "congestion": "Moderate"},
            {"id": "shenzhen", "name": "Port of Shenzhen", "country": "China", "teu": 30.0, "rank": 4, "dwell_days": 2.6, "status": "nominal", "congestion": "Low"},
            {"id": "guangzhou", "name": "Port of Guangzhou", "country": "China", "teu": 24.2, "rank": 5, "dwell_days": 2.9, "status": "nominal", "congestion": "Low"},
            {"id": "busan", "name": "Port of Busan", "country": "South Korea", "teu": 22.1, "rank": 6, "dwell_days": 3.2, "status": "nominal", "congestion": "Moderate"},
            {"id": "rotterdam", "name": "Port of Rotterdam", "country": "Netherlands", "teu": 14.5, "rank": 10, "dwell_days": 4.6, "status": "elevated", "congestion": "High"},
            {"id": "jebel_ali", "name": "Jebel Ali (Dubai)", "country": "UAE", "teu": 14.0, "rank": 11, "dwell_days": 3.0, "status": "nominal", "congestion": "Low"},
            {"id": "antwerp", "name": "Antwerp-Bruges", "country": "Belgium", "teu": 13.5, "rank": 12, "dwell_days": 4.1, "status": "elevated", "congestion": "Moderate"},
            {"id": "los_angeles", "name": "Port of Los Angeles", "country": "USA", "teu": 9.2, "rank": 16, "dwell_days": 4.9, "status": "elevated", "congestion": "High"},
            {"id": "long_beach", "name": "Port of Long Beach", "country": "USA", "teu": 8.1, "rank": 17, "dwell_days": 4.5, "status": "elevated", "congestion": "High"},
            {"id": "santos", "name": "Port of Santos", "country": "Brazil", "teu": 4.8, "rank": 38, "dwell_days": 5.2, "status": "elevated", "congestion": "High"}
        ]
        freight_rates = {
            "months": ["Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "Oct 26"],
            "shanghai_rotterdam": [2150, 2480, 3950, 4820, 4400, 3850, 4120, 4650, 4980, 4420, 3900, 3680],
            "shanghai_la": [1980, 2150, 3100, 3850, 3600, 3250, 3450, 3920, 4150, 3800, 3400, 3180],
            "rotterdam_ny": [1450, 1520, 1680, 1850, 1920, 1950, 2050, 2120, 2180, 2100, 2020, 1980],
            "shanghai_santos": [2650, 2890, 3850, 4450, 4200, 3950, 4100, 4520, 4800, 4350, 4050, 3820]
        }
        summary = {"total_daily_transits": 947, "baseline_daily_transits": 1084, "active_disruptions": 2, "elevated_corridors": 3, "cape_overhead_days": 12.6, "avg_port_dwell": 3.7}

    return {
        "year": y,
        "chokepoints": chokepoints,
        "ports": ports,
        "freight_rates": freight_rates,
        "summary": summary
    }


def get_consumer_prices_data(year="all"):
    """Returns global retail inflation rates, category baskets, and retailer price spreads parameterized by year."""
    y = str(year)

    if y == "2016":
        markets = [
            {"market": "United States", "code": "US", "cpi_yoy": 1.3, "retail_yoy": 1.1, "electronics": -2.4, "apparel": 0.8, "home": 1.2, "freight": -3.5, "food": 0.3},
            {"market": "Eurozone", "code": "EU", "cpi_yoy": 0.2, "retail_yoy": 0.4, "electronics": -3.1, "apparel": 0.5, "home": 0.6, "freight": -4.2, "food": 0.1},
            {"market": "United Kingdom", "code": "UK", "cpi_yoy": 0.7, "retail_yoy": 0.9, "electronics": -1.8, "apparel": -1.2, "home": 0.4, "freight": -2.1, "food": -1.5},
            {"market": "Brazil", "code": "BR", "cpi_yoy": 8.7, "retail_yoy": 9.2, "electronics": 11.4, "apparel": 6.8, "home": 8.4, "freight": 12.6, "food": 9.5},
            {"market": "India", "code": "IN", "cpi_yoy": 4.9, "retail_yoy": 5.1, "electronics": 3.8, "apparel": 5.4, "home": 4.2, "freight": 4.6, "food": 5.2},
            {"market": "Japan", "code": "JP", "cpi_yoy": -0.1, "retail_yoy": 0.1, "electronics": -1.5, "apparel": 0.2, "home": -0.2, "freight": -1.8, "food": 0.4},
            {"market": "China", "code": "CN", "cpi_yoy": 2.0, "retail_yoy": 1.8, "electronics": -1.9, "apparel": 1.4, "home": 1.1, "freight": 0.8, "food": 4.6}
        ]
        retailer_spread = {
            "categories": ["Consumer Electronics", "Smart Home & IoT", "Sporting Goods", "Apparel & Shoes", "Home & Kitchen", "Beauty & Care", "Automotive Acc.", "Office Supplies"],
            "amazon": [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
            "walmart": [99.4, 98.8, 102.0, 97.5, 98.1, 100.2, 98.9, 96.8],
            "target": [103.5, 104.2, 105.1, 101.0, 103.4, 102.8, 104.0, 101.2],
            "dtc_brands": [112.0, 114.5, 118.0, 114.0, 116.5, 120.0, 110.0, 112.5],
            "aliexpress": [78.5, 75.0, 72.4, 66.8, 70.2, 75.5, 68.0, 65.4]
        }
        price_movers = [
            {"sku": "SKU-9921", "name": "SATA III 2.5-inch Internal SSD 500GB", "category": "Electronics", "prev_price": 79.99, "curr_price": 64.99, "delta_pct": -18.75, "reason": "NAND Flash fab capacity expansion price cuts", "direction": "down"},
            {"sku": "SKU-8412", "name": "Heavy Duty Deep-Cycle Marine Battery 12V", "category": "Automotive", "prev_price": 145.00, "curr_price": 139.00, "delta_pct": -4.14, "reason": "Lead commodity input price decline", "direction": "down"},
            {"sku": "SKU-7734", "name": "Merino Wool Blend Winter Overcoat", "category": "Apparel", "prev_price": 160.00, "curr_price": 172.00, "delta_pct": 7.50, "reason": "Import tariff pass-through adjustment", "direction": "up"},
            {"sku": "SKU-6120", "name": "Digital Slow Cooker Crock Pot 6L", "category": "Home & Kitchen", "prev_price": 69.95, "curr_price": 62.50, "delta_pct": -10.65, "reason": "Black Friday volume promotion rebate", "direction": "down"},
            {"sku": "SKU-5049", "name": "IPS 1080p 60Hz Desktop Monitor 24-inch", "category": "Electronics", "prev_price": 159.99, "curr_price": 139.99, "delta_pct": -12.50, "reason": "LCD panel oversupply discount", "direction": "down"}
        ]
        summary = {"global_retail_cpi": 1.4, "max_category_inflation": 9.2, "avg_retailer_dispersion": 11.2, "purchasing_power_impact": -1.5}

    elif y == "2017":
        markets = [
            {"market": "United States", "code": "US", "cpi_yoy": 2.1, "retail_yoy": 1.9, "electronics": -1.2, "apparel": 1.4, "home": 1.8, "freight": 2.1, "food": 0.9},
            {"market": "Eurozone", "code": "EU", "cpi_yoy": 1.5, "retail_yoy": 1.6, "electronics": -1.9, "apparel": 1.1, "home": 1.2, "freight": 1.8, "food": 1.6},
            {"market": "United Kingdom", "code": "UK", "cpi_yoy": 2.7, "retail_yoy": 2.9, "electronics": 2.4, "apparel": 2.1, "home": 2.5, "freight": 3.8, "food": 2.2},
            {"market": "Brazil", "code": "BR", "cpi_yoy": 3.5, "retail_yoy": 3.8, "electronics": 4.5, "apparel": 2.9, "home": 3.4, "freight": 4.8, "food": -1.9},
            {"market": "India", "code": "IN", "cpi_yoy": 3.3, "retail_yoy": 3.7, "electronics": 2.9, "apparel": 4.2, "home": 3.5, "freight": 3.2, "food": 1.8},
            {"market": "Japan", "code": "JP", "cpi_yoy": 0.5, "retail_yoy": 0.7, "electronics": -0.4, "apparel": 0.8, "home": 0.5, "freight": 1.1, "food": 0.7},
            {"market": "China", "code": "CN", "cpi_yoy": 1.6, "retail_yoy": 1.5, "electronics": -0.8, "apparel": 1.3, "home": 1.4, "freight": 1.9, "food": -1.4}
        ]
        retailer_spread = {
            "categories": ["Consumer Electronics", "Smart Home & IoT", "Sporting Goods", "Apparel & Shoes", "Home & Kitchen", "Beauty & Care", "Automotive Acc.", "Office Supplies"],
            "amazon": [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
            "walmart": [98.8, 98.1, 101.5, 96.4, 97.2, 99.5, 98.2, 95.8],
            "target": [102.9, 103.5, 104.8, 100.2, 103.1, 102.0, 103.6, 100.5],
            "dtc_brands": [113.2, 116.0, 120.5, 115.2, 118.0, 122.5, 111.0, 113.8],
            "aliexpress": [76.0, 73.2, 70.1, 64.5, 68.4, 73.8, 66.2, 63.0]
        }
        price_movers = [
            {"sku": "SKU-9921", "name": "DDR4 Desktop Gaming RAM 16GB Kit", "category": "Electronics", "prev_price": 89.99, "curr_price": 124.99, "delta_pct": 38.89, "reason": "Global DRAM silicon wafer shortage supercycle", "direction": "up"},
            {"sku": "SKU-8412", "name": "Smart Wi-Fi Indoor Security Camera 1080p", "category": "Smart Home", "prev_price": 69.00, "curr_price": 54.00, "delta_pct": -21.74, "reason": "Mass market IoT chipset cost reduction", "direction": "down"},
            {"sku": "SKU-7734", "name": "Breathable Athletic Running Sneakers", "category": "Apparel", "prev_price": 110.00, "curr_price": 118.00, "delta_pct": 7.27, "reason": "Raw polymer sole input cost adjustment", "direction": "up"}
        ]
        summary = {"global_retail_cpi": 2.1, "max_category_inflation": 4.5, "avg_retailer_dispersion": 12.8, "purchasing_power_impact": -0.8}

    elif y == "2018":
        markets = [
            {"market": "United States", "code": "US", "cpi_yoy": 2.4, "retail_yoy": 2.8, "electronics": 3.2, "apparel": 1.8, "home": 2.4, "freight": 6.4, "food": 1.4},
            {"market": "Eurozone", "code": "EU", "cpi_yoy": 1.8, "retail_yoy": 2.0, "electronics": 1.9, "apparel": 1.4, "home": 1.6, "freight": 3.8, "food": 1.9},
            {"market": "United Kingdom", "code": "UK", "cpi_yoy": 2.5, "retail_yoy": 2.7, "electronics": 2.8, "apparel": 1.9, "home": 2.4, "freight": 4.5, "food": 2.1},
            {"market": "Brazil", "code": "BR", "cpi_yoy": 3.7, "retail_yoy": 4.1, "electronics": 5.8, "apparel": 3.2, "home": 3.8, "freight": 7.2, "food": 4.0},
            {"market": "India", "code": "IN", "cpi_yoy": 3.9, "retail_yoy": 4.2, "electronics": 4.1, "apparel": 4.6, "home": 3.9, "freight": 5.1, "food": 2.8},
            {"market": "Japan", "code": "JP", "cpi_yoy": 1.0, "retail_yoy": 1.2, "electronics": 1.5, "apparel": 1.1, "home": 0.9, "freight": 2.4, "food": 1.2},
            {"market": "China", "code": "CN", "cpi_yoy": 2.1, "retail_yoy": 2.0, "electronics": 1.2, "apparel": 1.5, "home": 1.6, "freight": 2.5, "food": 1.8}
        ]
        retailer_spread = {
            "categories": ["Consumer Electronics", "Smart Home & IoT", "Sporting Goods", "Apparel & Shoes", "Home & Kitchen", "Beauty & Care", "Automotive Acc.", "Office Supplies"],
            "amazon": [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
            "walmart": [98.4, 97.6, 101.3, 96.0, 96.8, 99.2, 97.9, 95.4],
            "target": [102.6, 103.3, 104.6, 99.6, 103.0, 101.8, 103.4, 100.1],
            "dtc_brands": [114.0, 117.5, 121.2, 115.8, 118.8, 123.2, 111.8, 114.5],
            "aliexpress": [74.8, 72.1, 69.2, 63.0, 67.4, 72.8, 65.1, 62.0]
        }
        price_movers = [
            {"sku": "SKU-9921", "name": "Graphics Processing Unit 8GB VRAM", "category": "Electronics", "prev_price": 249.99, "curr_price": 319.99, "delta_pct": 28.00, "reason": "Cryptocurrency mining demand & VRAM shortage", "direction": "up"},
            {"sku": "SKU-8412", "name": "Diesel Fuel Injection Assembly Kit", "category": "Automotive", "prev_price": 189.00, "curr_price": 215.00, "delta_pct": 13.76, "reason": "National Brazilian trucker strike logistics disruption", "direction": "up"},
            {"sku": "SKU-7734", "name": "Stainless Steel Kitchenware Set 10-Piece", "category": "Home & Kitchen", "prev_price": 135.00, "curr_price": 152.00, "delta_pct": 12.59, "reason": "Section 232 global steel tariff impact", "direction": "up"}
        ]
        summary = {"global_retail_cpi": 2.8, "max_category_inflation": 5.8, "avg_retailer_dispersion": 13.9, "purchasing_power_impact": -2.1}

    else: # "all" - Contemporary World Monitor benchmark
        markets = [
            {"market": "United States", "code": "US", "cpi_yoy": 2.9, "retail_yoy": 3.4, "electronics": 4.8, "apparel": 2.2, "home": 3.1, "freight": 5.4, "food": 2.6},
            {"market": "Eurozone", "code": "EU", "cpi_yoy": 2.4, "retail_yoy": 2.8, "electronics": 3.9, "apparel": 1.9, "home": 2.4, "freight": 6.8, "food": 2.2},
            {"market": "United Kingdom", "code": "UK", "cpi_yoy": 3.2, "retail_yoy": 3.7, "electronics": 4.5, "apparel": 2.8, "home": 3.5, "freight": 7.1, "food": 3.0},
            {"market": "Brazil", "code": "BR", "cpi_yoy": 4.6, "retail_yoy": 5.8, "electronics": 7.4, "apparel": 4.2, "home": 4.9, "freight": 8.6, "food": 5.1},
            {"market": "India", "code": "IN", "cpi_yoy": 4.8, "retail_yoy": 5.2, "electronics": 5.6, "apparel": 3.8, "home": 4.5, "freight": 6.2, "food": 5.9},
            {"market": "Japan", "code": "JP", "cpi_yoy": 2.1, "retail_yoy": 2.4, "electronics": 3.2, "apparel": 1.6, "home": 2.0, "freight": 4.2, "food": 2.7},
            {"market": "China", "code": "CN", "cpi_yoy": 0.8, "retail_yoy": 1.2, "electronics": -1.5, "apparel": 0.6, "home": 0.4, "freight": 2.8, "food": 1.1}
        ]
        retailer_spread = {
            "categories": ["Consumer Electronics", "Smart Home & IoT", "Sporting Goods", "Apparel & Shoes", "Home & Kitchen", "Beauty & Care", "Automotive Acc.", "Office Supplies"],
            "amazon": [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
            "walmart": [98.2, 97.4, 101.2, 95.8, 96.5, 99.1, 97.8, 95.2],
            "target": [102.4, 103.1, 104.5, 99.2, 102.8, 101.5, 103.2, 99.8],
            "dtc_brands": [114.5, 118.2, 122.0, 116.4, 119.5, 124.0, 112.5, 115.0],
            "aliexpress": [74.2, 71.5, 68.4, 62.1, 66.8, 72.0, 64.5, 61.2]
        }
        price_movers = [
            {"sku": "SKU-9921", "name": "NVMe PCIe 4.0 SSD 2TB", "category": "Electronics", "prev_price": 129.99, "curr_price": 149.99, "delta_pct": 15.38, "reason": "NAND Flash contract price surge", "direction": "up"},
            {"sku": "SKU-8412", "name": "Lithium-Ion Portable Power Station 1000W", "category": "Home & Garden", "prev_price": 549.00, "curr_price": 599.00, "delta_pct": 9.11, "reason": "Battery cell tariff surcharge", "direction": "up"},
            {"sku": "SKU-7734", "name": "Merino Wool Thermal Performance Jacket", "category": "Apparel", "prev_price": 185.00, "curr_price": 165.00, "delta_pct": -10.81, "reason": "End-of-season inventory clearance", "direction": "down"},
            {"sku": "SKU-6120", "name": "Multi-Cooker Smart Pressure Pot 8L", "category": "Home & Kitchen", "prev_price": 119.95, "curr_price": 104.50, "delta_pct": -12.88, "reason": "Volume manufacturer rebate", "direction": "down"},
            {"sku": "SKU-5049", "name": "OLED 4K 144Hz Gaming Monitor 32-inch", "category": "Electronics", "prev_price": 799.99, "curr_price": 849.99, "delta_pct": 6.25, "reason": "Display panel substrate supply pinch", "direction": "up"}
        ]
        summary = {"global_retail_cpi": 3.8, "max_category_inflation": 7.4, "avg_retailer_dispersion": 14.8, "purchasing_power_impact": -3.2}

    big_mac_basket = [
        {"country": "United States", "code": "US", "basket_usd": 5.69, "implied_ppp": "Base", "valuation": "0.0%", "conversion_rate": "3.42%"},
        {"country": "Eurozone", "code": "EU", "basket_usd": 5.82, "implied_ppp": "+2.3%", "valuation": "+2.3% (Over)", "conversion_rate": "3.18%"},
        {"country": "United Kingdom", "code": "UK", "basket_usd": 5.48, "implied_ppp": "-3.7%", "valuation": "-3.7% (Under)", "conversion_rate": "3.35%"},
        {"country": "Brazil", "code": "BR", "basket_usd": 4.35, "implied_ppp": "-23.6%", "valuation": "-23.6% (Under)", "conversion_rate": "2.85%"},
        {"country": "India", "code": "IN", "basket_usd": 2.55, "implied_ppp": "-55.2%", "valuation": "-55.2% (Under)", "conversion_rate": "2.41%"},
        {"country": "Japan", "code": "JP", "basket_usd": 3.15, "implied_ppp": "-44.6%", "valuation": "-44.6% (Under)", "conversion_rate": "3.64%"},
        {"country": "China", "code": "CN", "basket_usd": 3.52, "implied_ppp": "-38.1%", "valuation": "-38.1% (Under)", "conversion_rate": "3.20%"}
    ]

    return {
        "year": y,
        "markets": markets,
        "retailer_spread": retailer_spread,
        "price_movers": price_movers,
        "big_mac_basket": big_mac_basket,
        "summary": summary
    }


def get_cii_risk_data(year="all"):
    """Returns Country Instability Index (CII v14) scores, trade policy matrix, and FX volatility parameterized by year."""
    y = str(year)

    if y == "2016":
        cii_scores = [
            {"code": "BR", "country": "Brazil", "score": 52.4, "level": "elevated", "badge": "Elevated Volatility", "delta_24h": "+0.8", "sourcing_pct": 28.5, "primary_risk": "Political impeachment transition, fiscal austerity reform, USD/BRL 3.48", "stability_trajectory": "Transition"},
            {"code": "CN", "country": "China", "score": 36.8, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "+0.2", "sourcing_pct": 38.2, "primary_risk": "Industrial overcapacity reduction, RMB devaluation management", "stability_trajectory": "Stable"},
            {"code": "US", "country": "United States", "score": 21.2, "level": "low", "badge": "Low Risk", "delta_24h": "-0.1", "sourcing_pct": 14.2, "primary_risk": "US presidential election cycle; stable consumer spending", "stability_trajectory": "Stable"},
            {"code": "DE", "country": "Germany", "score": 22.4, "level": "low", "badge": "Low Risk", "delta_24h": "0.0", "sourcing_pct": 6.8, "primary_risk": "Eurozone banking stress tests, export capital goods demand", "stability_trajectory": "Stable"},
            {"code": "VN", "country": "Vietnam", "score": 32.1, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "-0.2", "sourcing_pct": 5.4, "primary_risk": "Early FDI manufacturing cluster expansion in Hai Phong", "stability_trajectory": "Improving"},
            {"code": "IN", "country": "India", "score": 42.5, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "+1.1", "sourcing_pct": 4.2, "primary_risk": "November 2016 currency demonetization cash friction", "stability_trajectory": "Short-Term Shock"},
            {"code": "TW", "country": "Taiwan", "score": 44.0, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "+0.3", "sourcing_pct": 4.1, "primary_risk": "Cross-strait dialogue suspension following election", "stability_trajectory": "Watch"},
            {"code": "TR", "country": "Turkey", "score": 68.4, "level": "high", "badge": "High Risk", "delta_24h": "+2.4", "sourcing_pct": 2.1, "primary_risk": "July 2016 state of emergency, Lira currency pressure", "stability_trajectory": "High Stress"}
        ]
        trade_policies = [
            {"policy": "Mercosur Free Trade Convergence", "jurisdiction": "South America", "impacted_categories": "Automotive, Industrial Hardware, Plastics", "tariff_rate": "0% Intra-bloc", "status": "Active", "action_needed": "Leverage zero-duty Argentine and Brazilian bilateral quotas"},
            {"policy": "Trans-Pacific Partnership (TPP)", "jurisdiction": "Pacific Basin (12 Nations)", "impacted_categories": "Textiles, Electronics, Footwear", "tariff_rate": "Proposed Tariff Elimination", "status": "Pending Ratification", "action_needed": "Pre-qualify Tier-2 suppliers in Vietnam and Malaysia"},
            {"policy": "Brazil Siscomex Modernization", "jurisdiction": "Brazil", "impacted_categories": "Imported Raw Components", "tariff_rate": "Unified Import Declaration", "status": "Enacted Pilot", "action_needed": "Transition customs clearance to digital single window"}
        ]
        fx_volatility = [
            {"pair": "USD / BRL", "rate": 3.48, "volatility_30d": "18.5%", "direction": "-4.2% (BRL Recovery)", "margin_drag": "+1.5%", "hedge_recommendation": "Maintain 60% forward cover at 3.50 target"},
            {"pair": "EUR / USD", "rate": 1.095, "volatility_30d": "7.2%", "direction": "-1.1% (EUR Flat)", "margin_drag": "0.0%", "hedge_recommendation": "Standard spot transaction settlement"},
            {"pair": "USD / CNY", "rate": 6.64, "volatility_30d": "5.1%", "direction": "+2.2% (CNY Soft)", "margin_drag": "+0.8%", "hedge_recommendation": "Invoice in RMB to capture supplier price discounts"}
        ]
        summary = {"sourcing_risk_index": 32.8, "tracked_countries": 31, "active_trade_tariffs": 8, "currency_volatility_idx": 15.2}

    elif y == "2017":
        cii_scores = [
            {"code": "BR", "country": "Brazil", "score": 46.5, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "-0.4", "sourcing_pct": 24.2, "primary_risk": "Labor modernization reform enacted; GDP returning to positive growth", "stability_trajectory": "Stabilizing"},
            {"code": "CN", "country": "China", "score": 39.4, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "+0.1", "sourcing_pct": 40.5, "primary_risk": "Belt and Road supply chain financing, shadow banking deleveraging", "stability_trajectory": "Stable"},
            {"code": "US", "country": "United States", "score": 23.5, "level": "low", "badge": "Low Risk", "delta_24h": "+0.3", "sourcing_pct": 16.0, "primary_risk": "US withdrawal from TPP; NAFTA renegotiation formally launched", "stability_trajectory": "Trade Shift"},
            {"code": "DE", "country": "Germany", "score": 21.8, "level": "low", "badge": "Low Risk", "delta_24h": "-0.1", "sourcing_pct": 7.0, "primary_risk": "Federal election coalition negotiations, EU single market strength", "stability_trajectory": "Stable"},
            {"code": "VN", "country": "Vietnam", "score": 31.5, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "-0.3", "sourcing_pct": 6.8, "primary_risk": "Samsung smartphone export surge boosting trade balance", "stability_trajectory": "Strong Expansion"},
            {"code": "IN", "country": "India", "score": 36.2, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "-0.5", "sourcing_pct": 5.1, "primary_risk": "National Goods and Services Tax (GST) rollout unifying 29 states", "stability_trajectory": "Tax Integration"},
            {"code": "TW", "country": "Taiwan", "score": 45.8, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "+0.4", "sourcing_pct": 4.2, "primary_risk": "Semiconductor foundry capacity expansion, cross-strait freeze", "stability_trajectory": "Neutral"}
        ]
        trade_policies = [
            {"policy": "US Section 232 Steel/Aluminium Investigation", "jurisdiction": "USA", "impacted_categories": "Steel, Aluminium Inputs", "tariff_rate": "National Security Review", "status": "Investigation Phase", "action_needed": "Assess exposure of metal cookware and appliance chassis"},
            {"policy": "India Goods and Services Tax (GST)", "jurisdiction": "India", "impacted_categories": "Pan-India E-Commerce", "tariff_rate": "5% – 28% Harmonized", "status": "Enacted July 2017", "action_needed": "Integrate GSTIN invoice compliance on South Asian sourcing"},
            {"policy": "EU General Data Protection Regulation (GDPR)", "jurisdiction": "European Union", "impacted_categories": "Digital Storefronts & CRM", "tariff_rate": "Regulatory Compliance", "status": "Preparation Window", "action_needed": "Audit EU customer data handling pipelines ahead of 2018"}
        ]
        fx_volatility = [
            {"pair": "USD / BRL", "rate": 3.19, "volatility_30d": "12.4%", "direction": "-3.8% (BRL Strong)", "margin_drag": "+2.1%", "hedge_recommendation": "Lock in favorable USD import purchases"},
            {"pair": "EUR / USD", "rate": 1.185, "volatility_30d": "8.4%", "direction": "+11.2% (EUR Rally)", "margin_drag": "-1.4%", "hedge_recommendation": "Collar options on European luxury goods"},
            {"pair": "USD / CNY", "rate": 6.53, "volatility_30d": "4.8%", "direction": "-5.2% (CNY Appr.)", "margin_drag": "-0.9%", "hedge_recommendation": "Negotiate quarterly price locks with Shenzhen suppliers"}
        ]
        summary = {"sourcing_risk_index": 34.6, "tracked_countries": 31, "active_trade_tariffs": 12, "currency_volatility_idx": 11.5}

    elif y == "2018":
        cii_scores = [
            {"code": "CN", "country": "China", "score": 49.8, "level": "elevated", "badge": "Elevated Risk", "delta_24h": "+1.2", "sourcing_pct": 41.8, "primary_risk": "US Section 301 tariffs of 25% enacted on $250B Chinese goods; retaliatory agricultural quotas", "stability_trajectory": "Trade Friction"},
            {"code": "BR", "country": "Brazil", "score": 48.2, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "+0.9", "sourcing_pct": 21.5, "primary_risk": "May 2018 nationwide trucker strike, presidential election uncertainty, USD/BRL 3.85", "stability_trajectory": "Volatile"},
            {"code": "US", "country": "United States", "score": 26.2, "level": "low", "badge": "Low Risk", "delta_24h": "+0.4", "sourcing_pct": 17.5, "primary_risk": "USMCA renegotiation conclusion, Section 232 global steel tariffs enacted", "stability_trajectory": "Trade Reshuffle"},
            {"code": "DE", "country": "Germany", "score": 24.5, "level": "low", "badge": "Low Risk", "delta_24h": "+0.2", "sourcing_pct": 6.9, "primary_risk": "Auto emission testing bottlenecks (WLTP), trade dispute retaliation fears", "stability_trajectory": "Stable"},
            {"code": "VN", "country": "Vietnam", "score": 33.8, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "-0.4", "sourcing_pct": 8.2, "primary_risk": "Massive supply chain nearshoring influx from Guangdong manufacturers", "stability_trajectory": "Beneficiary"},
            {"code": "TR", "country": "Turkey", "score": 72.8, "level": "critical", "badge": "Critical Alert", "delta_24h": "+3.1", "sourcing_pct": 1.8, "primary_risk": "August 2018 Lira currency plunge (-40%), US diplomatic sanctions", "stability_trajectory": "Currency Crisis"}
        ]
        trade_policies = [
            {"policy": "US Section 301 China Tariffs (Lists 1, 2, 3)", "jurisdiction": "USA / China", "impacted_categories": "Electronics, Machinery, Auto Parts, Furniture", "tariff_rate": "10% – 25% Extra Duty", "status": "Enacted (Jul - Sep 2018)", "action_needed": "Reroute assembly to Vietnam/India contract manufacturers"},
            {"policy": "US Section 232 Global Steel/Alu Tariffs", "jurisdiction": "USA", "impacted_categories": "Raw Steel (25%), Aluminium (10%)", "tariff_rate": "25% ad valorem", "status": "Enacted March 2018", "action_needed": "Source domestic Brazilian steel fabricators"},
            {"policy": "USMCA (NAFTA Replacement)", "jurisdiction": "US / Mexico / Canada", "impacted_categories": "Automotive, Cross-Border E-Commerce", "tariff_rate": "De Minimis Raised ($117 CAD)", "status": "Signed Nov 2018", "action_needed": "Prepare Mexican nearshoring fulfillment nodes"}
        ]
        fx_volatility = [
            {"pair": "USD / BRL", "rate": 3.85, "volatility_30d": "16.8%", "direction": "+18.2% (BRL Depr.)", "margin_drag": "-3.8%", "hedge_recommendation": "75% currency forward hedge to protect imported margins"},
            {"pair": "EUR / USD", "rate": 1.145, "volatility_30d": "7.9%", "direction": "-4.8% (EUR Soft)", "margin_drag": "+0.5%", "hedge_recommendation": "Quarterly collar options at 1.12 floor"},
            {"pair": "USD / CNY", "rate": 6.88, "volatility_30d": "6.2%", "direction": "+5.4% (CNY Weaker)", "margin_drag": "+1.8%", "hedge_recommendation": "Benefit from cheaper Chinese FOB procurement prices"}
        ]
        summary = {"sourcing_risk_index": 39.2, "tracked_countries": 31, "active_trade_tariffs": 26, "currency_volatility_idx": 14.8}

    else: # "all" - Contemporary World Monitor benchmark
        cii_scores = [
            {"code": "CN", "country": "China", "score": 48.5, "level": "elevated", "badge": "Elevated Risk", "delta_24h": "+0.4", "sourcing_pct": 42.6, "primary_risk": "US export controls, semiconductor sanctions, retaliatory rare-earth quotas", "stability_trajectory": "Fragile Neutral"},
            {"code": "US", "country": "United States", "score": 24.2, "level": "low", "badge": "Low Risk", "delta_24h": "-0.2", "sourcing_pct": 18.4, "primary_risk": "Port labor collective bargaining renewals, tariff policy shifts", "stability_trajectory": "Stable"},
            {"code": "DE", "country": "Germany", "score": 26.8, "level": "low", "badge": "Low Risk", "delta_24h": "+0.1", "sourcing_pct": 7.2, "primary_risk": "Industrial energy tariff costs, CBAM carbon border compliance", "stability_trajectory": "Stable"},
            {"code": "BR", "country": "Brazil", "score": 44.2, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "+0.6", "sourcing_pct": 12.8, "primary_risk": "Fiscal deficit expansion, currency FX swing (USD/BRL), customs ICMS reform", "stability_trajectory": "Volatile"},
            {"code": "VN", "country": "Vietnam", "score": 34.6, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "+0.3", "sourcing_pct": 9.4, "primary_risk": "Grid power brownouts in Bac Ninh tech clusters, transshipment origin audits", "stability_trajectory": "Stable Improving"},
            {"code": "IN", "country": "India", "score": 38.1, "level": "moderate", "badge": "Moderate Risk", "delta_24h": "-0.1", "sourcing_pct": 6.8, "primary_risk": "Non-tariff electronic certification hurdles, logistics intermodal dwell", "stability_trajectory": "Improving"},
            {"code": "TW", "country": "Taiwan", "score": 52.4, "level": "elevated", "badge": "Elevated Risk", "delta_24h": "+0.8", "sourcing_pct": 4.5, "primary_risk": "PLA naval blockade exercises, commercial air corridor NOTAM diversions", "stability_trajectory": "High Alert"},
            {"code": "EG", "country": "Egypt", "score": 71.5, "level": "critical", "badge": "Critical Alert", "delta_24h": "+1.8", "sourcing_pct": 0.8, "primary_risk": "Suez Canal transit revenue collapse (-58%), sovereign debt refinancing pressure", "stability_trajectory": "Acute Stress"}
        ]
        trade_policies = [
            {"policy": "US Section 301 China Tariffs", "jurisdiction": "USA / China", "impacted_categories": "Electronics, Power Tools, Solar Cells, Lithium Batteries", "tariff_rate": "25% – 50%", "status": "Enacted / Broadened", "action_needed": "Accelerate Vietnam / India assembly relocation"},
            {"policy": "EU Carbon Border Adjustment (CBAM)", "jurisdiction": "European Union", "impacted_categories": "Steel, Aluminium, Fertilizers, Polymers", "tariff_rate": "Carbon price parity (€68/ton)", "status": "Definitive Phase", "action_needed": "Audit Tier-2 supplier Scope 1/2 carbon certificates"},
            {"policy": "US De Minimis Reform (Section 321)", "jurisdiction": "USA", "impacted_categories": "Cross-Border DTC Parcels (<$800)", "tariff_rate": "Full duty + formal customs entry", "status": "Proposed / Enforcement Pilot", "action_needed": "Shift from direct postal drops to bonded US fulfillment"},
            {"policy": "Brazil ICMS Remessa Conforme", "jurisdiction": "Brazil", "impacted_categories": "Cross-Border Consumer Imports (<$50)", "tariff_rate": "20% federal + 17% ICMS state tax", "status": "Enacted", "action_needed": "In-country merchant checkout tax pre-collection (DDP)"}
        ]
        fx_volatility = [
            {"pair": "USD / BRL", "rate": 5.74, "volatility_30d": "14.2%", "direction": "+1.8% (BRL Depr.)", "margin_drag": "-2.8%", "hedge_recommendation": "75% Forward Hedge at 5.70 floor"},
            {"pair": "EUR / USD", "rate": 1.082, "volatility_30d": "6.8%", "direction": "-0.6% (EUR Weak)", "margin_drag": "+0.4%", "hedge_recommendation": "50% Collar Options (1.06 - 1.10)"},
            {"pair": "USD / CNY", "rate": 7.24, "volatility_30d": "4.5%", "direction": "+0.9% (CNY Soft)", "margin_drag": "+1.2%", "hedge_recommendation": "Natural supplier balance in CNH"}
        ]
        summary = {"sourcing_risk_index": 38.4, "tracked_countries": 31, "active_trade_tariffs": 22, "currency_volatility_idx": 11.8}

    return {
        "year": y,
        "cii_scores": cii_scores,
        "trade_policies": trade_policies,
        "fx_volatility": fx_volatility,
        "summary": summary
    }


def get_infrastructure_data(year="all"):
    """Returns digital infrastructure, cloud regions, subsea cables, and logistics incidents parameterized by year."""
    y = str(year)

    if y == "2016":
        cloud_regions = [
            {"region": "us-east-1 (N. Virginia)", "provider": "AWS", "service": "Checkout & Order State API", "uptime": "99.965%", "latency_ms": 48, "status": "operational", "load": "42%"},
            {"region": "sa-east-1 (São Paulo)", "provider": "AWS", "service": "Core Brazilian Database Instance", "uptime": "99.940%", "latency_ms": 72, "status": "operational", "load": "38%"},
            {"region": "Boleto Settlement Core", "provider": "FEBRABAN / Caixa", "service": "Cash Voucher Banking Clearance", "uptime": "99.820%", "latency_ms": 480, "status": "elevated", "load": "84%"},
            {"region": "Cielo Credit Card Rails", "provider": "Cielo", "service": "Installment Authorization Gateway", "uptime": "99.910%", "latency_ms": 320, "status": "operational", "load": "55%"}
        ]
        subsea_cables = [
            {"id": "americas_2", "name": "Americas-II", "route": "US (Florida) ⇄ Brazil (Fortaleza)", "capacity": "2.5 Tbps", "status": "nominal", "status_text": "Nominal", "rtt_ms": 118},
            {"id": "atlantis_2", "name": "Atlantis-2", "route": "South America ⇄ Europe (Portugal)", "capacity": "1.2 Tbps", "status": "nominal", "status_text": "Nominal", "rtt_ms": 142}
        ]
        logistics_incidents = [
            {"id": "INC-2016-01", "title": "São Paulo Correios Postal Strike Notice", "location": "São Paulo (SP), Brazil", "category": "Labor Dispute", "severity": "medium", "badge": "Moderate Impact", "time": "Oct 2016", "impact": "Postal union 48-hour stoppage slowing metropolitan deliveries.", "mitigation": "Switch priority consignments to regional private motor-courier pilots."},
            {"id": "INC-2016-02", "title": "Boleto Bancário Banking Holiday Backlog", "location": "National Banking Rails, Brazil", "category": "Payment Processing", "severity": "low", "badge": "Low Impact", "time": "Nov 2016", "impact": "3-day holiday weekend delayed settlement of 120 customer order confirmations.", "mitigation": "Hold inventory reservations for 72h before automated order release."}
        ]
        latency_trend = {
            "regions": ["North America", "Europe", "Latin America", "Asia-Pacific", "Middle East", "Africa"],
            "api_checkout": [140, 165, 240, 280, 310, 390],
            "subsea_rtt": [85, 110, 160, 180, 220, 290],
            "inventory_sync": [180, 210, 310, 350, 390, 480]
        }
        summary = {"checkout_sla": 99.942, "subsea_health_pct": 99.0, "active_incidents": 2, "avg_payment_latency": 320}

    elif y == "2017":
        cloud_regions = [
            {"region": "us-east-1 (N. Virginia)", "provider": "AWS", "service": "Checkout & Order State API", "uptime": "99.982%", "latency_ms": 36, "status": "operational", "load": "56%"},
            {"region": "eu-central-1 (Frankfurt)", "provider": "AWS", "service": "European Supplier Sync", "uptime": "99.980%", "latency_ms": 42, "status": "operational", "load": "45%"},
            {"region": "sa-east-1 (São Paulo)", "provider": "AWS", "service": "Primary Microservices Cluster", "uptime": "99.975%", "latency_ms": 54, "status": "operational", "load": "68%"},
            {"region": "MercadoPago Gateway", "provider": "MercadoLibre", "service": "1-Click Installment Processing", "uptime": "99.960%", "latency_ms": 195, "status": "operational", "load": "64%"}
        ]
        subsea_cables = [
            {"id": "americas_2", "name": "Americas-II", "route": "US (Florida) ⇄ Brazil (Fortaleza)", "capacity": "5.0 Tbps", "status": "nominal", "status_text": "Nominal", "rtt_ms": 112},
            {"id": "seabras_1", "name": "Seabras-1 (Seaborn)", "route": "US (NJ) ⇄ Brazil (Praia Grande)", "capacity": "72 Tbps", "status": "nominal", "status_text": "Inaugurated (Sep 2017)", "rtt_ms": 104}
        ]
        logistics_incidents = [
            {"id": "INC-2017-01", "title": "Black Friday Server Connection Pool Exhaustion", "location": "São Paulo Data Center", "category": "Cloud Infrastructure", "severity": "medium", "badge": "Resolved", "time": "Nov 2017", "impact": "Peak surge of 7,500 concurrent sessions spiked database latency to 420ms for 14 minutes.", "mitigation": "Deployed PgBouncer connection pooling and Read Replicas across 3 Availability Zones."},
            {"id": "INC-2017-02", "title": "Rio-Santos Highway Mudslide Transit Delay", "location": "BR-101 Highway, Southeast Brazil", "category": "Severe Weather", "severity": "medium", "badge": "Moderate Impact", "time": "Dec 2017", "impact": "Heavy summer rains blocked coastal freight corridor for 36 hours; 480 parcels delayed.", "mitigation": "Rerouted logistics trucks through inland Dutra highway (BR-116)."}
        ]
        latency_trend = {
            "regions": ["North America", "Europe", "Latin America", "Asia-Pacific", "Middle East", "Africa"],
            "api_checkout": [110, 125, 185, 195, 240, 290],
            "subsea_rtt": [65, 85, 130, 140, 180, 225],
            "inventory_sync": [140, 160, 230, 245, 295, 360]
        }
        summary = {"checkout_sla": 99.975, "subsea_health_pct": 98.4, "active_incidents": 2, "avg_payment_latency": 210}

    elif y == "2018":
        cloud_regions = [
            {"region": "us-east-1 (N. Virginia)", "provider": "AWS", "service": "Checkout & Order State API", "uptime": "99.990%", "latency_ms": 30, "status": "operational", "load": "62%"},
            {"region": "eu-central-1 (Frankfurt)", "provider": "AWS", "service": "European Inventory Sync", "uptime": "99.988%", "latency_ms": 35, "status": "operational", "load": "52%"},
            {"region": "southamerica-east1", "provider": "GCP", "service": "BigQuery & Analytics Ingestion", "uptime": "99.985%", "latency_ms": 44, "status": "operational", "load": "58%"},
            {"region": "sa-east-1 (São Paulo)", "provider": "AWS", "service": "E-Commerce Core & Churn ML API", "uptime": "99.982%", "latency_ms": 48, "status": "operational", "load": "74%"},
            {"region": "Adyen Brazil Hub", "provider": "Adyen", "service": "Credit Card Tokenization & Fraud Engine", "uptime": "99.980%", "latency_ms": 145, "status": "operational", "load": "66%"}
        ]
        subsea_cables = [
            {"id": "monet", "name": "Monet (Google/Algar)", "route": "US (Florida) ⇄ Brazil (Santos)", "capacity": "64 Tbps", "status": "nominal", "status_text": "Operational (May 2018)", "rtt_ms": 98},
            {"id": "sacs", "name": "SACS (Angola Cables)", "route": "Brazil (Fortaleza) ⇄ Angola (Luanda)", "capacity": "40 Tbps", "status": "nominal", "status_text": "Operational (Sep 2018)", "rtt_ms": 63},
            {"id": "seabras_1", "name": "Seabras-1", "route": "US (NJ) ⇄ Brazil (Praia Grande)", "capacity": "72 Tbps", "status": "nominal", "status_text": "Nominal", "rtt_ms": 102}
        ]
        logistics_incidents = [
            {"id": "INC-2018-01", "title": "Nationwide Brazilian Trucker Strike (Greve dos Caminhoneiros)", "location": "Pan-Brazil Highway Network", "category": "Severe National Disruption", "severity": "critical", "badge": "Critical Alert", "time": "May 2018", "impact": "11-day diesel fuel protest blocked highway distribution nationwide. R$ 1.8M in e-commerce orders held at carrier sorting centers.", "mitigation": "Declared customer delivery amnesty; negotiated priority air freight via LATAM Cargo for perishable orders."},
            {"id": "INC-2018-02", "title": "Boleto DDA Registration Mandatory Compliance", "location": "Central Bank of Brazil (BACEN)", "category": "Regulatory Banking", "severity": "medium", "badge": "Completed", "time": "Oct 2018", "impact": "Mandatory central registration of all payment slips eliminated fake boletos but required real-time API verification.", "mitigation": "Integrated direct CIP (Câmara Interbancária de Pagamentos) real-time webhook validation."}
        ]
        latency_trend = {
            "regions": ["North America", "Europe", "Latin America", "Asia-Pacific", "Middle East", "Africa"],
            "api_checkout": [92, 108, 162, 155, 195, 235],
            "subsea_rtt": [55, 72, 115, 102, 155, 195],
            "inventory_sync": [120, 138, 205, 185, 240, 285]
        }
        summary = {"checkout_sla": 99.982, "subsea_health_pct": 97.8, "active_incidents": 2, "avg_payment_latency": 165}

    else: # "all" - Contemporary World Monitor benchmark
        cloud_regions = [
            {"region": "us-east-1 (N. Virginia)", "provider": "AWS", "service": "Checkout & Order State API", "uptime": "99.992%", "latency_ms": 28, "status": "operational", "load": "64%"},
            {"region": "eu-central-1 (Frankfurt)", "provider": "AWS", "service": "European Inventory Sync", "uptime": "99.988%", "latency_ms": 34, "status": "operational", "load": "58%"},
            {"region": "sa-east-1 (São Paulo)", "provider": "GCP", "service": "MercadoLivre & Brazilian Webhook Hub", "uptime": "99.965%", "latency_ms": 46, "status": "operational", "load": "72%"},
            {"region": "ap-southeast-1 (Singapore)", "provider": "AWS", "service": "Asia-Pac Sourcing Gateway", "uptime": "99.995%", "latency_ms": 32, "status": "operational", "load": "51%"},
            {"region": "Global Edge CDN", "provider": "Cloudflare", "service": "Storefront Asset Caching & WAF", "uptime": "99.999%", "latency_ms": 12, "status": "operational", "load": "42%"},
            {"region": "Stripe Global API", "provider": "Stripe", "service": "Multi-Currency Card Processing", "uptime": "99.984%", "latency_ms": 115, "status": "operational", "load": "68%"},
            {"region": "PIX Settlement Core", "provider": "Banco Central do Brasil", "service": "Instant Brazilian Bank Rails", "uptime": "99.991%", "latency_ms": 88, "status": "operational", "load": "79%"},
            {"region": "Adyen European Hub", "provider": "Adyen", "service": "iDEAL, Klarna & Cartes Bancaires", "uptime": "99.979%", "latency_ms": 124, "status": "operational", "load": "63%"}
        ]
        subsea_cables = [
            {"id": "aeconnect_1", "name": "AEConnect-1", "route": "US (Shirley) ⇄ Ireland (Killala)", "capacity": "130 Tbps", "status": "nominal", "status_text": "Nominal", "rtt_ms": 54},
            {"id": "dunant", "name": "Dunant (Google)", "route": "US (Virginia Beach) ⇄ France (Saint-Hilaire)", "capacity": "250 Tbps", "status": "nominal", "status_text": "Nominal", "rtt_ms": 52},
            {"id": "seamewe_5", "name": "SEA-ME-WE 5", "route": "France ⇄ Egypt ⇄ Singapore", "capacity": "24 Tbps", "status": "elevated", "status_text": "Rerouted / Red Sea Repair", "rtt_ms": 168},
            {"id": "aae_1", "name": "Asia-Africa-Europe 1", "route": "Hong Kong ⇄ Vietnam ⇄ Egypt ⇄ France", "capacity": "40 Tbps", "status": "elevated", "status_text": "Degraded / Anchor Drag", "rtt_ms": 182},
            {"id": "faster", "name": "FASTER", "route": "US (Oregon) ⇄ Japan (Chiba)", "capacity": "60 Tbps", "status": "nominal", "status_text": "Nominal", "rtt_ms": 88},
            {"id": "2africa", "name": "2Africa", "route": "UK ⇄ Mediterranean ⇄ South Africa ⇄ Gulf", "capacity": "180 Tbps", "status": "nominal", "status_text": "Nominal", "rtt_ms": 112}
        ]
        logistics_incidents = [
            {"id": "INC-8831", "title": "Hamburg Port Dockworkers Tariff Action", "location": "Port of Hamburg, Germany", "category": "Labor Dispute", "severity": "high", "badge": "High Impact", "time": "3 hours ago", "impact": "24-hour warning strike halting Waltershof & Burchardkai container gantry cranes. 18 container feeder vessels delayed.", "mitigation": "Divert incoming ocean containers to Rotterdam or Antwerp-Bruges terminals."},
            {"id": "INC-8828", "title": "Panama Canal Gatun Lake Draft Advisory", "location": "Panama Canal Authority", "category": "Waterways & Climate", "severity": "medium", "badge": "Moderate Impact", "time": "7 hours ago", "impact": "Maximum vessel draft capped at 44.0 feet for Neopanamax locks due to seasonal dry weather replenishment limits.", "mitigation": "Reduce per-vessel container weight loading by 12% or route via US West Coast intermodal."},
            {"id": "INC-8824", "title": "Santos Port Custom Broker Union Slowdown", "location": "Santos Port, São Paulo, Brazil", "category": "Customs & Regulatory", "severity": "medium", "badge": "Moderate Impact", "time": "14 hours ago", "impact": "Receita Federal auditor work-to-rule action causing import clearance backlog from 48h normal to 120h average.", "mitigation": "Pre-file green-channel import declarations (Declaração Única de Importação - DU-E)."},
            {"id": "INC-8819", "title": "Taipei Taoyuan Air Cargo Typhoon Reroute", "location": "Taiwan Taoyuan Int'l Airport (TPE)", "category": "Severe Weather", "severity": "high", "badge": "High Impact", "time": "19 hours ago", "impact": "Pacific Typhoon Gaemi outer bands ground 42 dedicated freighter flights; semiconductor air cargo backlogged.", "mitigation": "Hold priority electronic component batches at Incheon (ICN) and Tokyo Narita (NRT) hubs."},
            {"id": "INC-8812", "title": "Red Sea Merchant Fleet Naval Convoy Mandate", "location": "Bab el-Mandeb / Gulf of Aden", "category": "Maritime Security", "severity": "critical", "badge": "Critical Alert", "time": "1 day ago", "impact": "Operation Aspides requires escort registration 72h prior to transit. Unescorted container carriers routing via Cape.", "mitigation": "Buffer 14 additional sailing days in global customer inventory stock-out models."}
        ]
        latency_trend = {
            "regions": ["North America", "Europe", "Latin America", "Asia-Pacific", "Middle East", "Africa"],
            "api_checkout": [84, 98, 156, 142, 178, 210],
            "subsea_rtt": [52, 64, 118, 92, 146, 184],
            "inventory_sync": [112, 126, 198, 168, 224, 255]
        }
        summary = {"checkout_sla": 99.984, "subsea_health_pct": 96.2, "active_incidents": 5, "avg_payment_latency": 138}

    return {
        "year": y,
        "cloud_regions": cloud_regions,
        "subsea_cables": subsea_cables,
        "logistics_incidents": logistics_incidents,
        "latency_trend": latency_trend,
        "summary": summary
    }
