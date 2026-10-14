import sys
from pathlib import Path

DEST_DIRS = [
    Path(r"c:\folk_tale_stories\outputs\kalulu-reader\assets\covers"),
    Path(r"c:\folk_tale_stories\outputs\kalulu-android\www\assets\covers")
]

STORIES = [
    (
        41,
        "Why the Lion Roars",
        "How Lion Lost His Gentle Voice to the Furious Bees",
        """
        <linearGradient id="sky41" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdba74"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky41)"/>
        <rect y="310" width="800" height="140" fill="#78350f"/>
        <!-- Baobab Tree -->
        <path d="M540 340 C520 220 560 140 640 100 C720 140 760 220 740 340 Z" fill="#451a03"/>
        <ellipse cx="640" cy="90" rx="130" ry="70" fill="#15803d"/>
        <!-- Honeycomb Hollow -->
        <ellipse cx="635" cy="190" rx="28" ry="38" fill="#1c1917"/>
        <ellipse cx="635" cy="190" rx="20" ry="28" fill="#eab308"/>
        <!-- Sleeping Lion -->
        <g transform="translate(180, 220)">
          <!-- Lion Body -->
          <ellipse cx="160" cy="95" rx="100" ry="55" fill="#d97706"/>
          <!-- Legs -->
          <rect x="75" y="120" width="28" height="40" rx="8" fill="#b45309"/>
          <rect x="210" y="120" width="28" height="40" rx="8" fill="#b45309"/>
          <!-- Thick Dark Mane -->
          <circle cx="80" cy="65" r="58" fill="#78350f"/>
          <!-- Lion Head -->
          <circle cx="80" cy="65" r="38" fill="#d97706"/>
          <!-- Eyes sleeping & muzzle -->
          <path d="M68 62 Q75 66 82 62" stroke="#451a03" stroke-width="3" fill="none"/>
          <ellipse cx="60" cy="74" rx="12" ry="8" fill="#fde68a"/>
          <circle cx="56" cy="72" r="4" fill="#1c1917"/>
          <path d="M260 95 Q290 80 280 60" stroke="#d97706" stroke-width="8" stroke-linecap="round" fill="none"/>
        </g>
        <!-- Swarming Angry Bees -->
        <g fill="#eab308" stroke="#1c1917" stroke-width="2">
          <ellipse cx="480" cy="180" rx="10" ry="6"/><circle cx="488" cy="180" r="3" fill="#38bdf8"/>
          <ellipse cx="510" cy="160" rx="9" ry="5"/><circle cx="517" cy="160" r="3" fill="#38bdf8"/>
          <ellipse cx="450" cy="210" rx="11" ry="7"/><circle cx="458" cy="210" r="3" fill="#38bdf8"/>
          <ellipse cx="420" cy="170" rx="8" ry="5"/><circle cx="426" cy="170" r="3" fill="#38bdf8"/>
          <ellipse cx="380" cy="230" rx="10" ry="6"/><circle cx="388" cy="230" r="3" fill="#38bdf8"/>
          <ellipse cx="350" cy="190" rx="9" ry="5"/><circle cx="357" cy="190" r="3" fill="#38bdf8"/>
        </g>
        """
    ),
    (
        42,
        "Why Ostrich Has a Long Neck",
        "The River Tug-of-War Between Ostrich and Crocodile",
        """
        <linearGradient id="sky42" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#bae6fd"/><stop offset="100%" stop-color="#e0f2fe"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky42)"/>
        <!-- River and Bank -->
        <path d="M0 260 Q400 300 800 240 L800 450 L0 450 Z" fill="#0284c7"/>
        <rect y="350" width="440" height="100" fill="#eab308"/>
        <!-- Crocodile in River clamping Ostrich -->
        <g transform="translate(460, 260)">
          <!-- Snout & Teeth -->
          <polygon points="0,40 160,10 170,55 0,65" fill="#15803d"/>
          <polygon points="40,43 55,50 50,56" fill="#fff"/>
          <polygon points="80,36 95,44 90,50" fill="#fff"/>
          <polygon points="120,29 135,37 130,44" fill="#fff"/>
          <!-- Eye ridge -->
          <circle cx="140" cy="18" r="14" fill="#166534"/>
          <circle cx="140" cy="18" r="6" fill="#facc15"/>
          <circle cx="140" cy="18" r="3" fill="#000"/>
          <!-- Scaled Body submerged -->
          <path d="M160 30 Q260 20 320 60 L300 120 L150 100 Z" fill="#14532d"/>
        </g>
        <!-- Stretched Ostrich pulling back -->
        <g transform="translate(140, 160)">
          <!-- Plump Feathered Body -->
          <ellipse cx="90" cy="140" rx="65" ry="48" fill="#18181b"/>
          <circle cx="90" cy="140" r="38" fill="#27272a"/>
          <!-- Stretched Strong Legs leaning back -->
          <line x1="70" y1="180" x2="40" y2="250" stroke="#f59e0b" stroke-width="10" stroke-linecap="round"/>
          <line x1="110" y1="180" x2="80" y2="250" stroke="#f59e0b" stroke-width="10" stroke-linecap="round"/>
          <!-- Extremely Long Stretched Neck -->
          <path d="M140 120 C230 110 280 135 340 142" fill="none" stroke="#fbcfe8" stroke-width="22" stroke-linecap="round"/>
          <!-- Ostrich Head pulling desperately -->
          <circle cx="345" cy="142" r="18" fill="#f472b6"/>
          <circle cx="342" cy="138" r="4" fill="#000"/>
          <polygon points="358,136 385,142 358,148" fill="#f59e0b"/>
        </g>
        """
    ),
    (
        43,
        "Why Chickens Scratch the Ground",
        "Searching Constantly for the Hawk's Lost Needle",
        """
        <linearGradient id="sky43" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky43)"/>
        <rect y="290" width="800" height="160" fill="#a16207"/>
        <circle cx="680" cy="90" r="50" fill="#f97316" opacity="0.3"/>
        <!-- Flying Hawk overhead -->
        <g transform="translate(560, 80)">
          <path d="M0 30 Q60 -10 120 30 Q60 15 0 30 Z" fill="#451a03"/>
          <circle cx="60" cy="28" r="8" fill="#78350f"/>
        </g>
        <!-- Mother Hen Scratching Ground -->
        <g transform="translate(240, 190)">
          <!-- Body -->
          <ellipse cx="140" cy="100" rx="80" ry="60" fill="#dc2626"/>
          <!-- Wing -->
          <ellipse cx="145" cy="105" rx="50" ry="35" fill="#b91c1c"/>
          <!-- Tail feathers fanned -->
          <path d="M200 80 L260 40 L250 80 L270 70 L250 100 Z" fill="#991b1b"/>
          <!-- Head & Red Comb -->
          <circle cx="70" cy="75" r="30" fill="#ef4444"/>
          <path d="M60 48 Q70 30 80 48 Q90 32 95 52 Z" fill="#b91c1c"/>
          <!-- Beak pointing down to ground -->
          <polygon points="45,75 25,85 48,90" fill="#facc15"/>
          <circle cx="62" cy="70" r="4" fill="#000"/>
          <!-- Feet Scratching Claws kicking dust -->
          <line x1="120" y1="150" x2="95" y2="200" stroke="#f59e0b" stroke-width="8" stroke-linecap="round"/>
          <line x1="160" y1="150" x2="175" y2="200" stroke="#f59e0b" stroke-width="8" stroke-linecap="round"/>
          <!-- Dust clouds -->
          <circle cx="85" cy="205" r="16" fill="#fde047" opacity="0.6"/>
          <circle cx="65" cy="200" r="10" fill="#fde047" opacity="0.4"/>
          <circle cx="195" cy="205" r="12" fill="#fde047" opacity="0.5"/>
        </g>
        <!-- Tiny glittering sewing needle on ground -->
        <line x1="190" y1="410" x2="225" y2="400" stroke="#f8fafc" stroke-width="4" stroke-linecap="round"/>
        <circle cx="192" cy="409" r="2" fill="#0f172a"/>
        <circle cx="210" cy="405" r="6" fill="#fff" opacity="0.7"/>
        """
    ),
    (
        44,
        "Why Frog Says Croack-Croack",
        "The Boiling Porridge that Changed Frog's Clear Voice",
        """
        <linearGradient id="sky44" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#a7f3d0"/><stop offset="100%" stop-color="#ccfbf1"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky44)"/>
        <!-- River Marsh & Lily Pads -->
        <rect y="280" width="800" height="170" fill="#065f46"/>
        <ellipse cx="260" cy="380" rx="90" ry="30" fill="#047857"/>
        <ellipse cx="580" cy="360" rx="110" ry="35" fill="#047857"/>
        <!-- Hot Clay Pot with Steam -->
        <g transform="translate(140, 240)">
          <ellipse cx="70" cy="90" rx="55" ry="35" fill="#78350f"/>
          <ellipse cx="70" cy="65" rx="42" ry="14" fill="#fbbf24"/>
          <!-- Steam trails -->
          <path d="M50 50 Q40 20 60 5" stroke="#f8fafc" stroke-width="4" fill="none" opacity="0.7"/>
          <path d="M70 50 Q85 20 70 5" stroke="#f8fafc" stroke-width="4" fill="none" opacity="0.7"/>
          <path d="M90 50 Q80 20 95 5" stroke="#f8fafc" stroke-width="4" fill="none" opacity="0.7"/>
        </g>
        <!-- Large Green Frog with Puffed Throat -->
        <g transform="translate(420, 180)">
          <!-- Back legs -->
          <ellipse cx="70" cy="150" rx="45" ry="25" fill="#15803d"/>
          <ellipse cx="200" cy="150" rx="45" ry="25" fill="#15803d"/>
          <!-- Body -->
          <ellipse cx="135" cy="120" rx="75" ry="60" fill="#22c55e"/>
          <!-- Huge Puffed Vocal Throat -->
          <circle cx="95" cy="130" r="46" fill="#86efac"/>
          <!-- Big Frog Eyes -->
          <circle cx="100" cy="65" r="24" fill="#22c55e"/>
          <circle cx="100" cy="65" r="14" fill="#facc15"/>
          <circle cx="100" cy="65" r="7" fill="#000"/>
          <circle cx="160" cy="65" r="24" fill="#22c55e"/>
          <circle cx="160" cy="65" r="14" fill="#facc15"/>
          <circle cx="160" cy="65" r="7" fill="#000"/>
          <!-- Wide Open Mouth Saying CROAK -->
          <ellipse cx="115" cy="100" rx="35" ry="18" fill="#14532d"/>
        </g>
        """
    ),
    (
        45,
        "Why the Hyena Laughs",
        "Hyena's Boastful Grin Across the Open Plains",
        """
        <linearGradient id="sky45" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdba74"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky45)"/>
        <rect y="290" width="800" height="160" fill="#a16207"/>
        <circle cx="180" cy="120" r="45" fill="#fef08a" opacity="0.6"/>
        <!-- Sloping Savanna Ridge -->
        <path d="M0 320 Q400 280 800 310 L800 450 L0 450 Z" fill="#78350f"/>
        <!-- Spotted Laughing Hyena -->
        <g transform="translate(300, 160)">
          <!-- Sloping Body -->
          <path d="M80 80 L220 120 L200 170 L70 150 Z" fill="#a8a29e"/>
          <circle cx="140" cy="115" r="50" fill="#a8a29e"/>
          <!-- Hyena Spots -->
          <circle cx="120" cy="110" r="7" fill="#44403c"/>
          <circle cx="150" cy="100" r="8" fill="#44403c"/>
          <circle cx="170" cy="125" r="6" fill="#44403c"/>
          <circle cx="140" cy="135" r="7" fill="#44403c"/>
          <!-- High Shoulders, Lower Hindquarters -->
          <rect x="75" y="145" width="22" height="65" rx="6" fill="#78716c"/>
          <rect x="180" y="145" width="20" height="50" rx="6" fill="#78716c"/>
          <!-- Head with Wide Grinning Open Mouth -->
          <circle cx="65" cy="80" r="42" fill="#a8a29e"/>
          <!-- Big Rounded Ears -->
          <circle cx="85" cy="45" r="18" fill="#57534e"/>
          <circle cx="50" cy="48" r="16" fill="#57534e"/>
          <!-- Gaping Laughing Jaws with Teeth -->
          <path d="M35 85 Q70 80 85 105 Q55 118 35 85 Z" fill="#1c1917"/>
          <polygon points="40,86 46,94 52,86" fill="#fff"/>
          <polygon points="56,86 62,94 68,86" fill="#fff"/>
          <polygon points="45,108 50,100 55,108" fill="#fff"/>
          <!-- Mischievous Eye -->
          <circle cx="58" cy="72" r="5" fill="#facc15"/>
          <circle cx="58" cy="72" r="2" fill="#000"/>
        </g>
        """
    ),
    (
        46,
        "Why the Hare Drinks Dew",
        "Clever Kalulu Sipping Morning Dew From Forest Leaves",
        """
        <linearGradient id="sky46" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#bae6fd"/><stop offset="100%" stop-color="#fbcfe8"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky46)"/>
        <rect y="310" width="800" height="140" fill="#15803d"/>
        <!-- Large Green Leaves Overhanging with Sparkling Dew -->
        <g transform="translate(100, 80)">
          <path d="M0 80 Q150 10 320 70 Q160 130 0 80 Z" fill="#16a34a"/>
          <path d="M120 75 Q260 20 400 90 Q250 150 120 75 Z" fill="#22c55e"/>
          <!-- Dew Drops sparkling -->
          <circle cx="240" cy="80" r="12" fill="#38bdf8" opacity="0.85"/>
          <circle cx="237" cy="76" r="4" fill="#fff"/>
          <circle cx="340" cy="95" r="16" fill="#38bdf8" opacity="0.85"/>
          <circle cx="335" cy="90" r="5" fill="#fff"/>
        </g>
        <!-- Hare Reaching Up to Sip -->
        <g transform="translate(380, 180)">
          <!-- Body standing on hind legs -->
          <ellipse cx="100" cy="130" rx="55" ry="70" fill="#d97706"/>
          <circle cx="100" cy="140" r="45" fill="#fef3c7"/>
          <!-- Tail -->
          <circle cx="155" cy="170" r="16" fill="#fff"/>
          <!-- Head tilted up -->
          <circle cx="80" cy="60" r="32" fill="#d97706"/>
          <!-- Long Upright Ears -->
          <ellipse cx="65" cy="5" rx="10" ry="38" fill="#d97706" transform="rotate(-10 65 5)"/>
          <ellipse cx="65" cy="5" rx="5" ry="28" fill="#f472b6" transform="rotate(-10 65 5)"/>
          <ellipse cx="90" cy="10" rx="10" ry="38" fill="#d97706" transform="rotate(10 90 10)"/>
          <ellipse cx="90" cy="10" rx="5" ry="28" fill="#f472b6" transform="rotate(10 90 10)"/>
          <!-- Tiny nose touching dewdrops -->
          <circle cx="60" cy="50" r="4" fill="#f43f5e"/>
          <circle cx="75" cy="52" r="5" fill="#000"/>
        </g>
        """
    ),
    (
        47,
        "How Hippo Lost His Horns",
        "The Magnificent Golden Horns Lost to the River Depths",
        """
        <linearGradient id="sky47" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdba74"/><stop offset="100%" stop-color="#fde047"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky47)"/>
        <!-- River Water -->
        <rect y="270" width="800" height="180" fill="#0284c7"/>
        <path d="M0 270 Q200 250 400 270 T800 270 L800 450 L0 450 Z" fill="#0369a1"/>
        <!-- Hippo Submerged with Horns -->
        <g transform="translate(260, 160)">
          <!-- Massive Head Emerging -->
          <ellipse cx="140" cy="130" rx="110" ry="75" fill="#6b7280"/>
          <!-- Snout with Nostrils -->
          <ellipse cx="80" cy="155" rx="60" ry="40" fill="#4b5563"/>
          <circle cx="60" cy="145" r="9" fill="#1f2937"/>
          <circle cx="95" cy="145" r="9" fill="#1f2937"/>
          <!-- Eyes Above Water -->
          <circle cx="160" cy="85" r="18" fill="#4b5563"/>
          <circle cx="160" cy="85" r="7" fill="#1f2937"/>
          <circle cx="120" cy="85" r="18" fill="#4b5563"/>
          <circle cx="120" cy="85" r="7" fill="#1f2937"/>
          <!-- Magnificent Golden Horns on Brow -->
          <path d="M125 70 Q110 10 90 -20 Q120 15 135 68 Z" fill="#eab308"/>
          <path d="M165 70 Q175 10 200 -20 Q175 15 155 68 Z" fill="#eab308"/>
          <!-- Water Ripples -->
          <ellipse cx="140" cy="180" rx="150" ry="25" fill="none" stroke="#bae6fd" stroke-width="6"/>
        </g>
        """
    ),
    (
        48,
        "Why the Hyena Walks with a Limp",
        "The Cunning Trap that Sprained Hyena's Hind Leg",
        """
        <linearGradient id="sky48" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fca5a5"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky48)"/>
        <rect y="310" width="800" height="140" fill="#78350f"/>
        <!-- Thorny Bush & Snare Tree -->
        <path d="M120 330 L160 120 L180 120 L160 330 Z" fill="#451a03"/>
        <path d="M160 160 Q260 120 340 180" fill="none" stroke="#451a03" stroke-width="12" stroke-linecap="round"/>
        <!-- Limping Hyena hobbling forward -->
        <g transform="translate(320, 180)">
          <!-- Sloping Body -->
          <ellipse cx="160" cy="90" rx="85" ry="50" fill="#78716c"/>
          <!-- Spots -->
          <circle cx="140" cy="80" r="7" fill="#292524"/>
          <circle cx="175" cy="85" r="8" fill="#292524"/>
          <circle cx="195" cy="100" r="6" fill="#292524"/>
          <!-- Strong Front Leg -->
          <rect x="95" y="125" width="24" height="65" rx="6" fill="#57534e"/>
          <!-- Injured Hind Leg lifted up in bandage/pain -->
          <path d="M205 125 L230 160 L210 165" stroke="#dc2626" stroke-width="14" stroke-linecap="round" fill="none"/>
          <!-- Head drooping in pain -->
          <circle cx="70" cy="70" r="36" fill="#78716c"/>
          <circle cx="55" cy="65" r="4" fill="#000"/>
          <polygon points="40,70 20,80 40,86" fill="#44403c"/>
          <circle cx="85" cy="40" r="14" fill="#57534e"/>
        </g>
        """
    ),
    (
        49,
        "How Birds Learned to Speak",
        "The Forest Assembly Where Feathers Found Their Songs",
        """
        <linearGradient id="sky49" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#bae6fd"/><stop offset="100%" stop-color="#fef08a"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky49)"/>
        <rect y="330" width="800" height="120" fill="#15803d"/>
        <!-- Great Baobab Branch Across Canvas -->
        <path d="M0 240 Q400 200 800 230 L800 280 Q400 250 0 290 Z" fill="#78350f"/>
        <!-- Colorful Singing Birds On Branch -->
        <!-- Bluebird -->
        <g transform="translate(180, 140)">
          <ellipse cx="40" cy="50" rx="30" ry="20" fill="#0284c7"/>
          <circle cx="20" cy="40" r="15" fill="#38bdf8"/>
          <polygon points="10,40 -4,44 10,48" fill="#f59e0b"/>
          <circle cx="18" cy="36" r="3" fill="#000"/>
          <!-- Musical note -->
          <text x="-10" y="15" font-size="28" fill="#0284c7">&#9835;</text>
        </g>
        <!-- Golden Oriole Singing -->
        <g transform="translate(380, 110)">
          <ellipse cx="50" cy="60" rx="36" ry="24" fill="#eab308"/>
          <circle cx="25" cy="45" r="18" fill="#facc15"/>
          <polygon points="12,45 -6,50 12,55" fill="#f97316"/>
          <circle cx="22" cy="42" r="3" fill="#000"/>
          <text x="-12" y="20" font-size="34" fill="#eab308">&#9834;</text>
        </g>
        <!-- Crimson Weaver Bird -->
        <g transform="translate(560, 130)">
          <ellipse cx="40" cy="50" rx="28" ry="20" fill="#dc2626"/>
          <circle cx="20" cy="40" r="15" fill="#ef4444"/>
          <polygon points="10,40 -2,44 10,48" fill="#1c1917"/>
          <circle cx="18" cy="37" r="3" fill="#fff"/>
          <text x="-8" y="18" font-size="28" fill="#dc2626">&#9835;</text>
        </g>
        """
    ),
    (
        50,
        "Why Fish Live in Water",
        "Finding Peace and Shelter in the Deep Mountain Rivers",
        """
        <linearGradient id="sky50" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0369a1"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky50)"/>
        <!-- Riverbed Rocks & Seaweed -->
        <path d="M0 380 Q400 350 800 390 L800 450 L0 450 Z" fill="#0f172a"/>
        <path d="M120 400 Q140 280 120 200" stroke="#10b981" stroke-width="12" stroke-linecap="round" fill="none"/>
        <path d="M680 400 Q660 260 690 180" stroke="#10b981" stroke-width="12" stroke-linecap="round" fill="none"/>
        <!-- Golden Fish Swimming Freely -->
        <g transform="translate(300, 160)">
          <!-- Sleek Fish Body -->
          <path d="M40 80 Q140 20 220 80 Q140 140 40 80 Z" fill="#f59e0b"/>
          <path d="M70 80 Q140 40 190 80 Q140 120 70 80 Z" fill="#fbbf24"/>
          <!-- Tail Fin -->
          <polygon points="220,80 270,40 255,80 270,120" fill="#ea580c"/>
          <!-- Dorsal and Ventral Fins -->
          <polygon points="120,45 160,20 170,45" fill="#ea580c"/>
          <polygon points="120,115 150,135 160,115" fill="#ea580c"/>
          <!-- Gills and Eye -->
          <circle cx="80" cy="72" r="7" fill="#fff"/>
          <circle cx="78" cy="72" r="4" fill="#000"/>
          <path d="M110 65 Q95 80 110 95" stroke="#d97706" stroke-width="4" fill="none"/>
          <!-- Bubbles -->
          <circle cx="45" cy="60" r="8" fill="none" stroke="#bae6fd" stroke-width="2"/>
          <circle cx="30" cy="40" r="6" fill="none" stroke="#bae6fd" stroke-width="2"/>
          <circle cx="18" cy="22" r="4" fill="none" stroke="#bae6fd" stroke-width="2"/>
        </g>
        """
    ),
    (
        51,
        "Why Porcupine Has Spikes",
        "The Sharp Defensive Quills Bestowed for Protection",
        """
        <linearGradient id="sky51" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fed7aa"/><stop offset="100%" stop-color="#fdba74"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky51)"/>
        <rect y="310" width="800" height="140" fill="#78350f"/>
        <!-- Proud Porcupine with Radiating Quills -->
        <g transform="translate(240, 140)">
          <!-- Fan of Sharp Black-and-White Quills -->
          <g stroke="#18181b" stroke-width="5" stroke-linecap="round">
            <line x1="160" y1="140" x2="280" y2="20" stroke="#f8fafc" stroke-width="7"/>
            <line x1="160" y1="140" x2="280" y2="20" stroke="#18181b" stroke-dasharray="14 14"/>
            <line x1="160" y1="140" x2="310" y2="50" stroke="#f8fafc" stroke-width="7"/>
            <line x1="160" y1="140" x2="310" y2="50" stroke="#18181b" stroke-dasharray="14 14"/>
            <line x1="160" y1="140" x2="330" y2="90" stroke="#f8fafc" stroke-width="7"/>
            <line x1="160" y1="140" x2="330" y2="90" stroke="#18181b" stroke-dasharray="14 14"/>
            <line x1="160" y1="140" x2="340" y2="140" stroke="#f8fafc" stroke-width="7"/>
            <line x1="160" y1="140" x2="340" y2="140" stroke="#18181b" stroke-dasharray="14 14"/>
            <line x1="160" y1="140" x2="320" y2="180" stroke="#f8fafc" stroke-width="7"/>
            <line x1="160" y1="140" x2="320" y2="180" stroke="#18181b" stroke-dasharray="14 14"/>
            <line x1="160" y1="140" x2="240" y2="10" stroke="#f8fafc" stroke-width="7"/>
            <line x1="160" y1="140" x2="240" y2="10" stroke="#18181b" stroke-dasharray="14 14"/>
          </g>
          <!-- Body and Head -->
          <ellipse cx="140" cy="150" rx="75" ry="50" fill="#292524"/>
          <circle cx="75" cy="150" r="35" fill="#44403c"/>
          <circle cx="50" cy="150" r="6" fill="#000"/>
          <circle cx="68" cy="140" r="4" fill="#facc15"/>
          <!-- Sturdy Claws -->
          <rect x="85" y="190" width="18" height="35" rx="5" fill="#1c1917"/>
          <rect x="150" y="190" width="18" height="35" rx="5" fill="#1c1917"/>
        </g>
        """
    ),
    (
        52,
        "Why the Owl Flies at Night",
        "The Wise Judge Who Soars Beneath the Stars",
        """
        <linearGradient id="sky52" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e1b4b"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky52)"/>
        <!-- Golden Crescent Moon & Stars -->
        <path d="M680 70 A40 40 0 1 0 710 135 A48 48 0 1 1 680 70 Z" fill="#facc15"/>
        <g fill="#fff" opacity="0.8">
          <circle cx="120" cy="60" r="2.5"/><circle cx="240" cy="90" r="2"/><circle cx="360" cy="50" r="3"/>
          <circle cx="480" cy="100" r="2.5"/><circle cx="580" cy="40" r="2"/><circle cx="180" cy="150" r="2"/>
        </g>
        <!-- Baobab Silhouette -->
        <path d="M0 340 L180 260 L240 450 L0 450 Z" fill="#020617"/>
        <!-- Great Horned Owl Flying with Outstretched Wings -->
        <g transform="translate(300, 140)">
          <!-- Left and Right Wide Wings -->
          <path d="M90 70 C0 30 -60 70 -90 120 C-30 110 30 100 90 70 Z" fill="#78350f"/>
          <path d="M130 70 C220 30 280 70 310 120 C250 110 190 100 130 70 Z" fill="#78350f"/>
          <!-- Owl Body -->
          <ellipse cx="110" cy="100" rx="42" ry="55" fill="#9a3412"/>
          <ellipse cx="110" cy="110" rx="28" ry="40" fill="#fed7aa"/>
          <!-- Head and Feather Tufts (Horns) -->
          <circle cx="110" cy="55" r="34" fill="#9a3412"/>
          <polygon points="85,35 75,10 100,28" fill="#78350f"/>
          <polygon points="135,35 145,10 120,28" fill="#78350f"/>
          <!-- Great Luminous Yellow Eyes -->
          <circle cx="96" cy="55" r="14" fill="#facc15"/>
          <circle cx="96" cy="55" r="6" fill="#000"/>
          <circle cx="124" cy="55" r="14" fill="#facc15"/>
          <circle cx="124" cy="55" r="6" fill="#000"/>
          <!-- Sharp Beak -->
          <polygon points="110,62 104,74 116,74" fill="#f59e0b"/>
        </g>
        """
    ),
    (
        53,
        "Why Tortoise Has a Hard Back",
        "The Protective Shell Carved to Shield Slow Tortoise",
        """
        <linearGradient id="sky53" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#bae6fd"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky53)"/>
        <rect y="310" width="800" height="140" fill="#a16207"/>
        <!-- Tortoise Walking Steadily -->
        <g transform="translate(260, 180)">
          <!-- Four Stubby Feet -->
          <ellipse cx="70" cy="150" rx="22" ry="14" fill="#65a30d"/>
          <ellipse cx="180" cy="150" rx="22" ry="14" fill="#65a30d"/>
          <!-- Tail -->
          <polygon points="210,135 240,140 210,145" fill="#65a30d"/>
          <!-- Heavy Hard Domed Shell -->
          <path d="M40 140 C40 40 210 40 210 140 Z" fill="#854d0e"/>
          <!-- Geometric Carved Shell Pattern Plates -->
          <polygon points="125,55 95,85 105,120 145,120 155,85" fill="#ca8a04" stroke="#451a03" stroke-width="4"/>
          <polygon points="95,85 60,95 70,135 105,120" fill="#a16207" stroke="#451a03" stroke-width="4"/>
          <polygon points="155,85 190,95 180,135 145,120" fill="#a16207" stroke="#451a03" stroke-width="4"/>
          <!-- Head with Wise Smile -->
          <ellipse cx="25" cy="125" rx="26" ry="18" fill="#65a30d"/>
          <circle cx="18" cy="120" r="4" fill="#000"/>
        </g>
        """
    ),
    (
        54,
        "Why the Cat and Dog Quarrel",
        "The Feast Left on the Table and the Broken Trust",
        """
        <linearGradient id="sky54" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fed7aa"/><stop offset="100%" stop-color="#fde047"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky54)"/>
        <!-- Wooden House Interior Floor -->
        <rect y="290" width="800" height="160" fill="#78350f"/>
        <!-- Wooden Table with Stolen Meat Plate -->
        <rect x="220" y="210" width="360" height="24" rx="4" fill="#9a3412"/>
        <rect x="250" y="234" width="22" height="130" fill="#78350f"/>
        <rect x="520" y="234" width="22" height="130" fill="#78350f"/>
        <!-- Bone & Plate on Table -->
        <ellipse cx="400" cy="205" rx="60" ry="15" fill="#f8fafc"/>
        <path d="M380 200 L420 200" stroke="#dc2626" stroke-width="12" stroke-linecap="round"/>
        <!-- Sly Cat on Top of Table Eating Meat -->
        <g transform="translate(420, 100)">
          <ellipse cx="60" cy="80" rx="36" ry="24" fill="#ea580c"/>
          <circle cx="28" cy="65" r="18" fill="#ea580c"/>
          <polygon points="18,52 24,35 32,52" fill="#9a3412"/>
          <polygon points="30,52 38,35 44,52" fill="#9a3412"/>
          <circle cx="22" cy="62" r="3" fill="#22c55e"/>
          <!-- Swishing Tail -->
          <path d="M96 80 Q130 60 120 40" stroke="#ea580c" stroke-width="8" stroke-linecap="round" fill="none"/>
        </g>
        <!-- Angry Dog on Ground Barking at Cat -->
        <g transform="translate(100, 220)">
          <!-- Dog Body -->
          <ellipse cx="90" cy="80" rx="60" ry="40" fill="#451a03"/>
          <rect x="55" y="110" width="18" height="45" rx="6" fill="#292524"/>
          <rect x="115" y="110" width="18" height="45" rx="6" fill="#292524"/>
          <!-- Dog Head barking up -->
          <circle cx="150" cy="50" r="30" fill="#451a03"/>
          <ellipse cx="140" cy="30" rx="10" ry="20" fill="#292524"/>
          <polygon points="170,40 195,50 170,65" fill="#f59e0b"/>
          <circle cx="150" cy="42" r="4" fill="#fff"/>
          <circle cx="152" cy="42" r="2" fill="#000"/>
        </g>
        """
    ),
    (
        55,
        "Why the Elephant Fears the Mouse",
        "The Giant of the Savannah Startled by the Smallest Friend",
        """
        <linearGradient id="sky55" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdba74"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky55)"/>
        <rect y="310" width="800" height="140" fill="#854d0e"/>
        <!-- Giant Mighty Elephant -->
        <g transform="translate(120, 80)">
          <!-- Huge Body -->
          <ellipse cx="260" cy="170" rx="190" ry="130" fill="#64748b"/>
          <!-- Massive Tree-Trunk Legs -->
          <rect x="120" y="240" width="55" height="110" rx="12" fill="#475569"/>
          <rect x="230" y="240" width="55" height="110" rx="12" fill="#475569"/>
          <rect x="340" y="240" width="55" height="110" rx="12" fill="#475569"/>
          <!-- Head and Huge Flapping Ear -->
          <circle cx="95" cy="150" r="75" fill="#64748b"/>
          <ellipse cx="130" cy="150" rx="45" ry="65" fill="#475569"/>
          <!-- Curious Curved Trunk lifting in surprise -->
          <path d="M45 160 C0 210 10 270 45 280 C65 285 60 260 45 250 C25 240 25 200 65 175 Z" fill="#64748b"/>
          <!-- Small Watchful Eye and White Tusk -->
          <circle cx="70" cy="135" r="6" fill="#facc15"/>
          <circle cx="70" cy="135" r="3" fill="#000"/>
          <path d="M75 195 Q30 220 20 200 Q45 190 75 185 Z" fill="#f8fafc"/>
        </g>
        <!-- Tiny Brave Mouse on the Ground Looking Up -->
        <g transform="translate(620, 340)">
          <!-- Mouse Body -->
          <ellipse cx="40" cy="35" rx="26" ry="16" fill="#78716c"/>
          <!-- Round Ears -->
          <circle cx="28" cy="22" r="10" fill="#a8a29e"/>
          <circle cx="28" cy="22" r="5" fill="#f472b6"/>
          <!-- Pointed Snout and Whiskers -->
          <polygon points="16,32 0,38 18,42" fill="#78716c"/>
          <circle cx="1" cy="38" r="3" fill="#000"/>
          <circle cx="16" cy="32" r="3" fill="#000"/>
          <!-- Long Curled Tail -->
          <path d="M66 35 Q105 20 100 50" stroke="#f472b6" stroke-width="3" fill="none"/>
        </g>
        """
    ),
    (
        56,
        "Why the Giraffe Has a Long Neck",
        "Reaching Above the Savannah into the High Baobab Canopy",
        """
        <linearGradient id="sky56" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#67e8f9"/><stop offset="100%" stop-color="#fef08a"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky56)"/>
        <rect y="330" width="800" height="120" fill="#a16207"/>
        <!-- Tall Baobab Foliage at Top Right -->
        <path d="M620 450 L640 180 L680 180 L700 450 Z" fill="#451a03"/>
        <ellipse cx="660" cy="120" rx="140" ry="70" fill="#15803d"/>
        <!-- Tall Majestic Giraffe -->
        <g transform="translate(240, 40)">
          <!-- Body -->
          <ellipse cx="140" cy="260" rx="80" ry="55" fill="#f59e0b"/>
          <!-- Long Slender Legs -->
          <rect x="90" y="300" width="16" height="130" fill="#d97706"/>
          <rect x="170" y="300" width="16" height="130" fill="#d97706"/>
          <!-- Tall Graceful Neck reaching high into leaves -->
          <path d="M90 240 L260 20 L290 25 L140 250 Z" fill="#f59e0b"/>
          <!-- Giraffe Head & Horns (Ossicones) -->
          <ellipse cx="280" cy="18" rx="22" ry="14" fill="#f59e0b"/>
          <line x1="275" y1="10" x2="270" y2="-4" stroke="#78350f" stroke-width="4"/>
          <circle cx="270" cy="-4" r="3" fill="#78350f"/>
          <circle cx="285" cy="15" r="4" fill="#000"/>
          <!-- Distinctive Polygonal Coat Patches -->
          <g fill="#78350f">
            <polygon points="120,240 145,235 140,255 118,255"/>
            <polygon points="125,190 155,185 150,215 120,215"/>
            <polygon points="160,150 190,145 185,175 155,175"/>
            <polygon points="195,110 225,105 220,135 190,135"/>
            <polygon points="230,70 260,65 255,95 225,95"/>
          </g>
        </g>
        """
    ),
    (
        57,
        "Why Leopard Has Spots",
        "The Beautiful Rosettes Bestowed for Forest Camouflage",
        """
        <linearGradient id="sky57" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fdba74"/><stop offset="100%" stop-color="#fde047"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky57)"/>
        <!-- Acacia Tree Trunk and Branch -->
        <path d="M120 450 L180 230 L220 230 L200 450 Z" fill="#451a03"/>
        <path d="M180 240 Q400 200 700 230 L700 260 Q400 230 180 270 Z" fill="#451a03"/>
        <!-- Splendid Spotted Leopard Lounging on Branch -->
        <g transform="translate(240, 130)">
          <!-- Sleek Golden Body -->
          <ellipse cx="170" cy="90" rx="110" ry="42" fill="#f59e0b"/>
          <!-- Paws dangling comfortably -->
          <rect x="95" y="115" width="20" height="50" rx="8" fill="#d97706"/>
          <rect x="225" y="115" width="20" height="50" rx="8" fill="#d97706"/>
          <!-- Long Spotted Tail Hanging Down -->
          <path d="M275 90 Q310 130 300 190" stroke="#f59e0b" stroke-width="12" stroke-linecap="round" fill="none"/>
          <!-- Feline Head resting on paws -->
          <circle cx="80" cy="75" r="32" fill="#f59e0b"/>
          <circle cx="68" cy="48" r="10" fill="#78350f"/>
          <circle cx="92" cy="48" r="10" fill="#78350f"/>
          <circle cx="70" cy="72" r="5" fill="#22c55e"/>
          <circle cx="70" cy="72" r="2" fill="#000"/>
          <!-- Distinctive Black Rosette Spots -->
          <g fill="#78350f" stroke="#000" stroke-width="2">
            <circle cx="130" cy="80" r="7"/><circle cx="160" cy="70" r="8"/><circle cx="190" cy="75" r="7"/>
            <circle cx="140" cy="100" r="8"/><circle cx="175" cy="98" r="9"/><circle cx="210" cy="95" r="8"/>
            <circle cx="240" cy="85" r="7"/><circle cx="245" cy="105" r="6"/>
          </g>
        </g>
        """
    ),
    (
        58,
        "Why Monkeys Resemble People",
        "The Kinship and Cleverness of the Tree Canopy Dwellers",
        """
        <linearGradient id="sky58" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#bae6fd"/><stop offset="100%" stop-color="#bbf7d0"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky58)"/>
        <!-- Jungle Canopy Vines & Leaves -->
        <path d="M0 80 Q200 140 400 90 T800 120" stroke="#15803d" stroke-width="16" fill="none"/>
        <path d="M0 40 Q400 20 800 40" stroke="#166534" stroke-width="30" fill="none"/>
        <!-- Playful Vervet Monkey Hanging from Branch -->
        <g transform="translate(320, 100)">
          <!-- Tail wrapped around vine -->
          <path d="M120 70 Q160 0 110 -20 Q80 -10 110 30" stroke="#78716c" stroke-width="12" fill="none" stroke-linecap="round"/>
          <!-- Body -->
          <ellipse cx="90" cy="120" rx="45" ry="60" fill="#78716c"/>
          <ellipse cx="90" cy="130" rx="30" ry="40" fill="#d6d3d1"/>
          <!-- Long Expressive Arms -->
          <path d="M60 100 Q10 130 30 170" stroke="#78716c" stroke-width="12" stroke-linecap="round" fill="none"/>
          <path d="M120 100 Q170 120 150 170" stroke="#78716c" stroke-width="12" stroke-linecap="round" fill="none"/>
          <!-- Human-like Face & Expressive Eyes -->
          <circle cx="90" cy="55" r="32" fill="#78716c"/>
          <ellipse cx="90" cy="60" rx="22" ry="18" fill="#1c1917"/>
          <circle cx="82" cy="56" r="5" fill="#facc15"/>
          <circle cx="82" cy="56" r="2.5" fill="#000"/>
          <circle cx="98" cy="56" r="5" fill="#facc15"/>
          <circle cx="98" cy="56" r="2.5" fill="#000"/>
          <!-- Ears -->
          <circle cx="60" cy="55" r="10" fill="#d6d3d1"/>
          <circle cx="120" cy="55" r="10" fill="#d6d3d1"/>
        </g>
        """
    ),
    (
        59,
        "The Friendship of Pulu and Ngolo",
        "The Loyal Partnership of Bushbuck and Zebra",
        """
        <linearGradient id="sky59" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fed7aa"/><stop offset="100%" stop-color="#bbf7d0"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky59)"/>
        <rect y="310" width="800" height="140" fill="#15803d"/>
        <!-- Pulu the Graceful Bushbuck -->
        <g transform="translate(140, 180)">
          <!-- Bushbuck Reddish-Brown Body -->
          <ellipse cx="110" cy="90" rx="65" ry="40" fill="#9a3412"/>
          <!-- White Spots on Flank -->
          <circle cx="120" cy="85" r="4" fill="#fff"/>
          <circle cx="135" cy="95" r="4" fill="#fff"/>
          <circle cx="150" cy="88" r="4" fill="#fff"/>
          <!-- Legs -->
          <rect x="70" y="125" width="14" height="60" rx="4" fill="#7c2d12"/>
          <rect x="140" y="125" width="14" height="60" rx="4" fill="#7c2d12"/>
          <!-- Elegant Head & Spiral Horns -->
          <circle cx="50" cy="65" r="24" fill="#9a3412"/>
          <path d="M45 45 L35 10" stroke="#292524" stroke-width="6" stroke-linecap="round"/>
          <path d="M55 45 L50 8" stroke="#292524" stroke-width="6" stroke-linecap="round"/>
          <circle cx="42" cy="62" r="4" fill="#000"/>
        </g>
        <!-- Ngolo the Zebra Standing Beside Him -->
        <g transform="translate(420, 150)">
          <!-- Zebra Body -->
          <ellipse cx="130" cy="110" rx="85" ry="55" fill="#f8fafc"/>
          <!-- Legs -->
          <rect x="80" y="160" width="18" height="65" rx="5" fill="#f8fafc"/>
          <rect x="165" y="160" width="18" height="65" rx="5" fill="#f8fafc"/>
          <!-- Head and Mane -->
          <circle cx="55" cy="75" r="32" fill="#f8fafc"/>
          <path d="M55 45 Q75 40 90 65" stroke="#000" stroke-width="8" fill="none"/>
          <!-- Striking Black Stripes -->
          <g stroke="#000" stroke-width="8" stroke-linecap="round">
            <line x1="90" y1="75" x2="95" y2="145"/>
            <line x1="115" y1="70" x2="120" y2="150"/>
            <line x1="140" y1="72" x2="145" y2="150"/>
            <line x1="165" y1="78" x2="170" y2="145"/>
            <line x1="190" y1="88" x2="192" y2="135"/>
          </g>
          <circle cx="42" cy="72" r="4" fill="#000"/>
        </g>
        """
    ),
    (
        60,
        "Why Collared Dove Has a Ring Around His Neck",
        "The Sacred Messenger Honoured with a Velvet Collar",
        """
        <linearGradient id="sky60" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#bae6fd"/><stop offset="100%" stop-color="#fed7aa"/></linearGradient>
        <rect width="800" height="450" fill="url(#sky60)"/>
        <!-- Woodland Clearing -->
        <rect y="320" width="800" height="130" fill="#15803d"/>
        <!-- Baobab Branch -->
        <path d="M100 290 Q400 240 700 270" stroke="#78350f" stroke-width="24" stroke-linecap="round" fill="none"/>
        <!-- African Collared Dove Resting on Branch -->
        <g transform="translate(320, 120)">
          <!-- Soft Sandy Pinkish-Grey Body -->
          <ellipse cx="100" cy="110" rx="75" ry="48" fill="#d6d3d1"/>
          <!-- Folded Wing with Soft Shading -->
          <ellipse cx="115" cy="115" rx="55" ry="32" fill="#a8a29e"/>
          <!-- Long Sleek Tail -->
          <polygon points="170,110 240,140 180,130" fill="#78716c"/>
          <!-- Elegant Dove Head -->
          <circle cx="45" cy="75" r="28" fill="#e7e5e4"/>
          <!-- The Distinctive Velvet Black Neck Collar Ring -->
          <path d="M50 85 C65 92 68 100 55 106" stroke="#1c1917" stroke-width="8" stroke-linecap="round" fill="none"/>
          <path d="M52 86 C64 92 66 99 56 104" stroke="#fff" stroke-width="2" stroke-linecap="round" fill="none"/>
          <!-- Ruby Ringed Eye & Beak -->
          <circle cx="36" cy="72" r="6" fill="#dc2626"/>
          <circle cx="36" cy="72" r="3" fill="#000"/>
          <polygon points="20,76 2,80 20,84" fill="#57534e"/>
          <!-- Delicate Pink Feet Gripping Branch -->
          <line x1="85" y1="155" x2="85" y2="175" stroke="#f43f5e" stroke-width="5" stroke-linecap="round"/>
          <line x1="115" y1="155" x2="115" y2="175" stroke="#f43f5e" stroke-width="5" stroke-linecap="round"/>
        </g>
        """
    )
]

def generate_svg(story_id, title, subtitle, content):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="800" height="450">
  <defs>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  {content}
  
  <!-- Title Badge Overlay -->
  <g transform="translate(24, 24)">
    <rect width="420" height="62" rx="10" fill="rgba(24, 57, 52, 0.90)" filter="url(#shadow)"/>
    <text x="18" y="24" font-family="Ubuntu, sans-serif" font-size="12" font-weight="700" fill="#f59e0b" letter-spacing="1.5">CHAPTER {story_id} &middot; LANSDOWN TALES</text>
    <text x="18" y="48" font-family="Ubuntu, sans-serif" font-size="18" font-weight="700" fill="#ffffff">{title}</text>
  </g>
</svg>
"""

def main():
    print(f"Generating {len(STORIES)} accurate illustrated story SVGs...")
    for story_id, title, subtitle, content in STORIES:
        svg_code = generate_svg(story_id, title, subtitle, content)
        filename = f"story-{str(story_id).zfill(2)}.svg"
        for d in DEST_DIRS:
            d.mkdir(parents=True, exist_ok=True)
            out_file = d / filename
            out_file.write_text(svg_code, encoding="utf-8")
        print(f"  [OK] Created {filename}: {title}")

if __name__ == "__main__":
    main()
