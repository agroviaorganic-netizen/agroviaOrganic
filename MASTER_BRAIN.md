# 🌾 AGROVIA ORGANIC — Master Brain & System Continuity Document
> **Version:** 2.0 (Phase 2 Upgrade Completed)  
> **Last Updated:** September 2026  
> **Purpose:** Paste this entire document into any new AI chat or new PC to instantly restore 100% context, operational memory, technical specifications, and strategic roadmaps.

---

## 📌 QUICK PROMPT TO RESUME WORK IN A NEW CHAT
```text
You are the Lead Technical Architect & Global Trade Strategist for AGROVIA ORGANIC. 
Read and adopt the Master Brain specifications below. 
You must maintain our exact brand architecture, design rules (White Background + Emerald Green + Gold Luxury), 
static HTML build engine, and deployment infrastructure without resetting or breaking existing features.
[PASTE THIS DOCUMENT BELOW]
```

---

## 🌍 PART 1: CORPORATE IDENTITY & BRAND ARCHITECTURE

### 1. Company Overview
* **Company Name:** AGROVIA ORGANIC
* **Founder & Managing Director:** Pranto Sarker
* **Headquarters:** Gulshan Commercial Area, Dhaka, Bangladesh 🇧🇩
* **Official Export Email:** `export@agroviaorganic.com`
* **Nature of Business:** Agricultural Commodity & Specialty Food Export Agency
* **Target Export Markets:** United Kingdom 🇬🇧, United States 🇺🇸, United Arab Emirates 🇦🇪, Saudi Arabia 🇸🇦, European Union 🇪🇺, Canada 🇨🇦, Malaysia 🇲🇾, Singapore 🇸🇬
* **Vision:** Positioning Bangladesh as a globally trusted benchmark for premium, single-origin, certified, and 100% traceable agricultural delicacies.
* **Value Proposition:** Direct ethical sourcing from traditional farming communities (Sundarbans honey hunters, Dinajpur GI rice cultivators, char peanut growers) combined with Tier-1 international food safety compliance (ISO 22000, HACCP, SGS, Halal, EU Food Safety).

---

### 2. The 5 Core Commodity Monographs & Lab Standards

