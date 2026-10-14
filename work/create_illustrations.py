#!/usr/bin/env python3
"""
Generate high-quality 16:9 storybook illustrations (SVGs) for Stories 41-60.
Each SVG has viewBox="0 0 800 450" (16:9 ratio) and features rich savanna
landscapes, detailed animal silhouettes/illustrations, and storybook styling.
"""

from pathlib import Path

DEST_DIRS = [
    Path(r"c:\folk_tale_stories\outputs\kalulu-reader\assets\covers"),
    Path(r"c:\folk_tale_stories\outputs\kalulu-android\www\assets\covers")
]

STORIES = [
    (41, "Why the Lion Roars", "Lion and the Golden Honey Bees",
     """
     <!-- Lion & Honey Scene -->
     <defs>
       <linearGradient id="sky41" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdba74"/><stop offset="55%" stop-color="#fed7aa"/><stop offset="100%" stop-color="#fef3c7"/></linearGradient>
       <linearGradient id="sun41" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ea580c"/><stop offset="100%" stop-color="#f59e0b"/></linearGradient>
       <linearGradient id="grass41" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#b45309"/><stop offset="100%" stop-color="#78350f"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky41)"/>
     <circle cx="680" cy="110" r="65" fill="url(#sun41)" opacity="0.85"/>
     <path d="M0 320 Q200 290 400 320 T800 310 L800 450 L0 450 Z" fill="#92400e" opacity="0.6"/>
     <path d="M0 350 Q250 330 500 360 T800 340 L800 450 L0 450 Z" fill="url(#grass41)"/>
     <!-- Acacia Tree -->
     <path d="M120 370 L135 220 L110 180 M135 220 L160 170 M135 250 L180 230" stroke="#451a03" stroke-width="8" stroke-linecap="round"/>
     <ellipse cx="140" cy="165" rx="90" ry="22" fill="#365314" opacity="0.9"/>
     <ellipse cx="170" cy="155" rx="60" ry="16" fill="#4d7c0f" opacity="0.8"/>
     <!-- Honey Pot -->
     <ellipse cx="250" cy="385" rx="30" ry="12" fill="#78350f"/>
     <path d="M225 385 C220 350 230 330 250 330 C270 330 280 350 275 385 Z" fill="#b45309"/>
     <ellipse cx="250" cy="330" rx="18" ry="7" fill="#fbbf24"/>
     <!-- Golden Lion Silhouette & Face -->
     <g transform="translate(420, 210)">
       <!-- Mane -->
       <path d="M110 50 C50 -20 180 -30 200 40 C240 10 260 90 220 130 C250 170 190 220 130 190 C80 210 40 160 60 120 C30 80 70 30 110 50 Z" fill="#9a3412"/>
       <!-- Body -->
       <path d="M140 150 C180 140 240 150 290 190 L270 210 L160 210 Z" fill="#c2410c"/>
       <!-- Head -->
       <ellipse cx="135" cy="100" rx="42" ry="48" fill="#ea580c"/>
       <!-- Muzzle -->
       <ellipse cx="135" cy="120" rx="24" ry="18" fill="#fef3c7"/>
       <polygon points="135,112 127,120 143,120" fill="#451a03"/>
       <!-- Roaring Mouth -->
       <path d="M125 125 Q135 142 145 125 Z" fill="#7f1d1d"/>
       <!-- Eyes -->
       <ellipse cx="120" cy="95" rx="5" ry="4" fill="#451a03"/>
       <ellipse cx="150" cy="95" rx="5" ry="4" fill="#451a03"/>
       <!-- Ears -->
       <circle cx="102" cy="62" r="14" fill="#ea580c"/>
       <circle cx="168" cy="62" r="14" fill="#ea580c"/>
     </g>
     <!-- Flying Bees -->
     <g fill="#fbbf24">
       <circle cx="330" cy="270" r="5"/><circle cx="338" cy="265" r="4"/><circle cx="355" cy="280" r="5"/><circle cx="370" cy="260" r="4"/><circle cx="385" cy="290" r="5"/>
     </g>
     """),

    (42, "Why Ostrich Has a Long Neck", "Ostrich & Crocodile at the River",
     """
     <defs>
       <linearGradient id="sky42" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="60%" stop-color="#bae6fd"/><stop offset="100%" stop-color="#fef08a"/></linearGradient>
       <linearGradient id="river42" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0284c7"/><stop offset="100%" stop-color="#0369a1"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky42)"/>
     <!-- Distant Hills -->
     <path d="M0 240 Q300 180 600 240 T800 220 L800 450 L0 450 Z" fill="#84cc16" opacity="0.7"/>
     <!-- Riverbank -->
     <path d="M0 320 Q400 280 800 330 L800 450 L0 450 Z" fill="#eab308"/>
     <!-- River Water -->
     <path d="M280 340 Q550 320 800 350 L800 450 L200 450 Z" fill="url(#river42)"/>
     <!-- Ostrich with Long Stretched Neck -->
     <g transform="translate(180, 140)">
       <!-- Long Curving Neck -->
       <path d="M80 180 C80 120 120 40 180 30 C200 28 210 38 200 50 C150 60 120 130 110 180 Z" fill="#475569"/>
       <!-- Head -->
       <ellipse cx="205" cy="38" rx="18" ry="12" fill="#64748b"/>
       <!-- Beak -->
       <polygon points="220,35 240,40 220,44" fill="#f59e0b"/>
       <circle cx="208" cy="35" r="3" fill="#0f172a"/>
       <!-- Ostrich Body -->
       <ellipse cx="80" cy="210" rx="60" ry="45" fill="#1e293b"/>
       <ellipse cx="90" cy="205" rx="40" ry="30" fill="#f8fafc"/>
       <!-- Legs -->
       <path d="M70 250 L65 310 M100 250 L105 310" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
     </g>
     <!-- Crocodile in Water -->
     <g transform="translate(480, 330)">
       <!-- Snout & Body -->
       <path d="M0 35 Q80 15 180 30 L160 60 L10 50 Z" fill="#15803d"/>
       <!-- Crocodile Eye -->
       <circle cx="120" cy="22" r="7" fill="#84cc16"/>
       <circle cx="120" cy="22" r="3" fill="#052e16"/>
       <!-- Teeth -->
       <polygon points="40,35 48,27 55,35 63,27 70,35" fill="#f8fafc"/>
     </g>
     """),

    (43, "Why the Hippo Has No Hair", "Hippo by the Fire and River",
     """
     <defs>
       <linearGradient id="sky43" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f97316"/><stop offset="50%" stop-color="#fbbf24"/><stop offset="100%" stop-color="#fef08a"/></linearGradient>
       <linearGradient id="water43" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0284c7"/><stop offset="100%" stop-color="#075985"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky43)"/>
     <!-- Savanna Fire Glow -->
     <ellipse cx="140" cy="310" rx="110" ry="40" fill="#dc2626" opacity="0.4"/>
     <!-- Flame Silhouettes -->
     <path d="M70 330 Q90 260 110 320 Q130 240 150 315 Q170 250 190 330 Z" fill="#ea580c"/>
     <path d="M90 330 Q110 280 125 325 Q145 270 160 330 Z" fill="#facc15"/>
     <!-- River -->
     <path d="M0 340 Q400 300 800 330 L800 450 L0 450 Z" fill="url(#water43)"/>
     <!-- Big Smooth Hairless Hippo in Water -->
     <g transform="translate(380, 230)">
       <!-- Hippo Back & Body -->
       <ellipse cx="180" cy="110" rx="140" ry="85" fill="#64748b"/>
       <!-- Large Head & Snout -->
       <ellipse cx="90" cy="85" rx="75" ry="55" fill="#475569"/>
       <ellipse cx="50" cy="100" rx="45" ry="35" fill="#334155"/>
       <!-- Nostrils -->
       <ellipse cx="35" cy="85" rx="8" ry="6" fill="#1e293b"/>
       <!-- Little Ears -->
       <circle cx="120" cy="45" r="10" fill="#475569"/>
       <!-- Eyes -->
       <circle cx="85" cy="65" r="7" fill="#0f172a"/>
       <circle cx="87" cy="63" r="2" fill="#fff"/>
       <!-- Water Ripples -->
       <ellipse cx="160" cy="160" rx="160" ry="12" fill="none" stroke="#38bdf8" stroke-width="4" opacity="0.7"/>
     </g>
     """),

    (44, "Why Crocodile Lives in Water", "Sunbathing Crocodile on Sandbank",
     """
     <defs>
       <linearGradient id="sky44" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0284c7"/><stop offset="70%" stop-color="#7dd3fc"/><stop offset="100%" stop-color="#fef3c7"/></linearGradient>
       <linearGradient id="sand44" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#d97706"/><stop offset="100%" stop-color="#f59e0b"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky44)"/>
     <!-- Deep Blue Water -->
     <rect y="260" width="800" height="190" fill="#0369a1"/>
     <!-- Sandbar Island -->
     <ellipse cx="380" cy="330" rx="320" ry="65" fill="url(#sand44)"/>
     <!-- Crocodile Sunning on Island -->
     <g transform="translate(200, 260)">
       <!-- Body -->
       <path d="M40 50 Q160 20 300 45 L360 65 L280 75 Q160 80 40 50 Z" fill="#166534"/>
       <!-- Tail Scutes -->
       <path d="M300 45 Q360 55 420 70 L380 80 L300 65 Z" fill="#14532d"/>
       <!-- Head -->
       <polygon points="40,50 0,60 45,70" fill="#15803d"/>
       <circle cx="35" cy="52" r="5" fill="#facc15"/>
       <circle cx="35" cy="52" r="2" fill="#000"/>
       <!-- Webbed Claws -->
       <path d="M120 70 L110 85 M220 70 L210 85" stroke="#14532d" stroke-width="6" stroke-linecap="round"/>
     </g>
     <!-- Water Reflections -->
     <path d="M100 410 Q400 395 700 410" stroke="#38bdf8" stroke-width="3" fill="none" opacity="0.6"/>
     """),

    (45, "Why Tortoise Has a Broken Shell", "Tortoise Falling from Cloud and Birds",
     """
     <defs>
       <linearGradient id="sky45" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1e3a8a"/><stop offset="60%" stop-color="#3b82f6"/><stop offset="100%" stop-color="#93c5fd"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky45)"/>
     <!-- Fluffy White Clouds -->
     <ellipse cx="200" cy="110" rx="90" ry="40" fill="#ffffff" opacity="0.85"/>
     <ellipse cx="270" cy="95" rx="70" ry="35" fill="#ffffff" opacity="0.9"/>
     <ellipse cx="580" cy="140" rx="100" ry="45" fill="#ffffff" opacity="0.85"/>
     <!-- Flying Birds Silhouettes -->
     <g fill="#1e293b">
       <path d="M360 80 Q375 60 390 80 Q405 60 420 80 Q390 90 360 80 Z"/>
       <path d="M470 120 Q482 105 495 120 Q508 105 520 120 Q495 128 470 120 Z"/>
     </g>
     <!-- Falling Tortoise with Cracked Pattern Shell -->
     <g transform="translate(350, 180) rotate(22)">
       <!-- Domed Shell -->
       <ellipse cx="60" cy="60" rx="65" ry="48" fill="#b45309"/>
       <!-- Shell Segments & Fracture Lines -->
       <path d="M15 60 L105 60 M60 15 L60 105 M35 30 L85 90 M85 30 L35 90" stroke="#fef08a" stroke-width="4"/>
       <!-- Head & Feet -->
       <circle cx="130" cy="55" r="16" fill="#15803d"/>
       <circle cx="134" cy="52" r="3" fill="#000"/>
       <ellipse cx="30" cy="20" rx="12" ry="8" fill="#15803d"/>
       <ellipse cx="90" cy="20" rx="12" ry="8" fill="#15803d"/>
       <ellipse cx="30" cy="100" rx="12" ry="8" fill="#15803d"/>
       <ellipse cx="90" cy="100" rx="12" ry="8" fill="#15803d"/>
     </g>
     <!-- Ground Crags Below -->
     <polygon points="0,450 150,380 300,420 500,370 700,430 800,360 800,450" fill="#78350f"/>
     """),

    (46, "Why Baboon Has a Bare Bottom", "Baboon on Sun-Heated Granite Kopje",
     """
     <defs>
       <linearGradient id="sky46" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fb923c"/><stop offset="60%" stop-color="#fed7aa"/><stop offset="100%" stop-color="#fef3c7"/></linearGradient>
       <linearGradient id="rock46" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#78716c"/><stop offset="100%" stop-color="#44403c"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky46)"/>
     <!-- Hot Blazing Sun -->
     <circle cx="680" cy="110" r="60" fill="#ea580c"/>
     <!-- Granite Boulders (Kopje) -->
     <path d="M100 450 Q300 240 600 320 T800 450 Z" fill="url(#rock46)"/>
     <ellipse cx="380" cy="330" rx="220" ry="80" fill="#57534e"/>
     <!-- Baboon Sitting on Heated Rock -->
     <g transform="translate(360, 190)">
       <!-- Tail -->
       <path d="M130 110 Q160 50 180 80" stroke="#713f12" stroke-width="8" fill="none" stroke-linecap="round"/>
       <!-- Bare Bright Red Patch -->
       <ellipse cx="120" cy="115" rx="18" ry="12" fill="#ef4444"/>
       <!-- Body -->
       <ellipse cx="75" cy="85" rx="45" ry="38" fill="#78350f"/>
       <!-- Arms Resting on Knees -->
       <path d="M60 85 L35 125 M85 85 L70 125" stroke="#78350f" stroke-width="12" stroke-linecap="round"/>
       <!-- Dog-like Muzzle & Head -->
       <circle cx="45" cy="45" r="22" fill="#78350f"/>
       <ellipse cx="30" cy="50" rx="16" ry="12" fill="#292524"/>
       <circle cx="42" cy="40" r="3" fill="#facc15"/>
     </g>
     """),

    (47, "Why the Warthog Runs with Its Tail Up", "Proud Warthog Trotting in Tall Grass",
     """
     <defs>
       <linearGradient id="sky47" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="50%" stop-color="#fed7aa"/><stop offset="100%" stop-color="#fdba74"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky47)"/>
     <!-- Savanna Trees -->
     <ellipse cx="680" cy="200" rx="80" ry="25" fill="#4d7c0f"/>
     <path d="M670 320 L680 200" stroke="#78350f" stroke-width="10"/>
     <!-- Savanna Field -->
     <rect y="290" width="800" height="160" fill="#ca8a04"/>
     <!-- Warthog Trotting with Tail Erect -->
     <g transform="translate(260, 200)">
       <!-- Antenna Tail Straight Up! -->
       <path d="M220 80 L225 -20" stroke="#451a03" stroke-width="6" stroke-linecap="round"/>
       <!-- Tuft on Tail -->
       <ellipse cx="225" cy="-24" rx="8" ry="12" fill="#1c1917"/>
       <!-- Heavy Body -->
       <ellipse cx="140" cy="90" rx="85" ry="48" fill="#78716c"/>
       <!-- Legs Trotting -->
       <path d="M80 130 L65 175 M115 130 L125 175 M175 130 L160 175 M205 130 L220 175" stroke="#57534e" stroke-width="10" stroke-linecap="round"/>
       <!-- Head with Tusks & Warts -->
       <path d="M70 65 L15 85 L65 110 Z" fill="#57534e"/>
       <!-- Curved White Tusks -->
       <path d="M30 95 Q10 70 25 55" stroke="#f8fafc" stroke-width="5" fill="none" stroke-linecap="round"/>
       <!-- Mane on Neck -->
       <path d="M120 45 Q90 35 60 55" stroke="#1c1917" stroke-width="8" fill="none"/>
       <circle cx="50" cy="72" r="3" fill="#000"/>
     </g>
     <!-- Golden Tall Grass in Foreground -->
     <g stroke="#eab308" stroke-width="4">
       <line x1="50" y1="450" x2="60" y2="360"/><line x1="80" y1="450" x2="70" y2="350"/><line x1="220" y1="450" x2="235" y2="370"/><line x1="520" y1="450" x2="510" y2="355"/>
     </g>
     """),

    (48, "Why Elephant Has Small Eyes", "Grand African Elephant Under Baobab",
     """
     <defs>
       <linearGradient id="sky48" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdba74"/><stop offset="100%" stop-color="#fde047"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky48)"/>
     <!-- Ancient Baobab Trunk -->
     <path d="M50 450 C80 320 100 240 140 180 C180 240 200 320 230 450 Z" fill="#78350f"/>
     <ellipse cx="140" cy="140" rx="110" ry="40" fill="#3f6212"/>
     <!-- Savanna Ground -->
     <rect y="330" width="800" height="120" fill="#a16207"/>
     <!-- Great Elephant -->
     <g transform="translate(320, 150)">
       <!-- Huge Body -->
       <ellipse cx="220" cy="120" rx="130" ry="100" fill="#64748b"/>
       <!-- Giant Sturdy Legs -->
       <rect x="130" y="180" width="40" height="85" rx="10" fill="#475569"/>
       <rect x="250" y="180" width="40" height="85" rx="10" fill="#475569"/>
       <!-- Big Ear -->
       <path d="M90 60 C30 40 10 140 70 170 C100 150 110 110 90 60 Z" fill="#475569"/>
       <!-- Head & Trunk -->
       <circle cx="105" cy="100" r="48" fill="#64748b"/>
       <path d="M110 130 Q100 220 50 240 Q40 220 80 180" stroke="#64748b" stroke-width="24" fill="none" stroke-linecap="round"/>
       <!-- White Ivory Tusk -->
       <path d="M85 145 Q40 175 30 150" stroke="#f8fafc" stroke-width="8" fill="none" stroke-linecap="round"/>
       <!-- The Famous Small Eye -->
       <circle cx="95" cy="90" r="3" fill="#0f172a"/>
     </g>
     """),

    (49, "Why Guinea-Fowl Has White Spots", "Speckled Guinea Fowl Flock",
     """
     <defs>
       <linearGradient id="sky49" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="70%" stop-color="#bae6fd"/><stop offset="100%" stop-color="#fef08a"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky49)"/>
     <rect y="310" width="800" height="140" fill="#84cc16"/>
     <!-- Acacia Shrub -->
     <ellipse cx="640" cy="240" rx="90" ry="30" fill="#4d7c0f"/>
     <path d="M635 320 L640 240" stroke="#713f12" stroke-width="8"/>
     <!-- Spotted Guinea Fowl -->
     <g transform="translate(300, 180)">
       <!-- Plump Round Body -->
       <ellipse cx="120" cy="100" rx="75" ry="55" fill="#1e293b"/>
       <!-- White Polka Dots Everywhere! -->
       <g fill="#f8fafc">
         <circle cx="80" cy="80" r="3"/><circle cx="100" cy="75" r="3"/><circle cx="120" cy="80" r="3"/><circle cx="140" cy="85" r="3"/>
         <circle cx="70" cy="100" r="3"/><circle cx="90" cy="100" r="3"/><circle cx="110" cy="105" r="3"/><circle cx="130" cy="105" r="3"/>
         <circle cx="85" cy="120" r="3"/><circle cx="105" cy="125" r="3"/><circle cx="125" cy="125" r="3"/><circle cx="145" cy="115" r="3"/>
         <circle cx="160" cy="100" r="3"/><circle cx="150" cy="95" r="3"/>
       </g>
       <!-- Slender Neck & Head with Blue/Red Helmet -->
       <path d="M60 85 Q40 40 45 25" stroke="#0284c7" stroke-width="12" fill="none" stroke-linecap="round"/>
       <circle cx="45" cy="20" r="12" fill="#0284c7"/>
       <polygon points="45,10 52,2 50,15" fill="#dc2626"/>
       <polygon points="35,22 22,25 35,28" fill="#f59e0b"/>
       <circle cx="42" cy="18" r="2" fill="#000"/>
       <!-- Legs -->
       <path d="M100 150 L95 190 M135 150 L140 190" stroke="#d97706" stroke-width="4" stroke-linecap="round"/>
     </g>
     """),

    (50, "Why Hyena Limps", "Spotted Hyena in Moonlit Savanna",
     """
     <defs>
       <linearGradient id="sky50" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0f172a"/><stop offset="60%" stop-color="#1e1b4b"/><stop offset="100%" stop-color="#312e81"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky50)"/>
     <!-- Luminous Full Moon -->
     <circle cx="620" cy="100" r="55" fill="#fef08a"/>
     <path d="M0 320 Q400 290 800 330 L800 450 L0 450 Z" fill="#1e293b"/>
     <!-- Sloping Back Hyena -->
     <g transform="translate(260, 200)">
       <!-- Sloping Body from High Shoulders to Low Hips -->
       <path d="M50 50 Q120 40 190 85 L180 125 L40 110 Z" fill="#78716c"/>
       <!-- Spots on Body -->
       <g fill="#292524" opacity="0.75">
         <circle cx="100" cy="65" r="6"/><circle cx="130" cy="70" r="5"/><circle cx="160" cy="88" r="6"/>
         <circle cx="115" cy="85" r="5"/><circle cx="145" cy="98" r="5"/>
       </g>
       <!-- Front High Legs -->
       <path d="M60 110 L50 165 M80 110 L85 165" stroke="#57534e" stroke-width="9" stroke-linecap="round"/>
       <!-- Hind Shorter Limping Leg -->
       <path d="M170 115 L160 155 M190 115 L185 145" stroke="#57534e" stroke-width="8" stroke-linecap="round"/>
       <!-- Broad Head & Rounded Ears -->
       <circle cx="35" cy="45" r="24" fill="#57534e"/>
       <circle cx="22" cy="25" r="10" fill="#292524"/>
       <circle cx="45" cy="22" r="10" fill="#292524"/>
       <polygon points="25,50 5,60 25,68" fill="#1c1917"/>
       <!-- Glowing Eye in the Dark -->
       <circle cx="30" cy="42" r="4" fill="#facc15"/>
     </g>
     """),

    (51, "Why Zebra Has Stripes", "Dazzle of Zebras in Golden Savanna",
     """
     <defs>
       <linearGradient id="sky51" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="70%" stop-color="#fed7aa"/><stop offset="100%" stop-color="#fef3c7"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky51)"/>
     <rect y="300" width="800" height="150" fill="#d97706"/>
     <!-- Zebra Galloping -->
     <g transform="translate(280, 160)">
       <!-- White Coat Base -->
       <ellipse cx="140" cy="100" rx="90" ry="50" fill="#f8fafc"/>
       <!-- Black Bold Stripes -->
       <g fill="#0f172a">
         <polygon points="90,55 98,55 105,145 95,145"/>
         <polygon points="115,52 124,52 130,148 120,148"/>
         <polygon points="142,52 150,52 154,148 145,148"/>
         <polygon points="168,55 177,55 178,145 168,145"/>
         <polygon points="192,65 200,65 198,135 189,135"/>
       </g>
       <!-- Neck & Head with Stripes -->
       <path d="M70 90 L30 30 L55 20 L95 70 Z" fill="#f8fafc"/>
       <polygon points="65,30 75,25 85,60 75,65" fill="#0f172a"/>
       <circle cx="30" cy="25" r="16" fill="#f8fafc"/>
       <ellipse cx="18" cy="30" rx="12" ry="8" fill="#0f172a"/>
       <circle cx="32" cy="20" r="3" fill="#000"/>
       <!-- Mane -->
       <path d="M85 60 L25 15" stroke="#0f172a" stroke-width="8" stroke-dasharray="4,3"/>
       <!-- Legs -->
       <path d="M75 145 L70 200 M110 145 L115 200 M180 145 L175 200 M215 140 L225 195" stroke="#f8fafc" stroke-width="9" stroke-linecap="round"/>
     </g>
     """),

    (52, "Why Leopard Has Spots", "Leopard on Savanna Tree Branch",
     """
     <defs>
       <linearGradient id="sky52" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f97316"/><stop offset="50%" stop-color="#fbbf24"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky52)"/>
     <!-- Heavy Tree Branch Across the Frame -->
     <path d="M0 260 Q350 240 800 290 L800 340 Q350 290 0 320 Z" fill="#451a03"/>
     <!-- Leaves Clusters -->
     <ellipse cx="650" cy="220" rx="70" ry="30" fill="#15803d"/>
     <ellipse cx="730" cy="250" rx="60" ry="25" fill="#166534"/>
     <!-- Sleek Leopard Resting on Branch -->
     <g transform="translate(240, 160)">
       <!-- Hanging Tail with Rings -->
       <path d="M300 90 Q340 140 330 190" stroke="#f59e0b" stroke-width="12" fill="none" stroke-linecap="round"/>
       <!-- Body -->
       <ellipse cx="180" cy="85" rx="110" ry="38" fill="#f59e0b"/>
       <!-- Hanging Paws -->
       <path d="M110 100 L110 145 M240 100 L240 145" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
       <!-- Head & Whisker Muzzle -->
       <circle cx="80" cy="65" r="28" fill="#f59e0b"/>
       <circle cx="68" cy="45" r="8" fill="#b45309"/>
       <circle cx="95" cy="45" r="8" fill="#b45309"/>
       <ellipse cx="70" cy="72" rx="12" ry="8" fill="#fef3c7"/>
       <circle cx="75" cy="60" r="3" fill="#15803d"/>
       <!-- Rosette Spots -->
       <g fill="none" stroke="#451a03" stroke-width="3">
         <circle cx="130" cy="75" r="6"/><circle cx="160" cy="65" r="6"/><circle cx="190" cy="75" r="6"/>
         <circle cx="220" cy="68" r="6"/><circle cx="250" cy="78" r="6"/><circle cx="150" cy="95" r="6"/>
         <circle cx="180" cy="98" r="6"/><circle cx="210" cy="95" r="6"/>
       </g>
     </g>
     """),

    (53, "Why Monkey Lives in the Trees", "Vervet Monkeys in Forest Canopy",
     """
     <defs>
       <linearGradient id="sky53" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#6ee7b7"/><stop offset="60%" stop-color="#a7f3d0"/><stop offset="100%" stop-color="#ecfdf5"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky53)"/>
     <!-- Deep Forest Canopy Leaves -->
     <ellipse cx="120" cy="60" rx="160" ry="70" fill="#065f46"/>
     <ellipse cx="400" cy="50" rx="190" ry="80" fill="#047857"/>
     <ellipse cx="680" cy="70" rx="170" ry="75" fill="#059669"/>
     <!-- Vines & Branches -->
     <path d="M0 160 Q250 280 500 170 T800 220" stroke="#78350f" stroke-width="12" fill="none"/>
     <path d="M200 100 Q240 240 220 340" stroke="#166534" stroke-width="6" fill="none"/>
     <!-- Monkey Swinging from Branch -->
     <g transform="translate(340, 160)">
       <!-- Long Prehensile Tail -->
       <path d="M120 70 Q160 30 180 70" stroke="#92400e" stroke-width="8" fill="none" stroke-linecap="round"/>
       <!-- Body -->
       <ellipse cx="70" cy="80" rx="42" ry="30" fill="#92400e"/>
       <!-- Limbs Reaching to Vine -->
       <path d="M50 70 L30 10 M80 70 L95 15 M45 95 L25 140 M85 95 L90 140" stroke="#92400e" stroke-width="8" stroke-linecap="round"/>
       <!-- Head & Expressive Face -->
       <circle cx="35" cy="45" r="20" fill="#78350f"/>
       <circle cx="30" cy="46" r="12" fill="#fed7aa"/>
       <circle cx="27" cy="42" r="3" fill="#000"/>
       <circle cx="35" cy="42" r="3" fill="#000"/>
     </g>
     """),

    (54, "Why the Rhinoceros Has No Horn on His Nose", "Rhinoceros by the Waterhole",
     """
     <defs>
       <linearGradient id="sky54" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdba74"/><stop offset="60%" stop-color="#fed7aa"/><stop offset="100%" stop-color="#fde047"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky54)"/>
     <rect y="310" width="800" height="140" fill="#854d0e"/>
     <!-- Waterhole -->
     <ellipse cx="200" cy="380" rx="160" ry="45" fill="#0284c7"/>
     <!-- Strong Heavy Rhinoceros -->
     <g transform="translate(320, 180)">
       <!-- Body Armor Fold -->
       <ellipse cx="170" cy="100" rx="110" ry="70" fill="#78716c"/>
       <path d="M130 35 Q140 100 135 165" stroke="#57534e" stroke-width="8"/>
       <!-- Sturdy Legs -->
       <rect x="90" y="145" width="30" height="60" rx="6" fill="#57534e"/>
       <rect x="210" y="145" width="30" height="60" rx="6" fill="#57534e"/>
       <!-- Heavy Head -->
       <path d="M85 70 L10 115 L60 145 Z" fill="#78716c"/>
       <!-- Nose with Broken/Missing Horn Stump -->
       <ellipse cx="16" cy="112" rx="8" ry="6" fill="#44403c"/>
       <circle cx="65" cy="85" r="4" fill="#000"/>
       <!-- Small Ears -->
       <polygon points="85,60 92,45 98,62" fill="#57534e"/>
     </g>
     """),

    (55, "Why the Giraffe Has a Long Neck", "Giraffe Browsing Tall Acacias at Sunset",
     """
     <defs>
       <linearGradient id="sunset55" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#c026d3"/><stop offset="40%" stop-color="#ea580c"/><stop offset="80%" stop-color="#facc15"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sunset55)"/>
     <!-- Giant Glowing Sun on Horizon -->
     <circle cx="480" cy="270" r="85" fill="#fef08a" opacity="0.95"/>
     <rect y="340" width="800" height="110" fill="#1c1917"/>
     <!-- Tall Acacia Canopy -->
     <ellipse cx="650" cy="120" rx="110" ry="30" fill="#1c1917"/>
     <path d="M640 340 L650 120" stroke="#1c1917" stroke-width="12"/>
     <!-- Tall Elegant Giraffe Reaching Up -->
     <g transform="translate(320, 60)">
       <!-- Towering Neck -->
       <path d="M90 280 L160 50 L185 55 L135 280 Z" fill="#d97706"/>
       <!-- Giraffe Head & Horns -->
       <polygon points="160,50 190,40 185,60" fill="#d97706"/>
       <line x1="170" y1="42" x2="170" y2="30" stroke="#78350f" stroke-width="4"/>
       <!-- Sloping Body -->
       <ellipse cx="90" cy="280" rx="60" ry="40" fill="#d97706"/>
       <!-- Long Legs -->
       <path d="M60 300 L55 380 M120 300 L125 380" stroke="#b45309" stroke-width="8"/>
       <!-- Patches -->
       <g fill="#78350f" opacity="0.8">
         <rect x="135" y="80" width="16" height="20" rx="4"/>
         <rect x="125" y="120" width="18" height="24" rx="4"/>
         <rect x="115" y="165" width="20" height="26" rx="4"/>
         <rect x="105" y="215" width="22" height="28" rx="4"/>
       </g>
     </g>
     """),

    (56, "Why Owl Flies at Night", "Wise Owl in Starlit Night",
     """
     <defs>
       <linearGradient id="night56" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#020617"/><stop offset="60%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e293b"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#night56)"/>
     <!-- Stars in Sky -->
     <g fill="#f8fafc">
       <circle cx="80" cy="60" r="2"/><circle cx="160" cy="90" r="1.5"/><circle cx="240" cy="50" r="2"/><circle cx="320" cy="110" r="1.5"/><circle cx="480" cy="70" r="2"/><circle cx="680" cy="50" r="2"/><circle cx="740" cy="110" r="1.5"/>
     </g>
     <!-- Silver Crescent Moon -->
     <path d="M640 40 A50 50 0 0 0 680 120 A42 42 0 0 1 640 40 Z" fill="#fef08a"/>
     <!-- Tree Branch -->
     <path d="M100 340 Q400 280 800 320" stroke="#451a03" stroke-width="16" fill="none"/>
     <!-- Perched Owl with Glowing Huge Eyes -->
     <g transform="translate(340, 150)">
       <!-- Body -->
       <ellipse cx="65" cy="110" rx="50" ry="65" fill="#44403c"/>
       <!-- Feathered Chest -->
       <ellipse cx="65" cy="120" rx="32" ry="42" fill="#d6d3d1"/>
       <!-- Feathers V Pattern -->
       <path d="M55 105 L65 115 L75 105 M55 125 L65 135 L75 125" stroke="#78716c" stroke-width="3" fill="none"/>
       <!-- Ear Tufts -->
       <polygon points="30,45 15,20 45,35" fill="#292524"/>
       <polygon points="100,45 115,20 85,35" fill="#292524"/>
       <!-- Giant Yellow Eyes -->
       <circle cx="45" cy="65" r="18" fill="#facc15"/>
       <circle cx="85" cy="65" r="18" fill="#facc15"/>
       <circle cx="45" cy="65" r="9" fill="#000"/>
       <circle cx="85" cy="65" r="9" fill="#000"/>
       <circle cx="48" cy="62" r="3" fill="#fff"/>
       <circle cx="88" cy="62" r="3" fill="#fff"/>
       <!-- Beak -->
       <polygon points="65,70 60,85 70,85" fill="#f97316"/>
     </g>
     """),

    (57, "Why Snake Has No Legs", "Slender Python in Forest Grasses",
     """
     <defs>
       <linearGradient id="sky57" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#14532d"/><stop offset="50%" stop-color="#166534"/><stop offset="100%" stop-color="#4ade80"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky57)"/>
     <rect y="310" width="800" height="140" fill="#713f12"/>
     <!-- Coiled Slithering Snake with Diamond Patterns -->
     <g transform="translate(140, 220)">
       <!-- Curving Body S-Shape -->
       <path d="M50 80 Q150 0 260 80 T480 80 Q540 100 520 130" stroke="#ca8a04" stroke-width="28" fill="none" stroke-linecap="round"/>
       <!-- Diamond Scales Over Body -->
       <path d="M50 80 Q150 0 260 80 T480 80" stroke="#451a03" stroke-width="8" stroke-dasharray="8,8" fill="none"/>
       <!-- Snake Head -->
       <ellipse cx="45" cy="80" rx="20" ry="14" fill="#a16207"/>
       <circle cx="40" cy="74" r="3" fill="#fef08a"/>
       <circle cx="40" cy="74" r="1" fill="#000"/>
       <!-- Forked Tongue -->
       <path d="M25 80 L5 80 M5 80 L-5 72 M5 80 L-5 88" stroke="#dc2626" stroke-width="3" fill="none"/>
     </g>
     <!-- Forest Foliage Leaves -->
     <g fill="#15803d">
       <ellipse cx="100" cy="380" rx="45" ry="18" transform="rotate(-20 100 380)"/>
       <ellipse cx="680" cy="390" rx="55" ry="20" transform="rotate(25 680 390)"/>
     </g>
     """),

    (58, "Why Fish Lives in Water", "Sparkling River Fish Underwater",
     """
     <defs>
       <linearGradient id="water58" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="50%" stop-color="#0284c7"/><stop offset="100%" stop-color="#0c4a6e"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#water58)"/>
     <!-- Sunlight Beams Down Into Water -->
     <polygon points="120,0 220,0 350,450 180,450" fill="#ffffff" opacity="0.12"/>
     <polygon points="400,0 520,0 680,450 500,450" fill="#ffffff" opacity="0.12"/>
     <!-- Riverbed Pebbles -->
     <g fill="#78716c">
       <circle cx="100" cy="430" r="25"/><circle cx="160" cy="435" r="18"/><circle cx="340" cy="440" r="28"/><circle cx="580" cy="430" r="32"/><circle cx="680" cy="438" r="22"/>
     </g>
     <!-- Main Beautiful African Tigerfish / Tilapia -->
     <g transform="translate(300, 170)">
       <!-- Fish Body -->
       <ellipse cx="120" cy="70" rx="85" ry="45" fill="#f59e0b"/>
       <!-- Scales Pattern -->
       <path d="M90 40 Q110 70 90 100 M120 35 Q140 70 120 105 M150 40 Q170 70 150 100" stroke="#b45309" stroke-width="4" fill="none"/>
       <!-- Tail Fin -->
       <polygon points="200,70 260,25 240,70 260,115" fill="#ea580c"/>
       <!-- Top Dorsal Fin -->
       <polygon points="90,26 140,5 170,30" fill="#ea580c"/>
       <!-- Pectoral Fin -->
       <polygon points="80,75 50,105 90,95" fill="#f97316"/>
       <!-- Eye -->
       <circle cx="55" cy="60" r="9" fill="#fef08a"/>
       <circle cx="55" cy="60" r="5" fill="#0c4a6e"/>
     </g>
     <!-- Air Bubbles -->
     <circle cx="280" cy="180" r="6" fill="#bae6fd" opacity="0.7"/>
     <circle cx="260" cy="140" r="4" fill="#bae6fd" opacity="0.7"/>
     <circle cx="270" cy="100" r="8" fill="#bae6fd" opacity="0.7"/>
     """),

    (59, "Why Crab Walks Sideways", "River Crab on Riverbank Stones",
     """
     <defs>
       <linearGradient id="sky59" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdba74"/><stop offset="50%" stop-color="#fed7aa"/><stop offset="100%" stop-color="#93c5fd"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky59)"/>
     <rect y="280" width="800" height="170" fill="#d97706"/>
     <!-- Wet Water Edge -->
     <path d="M0 360 Q400 320 800 370 L800 450 L0 450 Z" fill="#0284c7" opacity="0.8"/>
     <!-- River Crab Walking Sideways with Raised Claws -->
     <g transform="translate(310, 200)">
       <!-- Shell Carapace -->
       <ellipse cx="100" cy="80" rx="60" ry="42" fill="#dc2626"/>
       <!-- Big Left Pincer Claw -->
       <path d="M45 70 Q-10 40 10 0 Q35 25 35 60 Z" fill="#ef4444"/>
       <!-- Big Right Pincer Claw -->
       <path d="M155 70 Q210 40 190 0 Q165 25 165 60 Z" fill="#ef4444"/>
       <!-- Walking Legs on Left and Right -->
       <path d="M50 90 L10 120 M55 100 L20 135 M60 110 L30 148" stroke="#b91c1c" stroke-width="8" stroke-linecap="round"/>
       <path d="M150 90 L190 120 M145 100 L180 135 M140 110 L170 148" stroke="#b91c1c" stroke-width="8" stroke-linecap="round"/>
       <!-- Stalk Eyes -->
       <line x1="85" y1="42" x2="80" y2="22" stroke="#dc2626" stroke-width="6"/>
       <circle cx="80" cy="20" r="7" fill="#fef08a"/>
       <circle cx="80" cy="20" r="3" fill="#000"/>
       <line x1="115" y1="42" x2="120" y2="22" stroke="#dc2626" stroke-width="6"/>
       <circle cx="120" cy="20" r="7" fill="#fef08a"/>
       <circle cx="120" cy="20" r="3" fill="#000"/>
     </g>
     """),

    (60, "Why Chameleon Changes Colour", "Chameleon Changing Colour on Branch",
     """
     <defs>
       <linearGradient id="chamGrad60" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#10b981"/><stop offset="50%" stop-color="#f59e0b"/><stop offset="100%" stop-color="#ef4444"/></linearGradient>
       <linearGradient id="sky60" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0284c7"/><stop offset="60%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#bbf7d0"/></linearGradient>
     </defs>
     <rect width="800" height="450" fill="url(#sky60)"/>
     <!-- Slanted Branch -->
     <path d="M50 360 Q350 250 750 180" stroke="#78350f" stroke-width="20" fill="none" stroke-linecap="round"/>
     <!-- Colorful Leaves -->
     <ellipse cx="680" cy="150" rx="35" ry="16" fill="#15803d" transform="rotate(-30 680 150)"/>
     <ellipse cx="620" cy="180" rx="35" ry="16" fill="#eab308" transform="rotate(20 620 180)"/>
     <!-- Chameleon on Branch -->
     <g transform="translate(240, 130)">
       <!-- Coiled Spiral Tail -->
       <path d="M60 110 C-10 110 -10 170 30 170 C60 170 60 140 40 140" stroke="#10b981" stroke-width="12" fill="none" stroke-linecap="round"/>
       <!-- Gradient Color-Changing Body -->
       <ellipse cx="140" cy="95" rx="75" ry="40" fill="url(#chamGrad60)"/>
       <!-- Casque / Crest on Head -->
       <path d="M190 70 L240 60 L230 100 Z" fill="#ef4444"/>
       <!-- Turret Eye Rotating -->
       <circle cx="215" cy="80" r="14" fill="#facc15"/>
       <circle cx="218" cy="78" r="4" fill="#000"/>
       <!-- Zygodactylous Feet Gripping Branch -->
       <path d="M100 120 L90 155 M170 115 L180 145" stroke="#059669" stroke-width="10" stroke-linecap="round"/>
     </g>
     """)
]

