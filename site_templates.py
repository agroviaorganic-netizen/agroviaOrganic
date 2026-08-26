"""
site_templates.py — Agrovia Organic shared template module.
Generates shared <head>, navbar (with sticky smart quote bar), footer, and global scripts.
Phase 2 Upgrade: Playfair Display + scroll-reveal + certificate lightbox CSS + origin map styles + testimonial styles.
"""

import json, os

def get_head(title, description):
    return f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | AGROVIA ORGANIC</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="Bangladesh agro export, Sundarbans honey, Chinigura rice, GI Tulshimala, dried fish shukti, char peanuts, Himsagar mango, organic agro exporter, ISO 22000, HACCP, Halal export">
    <meta name="author" content="Pranto Sarker, AGROVIA ORGANIC">
    
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://agrovia-organic.vercel.app/">
    <meta property="og:title" content="{title} | AGROVIA ORGANIC">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="https://images.unsplash.com/photo-1587049352846-4a222e784d38?q=80&w=1200&auto=format&fit=crop">
    <meta property="twitter:card" content="summary_large_image">

    <!-- Favicon (SVG Organic Emblem) -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%2314532d'/%3E%3Cpath d='M16 6c0 0-8 5-8 12a8 8 0 0 0 16 0C24 11 16 6 16 6z' fill='%23e6a838' opacity='0.9'/%3E%3Cpath d='M16 10c0 0-5 3.5-5 8a5 5 0 0 0 10 0C21 13.5 16 10 16 10z' fill='%23166534'/%3E%3C/svg%3E">
    
    <!-- Premium Google Fonts: Playfair Display (Luxury Serif) + Outfit + Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600;1,700&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            50: '#f2f9f3',
                            100: '#e3f3e6',
                            200: '#c5e6cb',
                            300: '#97d2a3',
                            400: '#62b775',
                            500: '#3c9b52',
                            600: '#2c7d3f',
                            700: '#14532d',  /* Deep Botanical Emerald */
                            800: '#0f3d21',  /* Forest Green */
                            900: '#072413',  /* Deep Onyx Emerald */
                            950: '#03140a',
                            gold: '#d49a26', /* Radiant Royal Gold */
                            'gold-light': '#fdf8ec',
                            'gold-dark': '#b47b18',
                            amber: '#c07d17',
                        }}
                    }},
                    fontFamily: {{
                        sans: ['"Outfit"', '"Plus Jakarta Sans"', 'sans-serif'],
                        serif: ['"Playfair Display"', '"Cormorant Garamond"', 'Georgia', 'serif'],
                        display: ['"Playfair Display"', 'serif'],
                        legacy: ['"Cormorant Garamond"', 'Georgia', 'serif'],
                    }},
                    animation: {{
                        'float-gentle': 'floatGentle 6s ease-in-out infinite',
                        'pulse-slow': 'pulseSlow 4s ease-in-out infinite',
                        'shimmer-gold': 'shimmerGold 3s infinite linear',
                        'breeze': 'breeze 8s ease-in-out infinite',
                        'slide-up': 'slideUp 0.7s ease forwards',
                        'fade-in': 'fadeIn 0.8s ease forwards',
                        'pulse-dot': 'pulseDot 2s ease-in-out infinite',
                        'ticker': 'ticker 30s linear infinite',
                    }},
                    keyframes: {{
                        floatGentle: {{
                            '0%, 100%': {{ transform: 'translateY(0px) rotate(0deg)' }},
                            '50%': {{ transform: 'translateY(-10px) rotate(1.5deg)' }},
                        }},
                        pulseSlow: {{
                            '0%, 100%': {{ opacity: '0.6', transform: 'scale(1)' }},
                            '50%': {{ opacity: '1', transform: 'scale(1.03)' }},
                        }},
                        shimmerGold: {{
                            '0%': {{ backgroundPosition: '-200% 0' }},
                            '100%': {{ backgroundPosition: '200% 0' }},
                        }},
                        breeze: {{
                            '0%, 100%': {{ transform: 'translateX(0px)' }},
                            '50%': {{ transform: 'translateX(15px)' }},
                        }},
                        slideUp: {{
                            '0%': {{ opacity: '0', transform: 'translateY(40px)' }},
                            '100%': {{ opacity: '1', transform: 'translateY(0)' }},
                        }},
                        fadeIn: {{
                            '0%': {{ opacity: '0' }},
                            '100%': {{ opacity: '1' }},
                        }},
                        pulseDot: {{
                            '0%, 100%': {{ transform: 'scale(1)', opacity: '1' }},
                            '50%': {{ transform: 'scale(1.6)', opacity: '0.4' }},
                        }},
                        ticker: {{
                            '0%': {{ transform: 'translateX(0)' }},
                            '100%': {{ transform: 'translateX(-50%)' }},
                        }},
                    }}
                }}
            }}
        }}
    </script>
    
    <!-- Lucide Icons CDN -->
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <style>
        /* ==============================
           LUXURY TYPOGRAPHY SYSTEM
           ============================== */
        .hero-headline {{
            font-family: 'Playfair Display', serif;
            font-weight: 800;
            letter-spacing: -0.02em;
            line-height: 1.1;
        }}
        .section-headline {{
            font-family: 'Playfair Display', serif;
            font-weight: 700;
            line-height: 1.2;
        }}
        .gold-shimmer-text {{
            background: linear-gradient(90deg, #b47b18, #d49a26, #f0c040, #e6a838, #b47b18);
            background-size: 300% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmerGold 4s linear infinite;
        }}

        /* ==============================
           GOLD & EMERALD GRADIENTS
           ============================== */
        .gold-gradient-text {{
            background: linear-gradient(135deg, #b47b18 0%, #d49a26 40%, #e6a838 70%, #9a6510 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .emerald-gradient-text {{
            background: linear-gradient(135deg, #0f3d21 0%, #15803d 50%, #14532d 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        /* ==============================
           BOTANICAL MESH BACKGROUNDS
           ============================== */
        .botanical-mesh {{
            background-color: #ffffff;
            background-image: 
                radial-gradient(at 0% 0%, rgba(20, 83, 45, 0.05) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(212, 154, 38, 0.06) 0px, transparent 50%),
                radial-gradient(at 50% 100%, rgba(22, 101, 52, 0.04) 0px, transparent 60%);
        }}
        .botanical-mesh-ivory {{
            background-color: #fbfdfa;
            background-image: 
                radial-gradient(at 10% 20%, rgba(20, 83, 45, 0.04) 0px, transparent 40%),
                radial-gradient(at 90% 80%, rgba(212, 154, 38, 0.05) 0px, transparent 50%);
        }}
        .botanical-mesh-gold {{
            background-color: #fffbf0;
            background-image:
                radial-gradient(at 20% 10%, rgba(212, 154, 38, 0.08) 0px, transparent 50%),
                radial-gradient(at 80% 90%, rgba(20, 83, 45, 0.05) 0px, transparent 50%);
        }}

        /* ==============================
           GLASSMORPHISM CARDS
           ============================== */
        .glass-card-luxury {{
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(20, 83, 45, 0.12);
            box-shadow: 0 20px 40px -15px rgba(20, 83, 45, 0.07), 0 0 1px 1px rgba(212, 154, 38, 0.15);
        }}
        .card-hover-organic {{
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .card-hover-organic:hover {{
            transform: translateY(-8px);
            border-color: rgba(212, 154, 38, 0.45);
            box-shadow: 0 25px 50px -12px rgba(20, 83, 45, 0.14), 0 0 25px 2px rgba(212, 154, 38, 0.2);
        }}
        .image-zoom-subtle {{
            transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .group:hover .image-zoom-subtle {{
            transform: scale(1.07);
        }}

        /* ==============================
           ORGANIC SEAL & BUTTONS
           ============================== */
        .organic-seal {{
            border: 2px dashed #d49a26;
            border-radius: 9999px;
            box-shadow: inset 0 0 12px rgba(212, 154, 38, 0.15);
        }}
        .btn-gold-shimmer {{
            background: linear-gradient(90deg, #d49a26 0%, #f59e0b 50%, #d49a26 100%);
            background-size: 200% auto;
            animation: shimmerGold 4s infinite linear;
        }}
        .btn-gold-shimmer:hover {{
            background-position: right center;
        }}
        .btn-sample {{
            background: linear-gradient(135deg, rgba(20,83,45,0.08) 0%, rgba(20,83,45,0.12) 100%);
            border: 1.5px solid rgba(20,83,45,0.3);
            color: #14532d;
            transition: all 0.3s ease;
        }}
        .btn-sample:hover {{
            background: linear-gradient(135deg, #14532d 0%, #0f3d21 100%);
            color: #ffffff;
            border-color: transparent;
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(20,83,45,0.25);
        }}

        /* ==============================
           SCROLL REVEAL ANIMATIONS
           ============================== */
        .reveal {{
            opacity: 0;
            transform: translateY(35px);
            transition: opacity 0.7s ease, transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .reveal.revealed {{
            opacity: 1;
            transform: translateY(0);
        }}
        .reveal-left {{
            opacity: 0;
            transform: translateX(-35px);
            transition: opacity 0.7s ease, transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .reveal-left.revealed {{
            opacity: 1;
            transform: translateX(0);
        }}
        .reveal-right {{
            opacity: 0;
            transform: translateX(35px);
            transition: opacity 0.7s ease, transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .reveal-right.revealed {{
            opacity: 1;
            transform: translateX(0);
        }}
        .reveal-delay-1 {{ transition-delay: 0.1s; }}
        .reveal-delay-2 {{ transition-delay: 0.2s; }}
        .reveal-delay-3 {{ transition-delay: 0.3s; }}
        .reveal-delay-4 {{ transition-delay: 0.4s; }}
        .reveal-delay-5 {{ transition-delay: 0.5s; }}

        /* ==============================
           TESTIMONIAL CARDS
           ============================== */
        .testimonial-card {{
            background: linear-gradient(145deg, #fffbf0 0%, #ffffff 100%);
            border: 1px solid rgba(212, 154, 38, 0.25);
            border-radius: 1.25rem;
            box-shadow: 0 8px 30px rgba(20,83,45,0.06), 0 2px 8px rgba(212,154,38,0.1);
            transition: all 0.4s ease;
        }}
        .testimonial-card:hover {{
            transform: translateY(-6px);
            box-shadow: 0 20px 40px rgba(20,83,45,0.1), 0 4px 12px rgba(212,154,38,0.2);
            border-color: rgba(212, 154, 38, 0.5);
        }}
        .quote-mark {{
            font-family: 'Playfair Display', serif;
            font-size: 5rem;
            line-height: 0.8;
            color: #d49a26;
            opacity: 0.3;
        }}

        /* ==============================
           LIGHTBOX (CERTIFICATE VIEWER)
           ============================== */
        .cert-lightbox-overlay {{
            display: none;
            position: fixed;
            inset: 0;
            z-index: 9999;
            background: rgba(3, 20, 10, 0.92);
            backdrop-filter: blur(8px);
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }}
        .cert-lightbox-overlay.active {{
            display: flex;
        }}
        .cert-lightbox-content {{
            background: white;
            border-radius: 1.5rem;
            padding: 2rem;
            max-width: 720px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            border: 2px solid rgba(212,154,38,0.4);
            box-shadow: 0 40px 80px rgba(0,0,0,0.5);
            position: relative;
        }}
        .cert-card {{
            cursor: pointer;
            border: 1px solid rgba(20,83,45,0.15);
            border-radius: 1rem;
            overflow: hidden;
            transition: all 0.35s ease;
            background: white;
        }}
        .cert-card:hover {{
            transform: translateY(-6px) scale(1.02);
            border-color: rgba(212,154,38,0.5);
            box-shadow: 0 15px 35px rgba(20,83,45,0.15), 0 0 0 2px rgba(212,154,38,0.3);
        }}
        .cert-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.35rem 0.85rem;
            border-radius: 9999px;
            font-size: 0.7rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }}

        /* ==============================
           ORIGIN MAP STYLES
           ============================== */
        .origin-region {{
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        .origin-region:hover .region-fill {{
            filter: brightness(1.2);
        }}
        .origin-dot {{
            animation: pulseDot 2s ease-in-out infinite;
        }}
        .origin-tooltip {{
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease, transform 0.3s ease;
            transform: translateY(4px);
        }}
        .origin-region:hover .origin-tooltip {{
            opacity: 1;
            transform: translateY(0);
        }}

        /* ==============================
           COUNTRY FLAGS STRIP
           ============================== */
        .country-flag-item {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.4rem;
            padding: 0.75rem 1rem;
            border-radius: 0.875rem;
            border: 1px solid transparent;
            transition: all 0.3s ease;
            cursor: default;
        }}
        .country-flag-item:hover {{
            background: rgba(20,83,45,0.06);
            border-color: rgba(212,154,38,0.3);
            transform: translateY(-3px);
        }}
        .flag-emoji {{
            font-size: 2rem;
            line-height: 1;
        }}

        /* ==============================
           STICKY SMART QUOTE BAR
           ============================== */
        #smart-quote-bar {{
            position: relative;
            z-index: 60;
        }}

        /* ==============================
           PDF BROCHURE BUTTON
           ============================== */
        .btn-brochure {{
            background: linear-gradient(135deg, #14532d 0%, #0f3d21 100%);
            color: white;
            border: 1.5px solid rgba(212,154,38,0.5);
            border-radius: 0.875rem;
            padding: 0.85rem 1.75rem;
            font-weight: 700;
            font-size: 0.85rem;
            letter-spacing: 0.04em;
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            transition: all 0.35s ease;
            text-decoration: none;
            box-shadow: 0 6px 20px rgba(20,83,45,0.2);
        }}
        .btn-brochure:hover {{
            background: linear-gradient(135deg, #0f3d21 0%, #072413 100%);
            transform: translateY(-3px);
            box-shadow: 0 12px 30px rgba(20,83,45,0.3);
            border-color: rgba(212,154,38,0.8);
        }}
    </style>
</head>
<body class="font-sans text-slate-800 bg-[#ffffff] antialiased selection:bg-brand-100 selection:text-brand-800 relative">
'''

def get_smart_quote_bar():
    """Sticky smart quote bar shown above the navbar on all pages."""
    return '''
    <!-- ✦ STICKY SMART QUOTE BAR ✦ -->
    <div id="smart-quote-bar" class="bg-gradient-to-r from-brand-700 via-brand-800 to-brand-700 border-b border-brand-gold/20 py-2.5 px-4">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2 text-[11px]">
            <div class="flex flex-wrap items-center gap-x-5 gap-y-1.5 text-emerald-100">
                <span class="flex items-center gap-1.5 font-medium">
                    <span class="text-brand-gold">📦</span>
                    <span>Min. Order: <strong class="text-white">500 kg</strong></span>
                </span>
                <span class="hidden sm:inline text-brand-700/60">|</span>
                <span class="flex items-center gap-1.5 font-medium">
                    <span class="text-brand-gold">✈</span>
                    <span>Ships to: <strong class="text-white">UK · USA · UAE · KSA · EU · CA · MY · SG</strong></span>
                </span>
                <span class="hidden sm:inline text-brand-700/60">|</span>
                <span class="flex items-center gap-1.5 font-medium">
                    <span class="text-brand-gold">🏆</span>
                    <span>Certified: <strong class="text-white">ISO 22000 · HACCP · SGS · Halal</strong></span>
                </span>
            </div>
            <a href="rfq.html?sample=1" class="shrink-0 flex items-center gap-2 bg-brand-gold hover:bg-amber-400 text-brand-950 font-bold px-4 py-1.5 rounded-lg transition duration-200 text-[11px] tracking-wide shadow-sm">
                <span>🎁</span>
                <span>Request Free Sample</span>
            </a>
        </div>
    </div>
    '''

def get_navbar(active_page):
    pages = [
        ("index.html", "Home", "index"),
        ("products.html", "Commodities & Specs", "products"),
        ("compliance.html", "Lab Standards & QA", "compliance"),
        ("trade-logistics.html", "Incoterms & Logistics", "logistics"),
        ("rfq.html", "RFQ & Samples", "rfq")
    ]
    
    links_html = ""
    for url, name, key in pages:
        if key == active_page:
            links_html += f'<a href="{url}" class="text-brand-700 font-bold text-sm tracking-wide border-b-2 border-brand-700 pb-1 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-brand-gold"></span>{name}</a>\n'
        else:
            links_html += f'<a href="{url}" class="text-slate-600 font-medium text-sm tracking-wide hover:text-brand-700 transition duration-200">{name}</a>\n'
            
    mobile_links = ""
    for url, name, key in pages:
        if key == active_page:
            mobile_links += f'<a href="{url}" class="block font-bold text-brand-700 py-2.5 px-3 rounded-lg bg-brand-50">{name}</a>\n'
        else:
            mobile_links += f'<a href="{url}" class="block font-medium text-slate-700 py-2.5 px-3 hover:bg-slate-50 hover:text-brand-700">{name}</a>\n'

    return f'''
    <!-- ✦ SMART QUOTE BAR ✦ -->
    {get_smart_quote_bar()}

    <!-- ✦ MAIN NAVIGATION BAR ✦ -->
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-xl border-b border-emerald-100 shadow-sm transition-all">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">
                <!-- Brand Logo -->
                <a href="index.html" class="flex items-center gap-3.5 group">
                    <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-brand-700 to-brand-900 border border-brand-gold/40 flex items-center justify-center text-brand-gold shadow-md shadow-brand-900/10 group-hover:scale-105 group-hover:border-brand-gold transition duration-300">
                        <i data-lucide="sprout" class="w-7 h-7"></i>
                    </div>
                    <div>
                        <span class="font-serif text-2xl font-bold tracking-tight text-brand-900 block leading-none">AGROVIA</span>
                        <span class="text-[9px] tracking-[0.28em] font-extrabold gold-gradient-text uppercase block mt-1">ORGANIC &bull; EXPORT AGENCY</span>
                    </div>
                </a>

                <!-- Desktop Menu -->
                <nav class="hidden lg:flex items-center gap-8">
                    {links_html}
                </nav>

                <!-- Action CTA -->
                <div class="hidden sm:flex items-center gap-3">
                    <a href="rfq.html?sample=1" class="px-4 py-2.5 rounded-xl border border-brand-gold/40 text-brand-800 bg-amber-50 hover:bg-amber-100 text-xs font-semibold flex items-center gap-1.5 transition duration-200">
                        <span>🎁</span>
                        <span>Free Sample</span>
                    </a>
                    <a href="rfq.html" class="px-5 py-2.5 rounded-xl bg-gradient-to-r from-brand-700 to-brand-800 hover:from-brand-800 hover:to-brand-900 text-white text-xs font-bold uppercase tracking-wider shadow-md shadow-brand-900/15 hover:shadow-lg transition duration-300 flex items-center gap-2 transform hover:-translate-y-0.5 border border-brand-gold/40">
                        <span class="text-brand-gold">✦</span>
                        <span>Request B2B Quote</span>
                        <i data-lucide="arrow-up-right" class="w-4 h-4 text-brand-gold"></i>
                    </a>
                </div>

                <!-- Mobile Menu Button -->
                <div class="lg:hidden">
                    <button id="mobile-menu-btn" class="p-2.5 rounded-xl text-slate-700 hover:bg-slate-100 border border-slate-200 focus:outline-none">
                        <i data-lucide="menu" class="w-6 h-6"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Menu Drawer -->
        <div id="mobile-menu" class="hidden lg:hidden border-t border-slate-200 bg-white px-6 pt-4 pb-8 space-y-2 shadow-xl">
            {mobile_links}
            <div class="pt-4 border-t border-slate-200 flex flex-col gap-3">
                <a href="rfq.html?sample=1" class="w-full py-3 text-center bg-amber-50 border border-brand-gold/40 text-brand-800 font-bold text-xs rounded-xl">🎁 Request Free Sample</a>
                <a href="rfq.html" class="w-full py-3 text-center bg-brand-800 text-white font-bold text-xs uppercase tracking-wider rounded-xl shadow">Request B2B Quote</a>
                <a href="https://wa.me/8801700000000" target="_blank" class="w-full py-3 text-center border border-emerald-600 text-emerald-800 bg-emerald-50 font-bold text-xs rounded-xl">WhatsApp Trade Concierge</a>
            </div>
        </div>
    </header>
    '''

def get_footer():
    return '''
    <!-- ✦ GLOBAL FOOTER ✦ -->
    <footer class="bg-gradient-to-b from-brand-950 to-[#020d06] text-slate-300 border-t border-brand-800/60 pt-20 pb-12 relative overflow-hidden">
        <!-- Ambient decorative background glow -->
        <div class="absolute -bottom-20 -left-20 w-96 h-96 bg-brand-600/10 rounded-full blur-3xl pointer-events-none"></div>
        <div class="absolute -top-20 -right-20 w-96 h-96 bg-brand-gold/10 rounded-full blur-3xl pointer-events-none"></div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-12 pb-16 border-b border-brand-800/60">
                
                <!-- Brand Profile -->
                <div class="lg:col-span-2 space-y-5">
                    <div class="flex items-center gap-3.5">
                        <div class="w-11 h-11 rounded-2xl bg-brand-800 border border-brand-gold/40 flex items-center justify-center text-brand-gold shadow-md">
                            <i data-lucide="sprout" class="w-6 h-6"></i>
                        </div>
                        <div>
                            <span class="font-serif text-2xl font-bold tracking-tight text-white block leading-none">AGROVIA</span>
                            <span class="text-[9px] tracking-[0.25em] font-extrabold gold-gradient-text uppercase block mt-1">ORGANIC &bull; EXPORT AGENCY</span>
                        </div>
                    </div>
                    <p class="text-xs text-slate-300 font-light leading-relaxed max-w-sm">
                        Agrovia Organic is Bangladesh's premier certified agricultural commodity export agency, connecting Sundarbans mangrove honey hunters, GI rice cultivators, and char farmers with global tier-1 food importers.
                    </p>
                    <div class="pt-2 space-y-1.5 text-xs text-slate-400 font-light">
                        <div><strong class="text-slate-200 font-medium">Founder & MD:</strong> Pranto Sarker</div>
                        <div><strong class="text-slate-200 font-medium">Origin:</strong> Dhaka, Bangladesh 🇧🇩</div>
                        <div><strong class="text-slate-200 font-medium">Regulatory:</strong> EPB / ERC / Trade License Registered Exporter</div>
                    </div>
                    <!-- Brochure Download CTA in Footer -->
                    <a href="rfq.html?brochure=1" class="inline-flex items-center gap-2 mt-2 px-4 py-2 rounded-lg bg-brand-800 border border-brand-gold/30 text-brand-gold hover:bg-brand-700 transition text-xs font-semibold">
                        <i data-lucide="download" class="w-3.5 h-3.5"></i>
                        <span>Download Product Catalogue</span>
                    </a>
                </div>

                <!-- Commodities -->
                <div class="space-y-4">
                    <h4 class="font-bold text-xs uppercase tracking-widest text-brand-gold">Export Portfolio</h4>
                    <ul class="space-y-2.5 text-xs">
                        <li><a href="products.html#honey" class="hover:text-brand-gold transition duration-200">Sundarbans Raw Honey</a></li>
                        <li><a href="products.html#rice" class="hover:text-brand-gold transition duration-200">Chinigura & GI Tulshimala Rice</a></li>
                        <li><a href="products.html#fish" class="hover:text-brand-gold transition duration-200">Pesticide-Free Dried Fish (Shukti)</a></li>
                        <li><a href="products.html#peanuts" class="hover:text-brand-gold transition duration-200">Northern Char Peanuts & Butter</a></li>
                        <li><a href="products.html#fruits" class="hover:text-brand-gold transition duration-200">Himsagar Mango (GI) & Jackfruit</a></li>
                    </ul>
                </div>

                <!-- Compliance & Trade -->
                <div class="space-y-4">
                    <h4 class="font-bold text-xs uppercase tracking-widest text-brand-gold">Trade & Quality</h4>
                    <ul class="space-y-2.5 text-xs">
                        <li><a href="compliance.html" class="hover:text-brand-gold transition duration-200">Lab Standards (IRMS / HPLC)</a></li>
                        <li><a href="compliance.html" class="hover:text-brand-gold transition duration-200">Pre-Shipment Inspection (SGS/BV)</a></li>
                        <li><a href="trade-logistics.html" class="hover:text-brand-gold transition duration-200">Incoterms 2020 (FOB / CFR / CIF)</a></li>
                        <li><a href="trade-logistics.html#banking" class="hover:text-brand-gold transition duration-200">Sight LC (UCP 600) & CAD</a></li>
                        <li><a href="rfq.html" class="hover:text-brand-gold transition duration-200">B2B Sample Order Protocol</a></li>
                    </ul>
                </div>

                <!-- Export Desk -->
                <div class="space-y-4">
                    <h4 class="font-bold text-xs uppercase tracking-widest text-brand-gold">International Desk</h4>
                    <div class="text-xs space-y-2.5">
                        <div class="flex items-center gap-2 text-slate-300">
                            <i data-lucide="map-pin" class="w-4 h-4 text-brand-gold shrink-0"></i>
                            <span>Gulshan Commercial Area, Dhaka</span>
                        </div>
                        <div class="flex items-center gap-2 text-slate-300">
                            <i data-lucide="mail" class="w-4 h-4 text-brand-gold shrink-0"></i>
                            <span>export@agroviaorganic.com</span>
                        </div>
                        <div class="flex items-center gap-2 text-slate-300">
                            <i data-lucide="phone" class="w-4 h-4 text-brand-gold shrink-0"></i>
                            <span>WhatsApp: +880 1700-000000</span>
                        </div>
                    </div>
                    <div class="pt-2">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-brand-900 border border-brand-800 text-[10px] text-brand-200 font-mono">
                            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                            <span>TIMEZONE: GMT+6 (BST)</span>
                        </span>
                    </div>
                </div>

            </div>

            <!-- Bottom Credits -->
            <div class="pt-8 flex flex-col sm:flex-row justify-between items-center gap-4 text-xs text-slate-400">
                <div>
                    &copy; 2026 <strong class="text-slate-200">AGROVIA ORGANIC</strong>. All Rights Reserved. Founded by Pranto Sarker.
                </div>
                <div class="flex items-center gap-6">
                    <span class="hover:text-slate-200">ISO 22000 & HACCP Framework</span>
                    <span>&bull;</span>
                    <span class="hover:text-slate-200">Bangladesh Bank EXP Compliance</span>
                </div>
            </div>
        </div>
    </footer>

    <!-- Floating WhatsApp Widget -->
    <a href="https://wa.me/8801700000000?text=Hello%20Agrovia%20Organic,%20I%20am%20interested%20in%20sourcing%20agricultural%20commodities." target="_blank" class="fixed bottom-6 right-6 z-50 p-3.5 rounded-2xl bg-gradient-to-tr from-emerald-700 to-emerald-600 text-white shadow-2xl shadow-emerald-950/40 hover:scale-110 transition duration-300 flex items-center gap-2.5 group border border-emerald-400/40">
        <i data-lucide="message-circle" class="w-6 h-6"></i>
        <span class="text-xs font-bold tracking-wide hidden group-hover:inline-block pr-1 transition-all duration-300">WhatsApp Trade Desk</span>
    </a>

    <!-- Global Scripts -->
    <script>
        lucide.createIcons();
        // Mobile menu
        const menuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        if (menuBtn && mobileMenu) {
            menuBtn.addEventListener('click', () => { mobileMenu.classList.toggle('hidden'); });
        }

        // Scroll Reveal (Intersection Observer)
        const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
        if (revealElements.length > 0) {
            const revealObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('revealed');
                    }
                });
            }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
            revealElements.forEach(el => revealObserver.observe(el));
        }

        // Certificate Lightbox
        function openCertLightbox(certId) {
            const overlay = document.getElementById('cert-lightbox-overlay');
            const content = document.getElementById('cert-lightbox-content');
            if (!overlay || !content) return;
            const certData = window.certDetails && window.certDetails[certId];
            if (certData) {
                content.innerHTML = `
                    <button onclick="closeCertLightbox()" class="absolute top-4 right-4 w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-600 font-bold text-lg transition">&times;</button>
                    <div class="space-y-4">
                        <div class="flex items-center gap-3">
                            <span class="text-3xl">${certData.icon}</span>
                            <div>
                                <h3 class="font-serif text-xl font-bold text-brand-900">${certData.name}</h3>
                                <p class="text-xs text-slate-500 font-medium">${certData.issuer}</p>
                            </div>
                        </div>
                        <div class="h-0.5 bg-gradient-to-r from-brand-700 to-brand-gold opacity-30 rounded"></div>
                        <p class="text-sm text-slate-700 leading-relaxed">${certData.description}</p>
                        <div class="grid grid-cols-2 gap-3">
                            ${certData.specs.map(s => `<div class="bg-emerald-50 rounded-lg p-3 border border-emerald-100"><div class="text-[10px] font-bold uppercase tracking-widest text-brand-700 mb-1">${s.label}</div><div class="text-sm font-semibold text-slate-800">${s.value}</div></div>`).join('')}
                        </div>
                        <div class="bg-amber-50 border border-brand-gold/30 rounded-xl p-4">
                            <p class="text-xs text-amber-800 font-medium">✦ This certification is verified by independent third-party auditors. Original certificate copies are available on request for qualified B2B buyers.</p>
                        </div>
                        <a href="rfq.html" class="inline-flex items-center gap-2 px-5 py-2.5 bg-brand-700 hover:bg-brand-800 text-white font-bold text-xs uppercase tracking-wider rounded-xl transition">Request Certificate Copies →</a>
                    </div>
                `;
            }
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
        function closeCertLightbox() {
            const overlay = document.getElementById('cert-lightbox-overlay');
            if (overlay) overlay.classList.remove('active');
            document.body.style.overflow = '';
        }
        // Close on backdrop click
        document.addEventListener('click', function(e) {
            const overlay = document.getElementById('cert-lightbox-overlay');
            if (overlay && e.target === overlay) closeCertLightbox();
        });
    </script>
</body>
</html>
'''

print("site_templates.py ready! Phase 2 Upgrade — Playfair Display + Smart Bar + Lightbox + Scroll Reveal")