| # | Commodity | Geographic Origin | Mandatory Lab & Quality Standards | Primary Packaging |
|---|---|---|---|---|
| **1** | **Sundarbans Wild Raw Mangrove Honey** | UNESCO Sundarbans Mangrove Forest (Khulna / Satkhira) | • C4 Sugar (EA-IRMS): **0.000% (Zero Adulteration)**<br>• Moisture: **≤ 18.5%** (Codex Standard)<br>• HMF: **< 40 mg/kg** (EU 2001/110/EC)<br>• Antibiotics/Chloramphenicol: **Non-detectable** | 250g, 500g, 1kg amber glass jars; 25kg / 200L food-grade drums |
| **2** | **Chinigura & GI Tulshimala Aromatic Rice** | Dinajpur & Sherpur Districts | • Broken Grain: **< 3% (Grade A Premium)**<br>• Moisture: **≤ 12.5%**<br>• Foreign Matter: **< 0.1%**<br>• Treatment: **100% Phostoxin Gas Fumigated**<br>• Sorting: **Sortex Optical Cleaned** | 1kg, 2kg, 5kg vacuum-sealed foil barrier pouches; 25kg/50kg laminated PP bags |
| **3** | **Pesticide-Free Traditional Dried Fish (Shukti)** | Bay of Bengal Coastal Belt (Cox's Bazar) | • Pesticide Residue (GC-MS): **0% (DDT/Malathion Free)**<br>• Histamine Level: **< 200 ppm** (EC 854/2004)<br>• Moisture: **≤ 25%**<br>• Salmonella: **Absent per 25g sample** | Food-grade nitrogen-flushed vacuum pouches (500g, 1kg, 5kg) |
| **4** | **Northern Char Peanuts & Pure Peanut Butter** | Padma & Jamuna River Char Basins | • Total Aflatoxin (HPLC): **< 4 ppb** (EU Regulation 1881/2006 compliance)<br>• Moisture: **≤ 8%**<br>• Peanut Butter: **100% pure roasted peanuts (No palm oil, no added sugar)** | 25kg PP export bags (raw kernels); 500g / 1kg glass jars (peanut butter) |
| **5** | **Himsagar Mango (GI) & Fresh Jackfruit** | Rajshahi Division (Mango) & Central Belt (Jackfruit) | • Sugar Brix Level: **19–22° Brix**<br>• Quarantine Protocol: **Hot Water Treatment (HWT: 47°C for 75 min)**<br>• Transport: **Air Cargo Only (DAC) with 2–4°C cold chain** | 4kg / 5kg ventilated export corrugated cartons with foam netting |

---

## 🎨 PART 2: UI/UX DESIGN PHILOSOPHY & SYSTEM TOKENS

> [!IMPORTANT]
> **STRICT USER DESIGN DIRECTIVE:**
> - **Background:** Pure White (`#ffffff`) and soft ivory/mint tints (`#fbfdfa`, `#f7fdf9`). **NO DARK THEME.**
> - **Primary Accent:** Botanical Emerald Green (`#14532d` / `#0f3d21`).
> - **Secondary Luxury Accent:** Radiant Royal Gold (`#d49a26` / `#b47b18`).
> - **Typography:** `Playfair Display` (Luxury Serif for headlines) + `Outfit` / `Plus Jakarta Sans` (Clean geometric modern sans-serif for UI/body).
> - **Vibe:** Ultra-clean, organic, luxurious, trustworthy, and institutional.

### Key CSS Utilities (in `site_templates.py`)
* `.gold-shimmer-text`: Keyframe-animated gold gradient text.
* `.glass-card-luxury`: White translucent card with subtle green-gold border and organic shadow.
* `.card-hover-organic`: Smooth `-8px` vertical translation with golden glow shadow.
* `.btn-gold-shimmer`: Shimmering gradient gold CTA button.
* `.btn-sample`: Distinctive light-green/emerald sample request button.
* `.reveal`, `.reveal-left`, `.reveal-right`: IntersectionObserver-driven scroll reveal animations.
* `#heroCanvas`: Interactive HTML5 canvas rendering floating green leaves and golden pollen dewdrops.

---

## 🌐 PART 3: SITE ARCHITECTURE & LIVE PAGES

| File Name | Page Title | Core Features & Interactive Elements |
|---|---|---|
| [`index.html`](file:///c:/Users/Ptech/Documents/Babu/AGY/Agrovia_Organic/index.html) | Home | • **Sticky Smart Quote Bar** (MOQ 500kg, 8 countries, Free Sample button)<br>• **Canvas Breeze Hero** with animated leaves & gold particles<br>• **6-Badge Trust Strip** (ISO, HACCP, SGS, Halal, EU, EPB)<br>• **8-Country Flag Strip** (UK, USA, UAE, KSA, EU, CA, MY, SG)<br>• **5 Commodity Cards** with direct "Request Free Sample" buttons<br>• **Interactive Bangladesh Origin Map (SVG)** with clickable region inspection (Sundarbans, Dinajpur, Cox's Bazar, Char Basins, Rajshahi)<br>• **Agrovia vs Generic Suppliers** comparison matrix<br>• **B2B Buyer Testimonials** (UK, UAE, Netherlands)<br>• **Founder & Origin Story** (Pranto Sarker profile)<br>• **PDF Catalogue Download Banner** |
| [`products.html`](file:///c:/Users/Ptech/Documents/Babu/AGY/Agrovia_Organic/products.html) | Commodities & Specs | • Quick-jump anchor navigation bar<br>• 5 deep technical monographs with lab parameters and packaging tables<br>• Seasonal harvest availability badges<br>• "Request B2B Quote" & "Request Free Sample" CTAs on every product |
| [`compliance.html`](file:///c:/Users/Ptech/Documents/Babu/AGY/Agrovia_Organic/compliance.html) | Lab Standards & QA | • 4-Stage Quality Gate visual flow (Farm Audit → Lab Test → SGS Inspection → Export Docs)<br>• **Certificate Lightbox Gallery** (Interactive modal popup for ISO 22000, HACCP, SGS, Halal, EU 1881/2006, EPB/ERC)<br>• Comprehensive Lab Testing Matrix (EA-IRMS, HPLC, GC-MS, ELISA thresholds) |
| [`trade-logistics.html`](file:///c:/Users/Ptech/Documents/Babu/AGY/Agrovia_Organic/trade-logistics.html) | Incoterms & Logistics | • Port Gateways: Chittagong Sea Port (CGB) & Dhaka Airport (DAC) with transit times<br>• Incoterms 2020 breakdown (FOB, CFR, CIF)<br>• Banking & Trade Finance terms (Sight LC UCP 600, CAD, TT)<br>• **12-Month Seasonal Availability Calendar** for procurement planning |
| [`rfq.html`](file:///c:/Users/Ptech/Documents/Babu/AGY/Agrovia_Organic/rfq.html) | RFQ & Samples | • **Dual-Tab Interface:** "B2B Quote Request" vs "Free Sample Request"<br>• URL parameter support (`?product=honey&sample=1`) to auto-fill inputs<br>• Trade Desk contact cards, minimum order quantities (MOQs), and country picker |

---

## ⚙️ PART 4: REPOSITORY & DEPLOYMENT INFRASTRUCTURE

### 1. Remote Locations
* **Live Production URL:** [https://agrovia-organic.vercel.app](https://agrovia-organic.vercel.app)
* **GitHub Repository:** [agroviaorganic-netizen/agroviaOrganic](https://github.com/agroviaorganic-netizen/agroviaOrganic)
  *(CRITICAL: Note camelCase `agroviaOrganic`, NOT `Agrovia_Organic`)*

### 2. Credentials & Environment Reference
* **GitHub PAT:** `github_pat_11CMKIACA0FhO1l173Rg7k_***` *(Stored securely in deployment scripts / workspace)*
* **GitHub User:** `agroviaorganic-netizen`
* **Vercel Token:** `vcp_5IVPiiKB6SahuT8BhJXJUmAes***` *(Stored securely in deployment scripts / workspace)*
* **Vercel User:** `agroviaorganic-3842`
* **Vercel Team ID:** `team_SCTmAcusHZ8ufSlz7QC6Z9rx`
* **Vercel Project Name:** `agrovia-organic`

---

### 3. Critical Technical Environment Quirks (MUST READ)

1. **IPv4 Requirement on Windows (`WinError 10060`):**
   - Python's standard `urllib` and `requests` fail when connecting to GitHub or Vercel APIs due to IPv6 routing issues on this Windows workstation.
   - **MANDATORY RULE:** Always execute commands using `curl.exe -4` via subprocess or PowerShell.

2. **Windows Command-Line Limit (`WinError 206`):**
   - Passing large JSON or base64 HTML payloads in `--data` CLI arguments exceeds Windows character limits.
   - **MANDATORY RULE:** Always write payloads to a temporary JSON file (via `tempfile.NamedTemporaryFile`) and pass `--data-binary @temp.json` to `curl.exe`.

3. **Windows UTF-8 Console Encoding:**
   - Any Python script printing emoji or unicode must start with:
     ```python
     if sys.platform == 'win32':
         sys.stdout.reconfigure(encoding='utf-8', errors='replace')
         sys.stderr.reconfigure(encoding='utf-8', errors='replace')
     ```

4. **Code Generation Workflow:**
   - Modify `site_templates.py` or the generator scripts.
   - Run `python build_all.py` to regenerate all 5 static HTML files.
   - Run `python deploy_all.py` to push binaries to Vercel and commit updates to GitHub.

---

## 📁 PART 5: DIRECTORY STRUCTURE

```
c:\Users\Ptech\Documents\Babu\AGY\Agrovia_Organic\
├── AGROVIA_BRAND_BRAIN.md      # Initial knowledge base
├── MASTER_BRAIN.md             # THIS FILE — Master System & Continuity Prompt
├── README.md                   # Repository overview
├── commodities_data.json       # Structured commodity parameters
├── site_templates.py           # Shared HTML components (head, navbar, smart bar, footer, CSS)
├── build_all.py                # Master Python HTML builder
├── deploy_all.py               # Automated Vercel deploy & GitHub sync script
├── index.html                  # Homepage (generated)
├── products.html               # Products page (generated)
├── compliance.html             # Lab & Certifications page (generated)
├── trade-logistics.html        # Logistics & Incoterms page (generated)
└── rfq.html                    # RFQ & Sample Request page (generated)
```

---

## 📈 PART 6: BUSINESS STATUS & 30-DAY CLIENT ACQUISITION ROADMAP

### Current Situation:
- **Status:** The Digital Showroom is built, live, and verified.
- **Why No Orders Yet:** B2B agricultural export relies on active outbound lead generation. International buyers source through targeted outreach, cold pitch emails, B2B trade directories, and physical sample kits — not unprompted organic search on a newly published `.vercel.app` domain.

### Immediate Technical To-Do Items:
1. **Real WhatsApp Number:** Replace dummy `+880 1700-000000` with Pranto Sarker's real WhatsApp Business line.
2. **Real Form Submission Handler:** Integrate [Web3Forms](https://web3forms.com) or Formspree into `rfq.html` so incoming quotes instantly trigger an email/SMS notification to Pranto.
3. **Custom Domain:** Connect `agroviaorganic.com` on Vercel to establish maximum B2B credibility.

### High-Impact B2B Outreach Strategy:
1. **UK & EU Ethnic Supermarkets:** Pitch Procurement Managers at *TRS Foods, East End Foods, Bestway Wholesale, Surya Foods* with Tulshimala Rice & Sundarbans Honey.
2. **UAE Supermarket Chains:** Connect with Category Buyers at *Lulu Group, Al Maya, Choithrams* via WhatsApp & LinkedIn.
3. **Trade Portal Directory Listings:** Create free company profiles on *Go4WorldBusiness, TradeWheel, B2BMAP, ExportBangladesh*.
4. **Sample Kit Campaign:** Send 10 custom-packaged sample boxes (containing honey, rice, and peanuts with printed SGS lab reports) to vetted buyers in London and Dubai via DHL.

---

## 🛡️ DIRECTIVES FOR NEW AI AGENTS (OPERATIONAL RULES)

1. **NEVER switch to a dark background theme.** Always preserve the pristine white canvas with emerald green accents and gold luxury touches.
2. **NEVER wipe out existing features.** All additions (such as backend form hooks, new commodities, or analytics) must be additive.
3. **ALWAYS maintain the Python build engine.** Keep `site_templates.py` as the single source of truth for global layouts.
4. **ALWAYS use `deploy_all.py` for Vercel & GitHub updates** to ensure Windows networking compatibility (`curl.exe -4`).
5. **Always communicate with the founder (Pranto Sarker)** with professional, encouraging, and commercially actionable advice.