def generate_svg(id_num, title, subtitle, inner_content):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="800" height="450">
  <defs>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.3"/>
    </filter>
  </defs>
  {inner_content}
  <!-- Title Badge Overlay -->
  <g transform="translate(24, 24)">
    <rect width="360" height="62" rx="10" fill="rgba(24, 57, 52, 0.88)" filter="url(#shadow)"/>
    <text x="18" y="24" font-family="Ubuntu, sans-serif" font-size="12" font-weight="700" fill="#f59e0b" letter-spacing="1.5">CHAPTER {id_num} &middot; LANSDOWN TALES</text>
    <text x="18" y="48" font-family="Ubuntu, sans-serif" font-size="18" font-weight="700" fill="#ffffff">{title}</text>
  </g>
</svg>
"""

def main():
    print(f"Generating {len(STORIES)} illustrated story SVGs...")
    for story_id, title, subtitle, content in STORIES:
        svg_code = generate_svg(story_id, title, subtitle, content)
        filename = f"story-{str(story_id).padStart(2, '0') if hasattr(str(story_id), 'padStart') else str(story_id).zfill(2)}.svg"
        for d in DEST_DIRS:
            d.mkdir(parents=True, exist_ok=True)
            out_file = d / filename
            out_file.write_text(svg_code, encoding="utf-8")
        print(f"  [OK] Created {filename}: {title}")

if __name__ == "__main__":
    main()
