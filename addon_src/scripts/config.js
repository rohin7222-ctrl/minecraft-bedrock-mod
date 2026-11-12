/**
 * ============================================================================
 * CONFIG.JS - CIVILIZATION ADDON PART 5 CONFIGURATION & VOCABULARY GRAPH
 * ============================================================================
 */

export const BEDROCK_MONSTER_IDS = [
  "minecraft:blaze", "minecraft:bogged", "minecraft:breeze", "minecraft:cave_spider",
  "minecraft:creeper", "minecraft:drowned", "minecraft:elder_guardian", "minecraft:endermite",
  "minecraft:evocation_illager", "minecraft:evoker", "minecraft:ghast", "minecraft:guardian",
  "minecraft:hoglin", "minecraft:husk", "minecraft:illusion_illager", "minecraft:illusioner",
  "minecraft:magma_cube", "minecraft:phantom", "minecraft:piglin_brute", "minecraft:pillager",
  "minecraft:ravager", "minecraft:shulker", "minecraft:silverfish", "minecraft:skeleton",
  "minecraft:slime", "minecraft:stray", "minecraft:vex", "minecraft:vindicator",
  "minecraft:warden", "minecraft:witch", "minecraft:wither_skeleton", "minecraft:zoglin",
  "minecraft:zombie", "minecraft:zombie_villager", "minecraft:zombie_villager_v2",
  "minecraft:enderman", "minecraft:spider", "minecraft:zombie_pigman",
  "minecraft:zombified_piglin", "minecraft:wither", "minecraft:ender_dragon",
  "minecraft:zombie_horse", "minecraft:creaking", "minecraft:creaking_transient"
];

export const MONSTER_TYPE_IDS = new Set(BEDROCK_MONSTER_IDS);

export const JOB_ROLES = [
  { id: "woodcutter", title: "Master Woodcutter", emoji: "🪓", tool: "Axe", desc: "Harvests logs from forests and supplies the Crafter" },
  { id: "miner", title: "Master Miner", emoji: "⛏️", tool: "Pickaxe", desc: "Extracts stone, coal, iron, and minerals for metallurgy" },
  { id: "crafter", title: "Master Artisan Crafter", emoji: "🔨", tool: "Crafting Table", desc: "Processes timber and ores into tools, building kits, and beds" },
  { id: "storage_manager", title: "Grand Storage Manager", emoji: "📦", tool: "Communal Chest", desc: "Maintains the central depot and distributes tools and construction supplies" },
  { id: "builder", title: "Chief Architect Builder", emoji: "🏗️", tool: "Trowel & Hammer", desc: "Constructs residential cottages with beds for new citizens and upgrades roads" }
];

export const BASE_VOCABULARY = {
  "civilization": "An advanced, peaceful society with architecture, science, and flourishing culture.",
  "peaceful": "A tranquil state free from hostile monsters or destruction.",
  "emerald": "The radiant green gem that drives honest trade across all lands."
};

export const AUTONOMOUS_DISCOVERY_POOL = [
  // 1. Science & Physical Laws
  { word: "photosynthesis", topic: "science", meaning: "The biological process by which green crops harness sunlight to synthesize nourishment." },
  { word: "thermodynamics", topic: "science", meaning: "The physical laws governing heat transfer, energy transformation, and smelting power." },
  { word: "metallurgy", topic: "craft", meaning: "The science studying the extraction, melting, and alloying of metallic elements." },
  { word: "acoustics", topic: "science", meaning: "The physical science determining how sound harmonics and bell chimes reverberate across space." },
  { word: "crystallography", topic: "science", meaning: "The experimental study of emerald crystal lattice structures and light refraction." },
  { word: "aerodynamics", topic: "science", meaning: "The study of air currents and forces acting upon gliding wings and flight paths." },
  { word: "optics", topic: "science", meaning: "The study of light transmission, glass lenses, prism colors, and visual focus." },
  { word: "resonance", topic: "science", meaning: "The amplification of harmonic energy when external frequency matches natural vibration." },
  { word: "equilibrium", topic: "science", meaning: "A harmonious state of perfect balance where opposing forces neutralize each other." },
  { word: "gravitation", topic: "science", meaning: "The fundamental cosmic attraction drawing celestial bodies and matter together." },
  { word: "magnetism", topic: "science", meaning: "The physical phenomenon of magnetic attraction utilized in compass navigation." },
  { word: "chemistry", topic: "science", meaning: "The scientific discipline examining matter transformation, alchemy, and elemental bonds." },
  { word: "mechanics", topic: "science", meaning: "The study of mechanical forces, momentum, kinetic transfer, and simple machines." },
  { word: "hydraulics", topic: "science", meaning: "The applied science of liquid flow, fluid pressure, and water-powered conduits." },

  // 2. Agriculture, Forestry & Ecology
  { word: "irrigation", topic: "agriculture", meaning: "The deliberate channeling of fresh water to land to cultivate thriving bountiful harvests." },
  { word: "germination", topic: "agriculture", meaning: "The initial emergence of a vibrant living sprout breaking through a fertile seed." },
  { word: "permaculture", topic: "agriculture", meaning: "Sustainable agricultural ecosystems modeled after self-sustaining natural biomes." },
  { word: "hydrology", topic: "science", meaning: "The comprehensive science of water flow, evaporation, river basins, and rainfall." },
  { word: "biodiversity", topic: "nature", meaning: "The rich variety of flora and fauna coexisting to preserve ecological health." },
  { word: "symbiosis", topic: "nature", meaning: "A mutually beneficial partnership between distinct living species in an ecosystem." },
  { word: "botany", topic: "nature", meaning: "The botanical branch devoted to plant physiology, crop genetics, and herbal properties." },
  { word: "meteorology", topic: "nature", meaning: "The observational study of atmospheric pressure, clouds, weather patterns, and rainfall." },
  { word: "agronomy", topic: "agriculture", meaning: "The science and technology of cultivating soil and maximizing crop nutritional yields." },
  { word: "reforestation", topic: "nature", meaning: "The systematic replanting of woodlands to sustain biodiversity and timber balance." },
  { word: "composting", topic: "agriculture", meaning: "The organic biological recycling of plant remnants into nutrient-rich soil humus." },
  { word: "horticulture", topic: "agriculture", meaning: "The cultivation of garden botanicals, medicinal plants, orchard fruits, and flowers." },
  { word: "microclimate", topic: "nature", meaning: "Local atmospheric conditions in a sheltered valley or mountain terrace distinct from surrounding zones." },

  // 3. Craft, Architecture & Engineering
  { word: "architecture", topic: "craft", meaning: "The art and engineering discipline of designing enduring, magnificent monuments and shelters." },
  { word: "infrastructure", topic: "craft", meaning: "The essential network of paved roads, aqueducts, and bridges connecting a civilization." },
  { word: "masonry", topic: "craft", meaning: "The time-honored craft of dressing stone and bricks into impenetrable, aesthetic structures." },
  { word: "aqueducts", topic: "craft", meaning: "Monumental arched conduits built to transport fresh spring water across vast distances." },
  { word: "geometry", topic: "science", meaning: "The mathematics of angles, spatial symmetry, coordinates, and architectural proportions." },
  { word: "engineering", topic: "craft", meaning: "The creative application of scientific principles to construct machines and enduring works." },
  { word: "cartography", topic: "craft", meaning: "The precise science of surveying terrain and charting accurate geographic maps of our World." },
  { word: "navigation", topic: "craft", meaning: "The art of calculating position, coordinates, and travel routes by celestial landmarks." },
  { word: "carpentry", topic: "craft", meaning: "The skilled art of cutting, joining, and shaping timber into functional and artistic works." },
  { word: "surveying", topic: "craft", meaning: "The precision measurement of boundary elevations, distances, and geographic angles." },
  { word: "stonemasonry", topic: "craft", meaning: "The master cutting of granite, andesite, and deepslate to withstand centuries of weathering." },
  { word: "ventilation", topic: "craft", meaning: "Designing air conduits and chimneys within subterranean halls to maintain pure airflow." },

  // 4. Astronomy & Cosmology
  { word: "astronomy", topic: "astronomy", meaning: "The scientific observation of celestial bodies, constellations, planetary orbits, and the cosmos." },
  { word: "celestial", topic: "astronomy", meaning: "Pertaining to the infinite starry sky, astronomical motions, and cosmic wonder." },
  { word: "zenith", topic: "astronomy", meaning: "The culminating celestial point directly overhead where the sun shines at maximum brilliance." },
  { word: "solstice", topic: "astronomy", meaning: "The celestial milestone marking the longest solar day or deepest winter twilight." },
  { word: "equinox", topic: "astronomy", meaning: "The celestial moment when daylight and night achieve absolute mathematical equality." },
  { word: "chronometry", topic: "astronomy", meaning: "The high-precision science of time measurement synchronized with the planetary solar cycle." },
  { word: "cosmology", topic: "astronomy", meaning: "The profound exploration into the birth, architecture, and destiny of the universe." },
  { word: "constellations", topic: "astronomy", meaning: "Recognizable star clusters in the night sky utilized for seasonal calendars and wayfinding." },
  { word: "eclipse", topic: "astronomy", meaning: "The cosmic alignment when one celestial body passes directly into the shadow of another." },
  { word: "astrophysics", topic: "astronomy", meaning: "The physical laws determining stellar radiation, gravity wells, and planetary orbits." },
  { word: "orbital", topic: "astronomy", meaning: "The curved trajectory of a celestial sphere governed by balanced gravitational attraction." },
  { word: "parallax", topic: "astronomy", meaning: "The apparent displacement of a distant star viewed from different orbital positions." },

  // 5. Philosophy, Civics & Law
  { word: "epistemology", topic: "philosophy", meaning: "The branch of philosophy investigating the origin, foundations, and validity of knowledge." },
  { word: "philosophy", topic: "philosophy", meaning: "The contemplation of truth, reason, existence, ethics, and the human journey." },
  { word: "democracy", topic: "philosophy", meaning: "A cooperative system of collective decision-making where every citizen shares a voice." },
  { word: "harmony", topic: "peace", meaning: "A tranquil state of mutual coexistence, balance, and cooperative solidarity in society." },
  { word: "innovation", topic: "science", meaning: "The generation, testing, and implementation of novel ideas to advance our civilization." },
  { word: "ethics", topic: "philosophy", meaning: "Moral principles guiding benevolent decisions, honest dealings, and mutual respect." },
  { word: "compassion", topic: "peace", meaning: "Empathy for fellow citizens coupled with an active dedication to uplift one another." },
  { word: "civics", topic: "philosophy", meaning: "The shared rights, responsibilities, and duties of citizens nurturing a flourishing society." },
  { word: "prosperity", topic: "peace", meaning: "A thriving state characterized by abundant resources, universal safety, and collective joy." },
  { word: "altruism", topic: "peace", meaning: "Selfless concern for the well-being and advancement of the community as a whole." },
  { word: "justice", topic: "philosophy", meaning: "The impartial administration of fairness, truth, and equitable opportunity for all." },
  { word: "jurisprudence", topic: "philosophy", meaning: "The theoretical study and philosophy of legal principles, rights, and societal order." },
  { word: "constitution", topic: "philosophy", meaning: "The fundamental organic law and charter defining the governance and rights of a people." },
  { word: "egalitarianism", topic: "philosophy", meaning: "The civic doctrine that all citizens possess equal worth, rights, and dignity." },

  // 6. Economics, Commerce & Logistics
  { word: "commerce", topic: "economics", meaning: "The ethical exchange of goods, commodities, and craftsmanship between peaceful communities." },
  { word: "currency", topic: "economics", meaning: "The recognized medium of trade, such as luminous emeralds, facilitating honest commerce." },
  { word: "reciprocity", topic: "economics", meaning: "The mutual practice of exchanging gifts, aid, and trade benefits in fair equilibrium." },
  { word: "specialization", topic: "economics", meaning: "The division of civic labor allowing citizens to master distinct arts and sciences." },
  { word: "mercantilism", topic: "economics", meaning: "The economic principle of maximizing civic productivity and domestic abundance." },
  { word: "enterprise", topic: "economics", meaning: "The bold undertaking of productive, cooperative ventures to serve community needs." },
  { word: "barter", topic: "economics", meaning: "The direct, mutually advantageous exchange of goods without financial intermediaries." },
  { word: "stewardship", topic: "economics", meaning: "The prudent, responsible management of shared communal resources and lands." },
  { word: "logistics", topic: "economics", meaning: "The organized coordination and transport of materials, tools, and provisions." },
  { word: "sovereign", topic: "economics", meaning: "Possessing autonomous self-governance and recognized territorial authority." },
  { word: "granary", topic: "economics", meaning: "A strategic communal storehouse preserving surplus grain against unforeseen drought." },

  // 7. Medicine & Cellular Biology
  { word: "herbalism", topic: "nature", meaning: "The medicinal knowledge of harvesting wild botanicals and herbs to restore health and vigor." },
  { word: "sanitation", topic: "science", meaning: "Public hygienic measures and clean water stewardship safeguarding community wellness." },
  { word: "physiology", topic: "science", meaning: "The scientific study of the functions and living mechanisms sustaining the body." },
  { word: "pharmacology", topic: "science", meaning: "The science of preparing therapeutic remedies, poultices, and curative brews." },
  { word: "immunology", topic: "science", meaning: "The bodily defense systems shielding living organisms from ailments and toxins." },
  { word: "respiration", topic: "science", meaning: "The vital exchange of gases supplying living cells with oxygen for metabolic energy." },
  { word: "cellular", topic: "science", meaning: "Pertaining to the microscopic living units that compose all botanical and animal life." },
  { word: "homeostasis", topic: "science", meaning: "The self-regulating physiological process maintaining internal bodily equilibrium." },
  { word: "hygiene", topic: "science", meaning: "Practices conducive to maintaining health and preventing ailments through cleanliness." },
  { word: "nourishment", topic: "nature", meaning: "Wholesome nutritional intake sustaining physical vigor and cognitive clarity." },
  { word: "vitality", topic: "peace", meaning: "A vibrant state of physical health, resilience, and boundless energetic life." },

  // 8. Cybernetics, Logic & Epistemology
  { word: "cybernetics", topic: "science", meaning: "The comparative study of automatic control systems and communication feedback loops." },
  { word: "algorithms", topic: "science", meaning: "Step-by-step mathematical procedures formulated for problem-solving and computation." },
  { word: "calculus", topic: "science", meaning: "The branch of mathematics examining rates of change, continuous curves, and areas." },
  { word: "empiricism", topic: "philosophy", meaning: "The epistemological theory asserting that knowledge originates in sensory observation." },
  { word: "deduction", topic: "philosophy", meaning: "The logical inference from general premises to arrive at certain, specific conclusions." },
  { word: "induction", topic: "philosophy", meaning: "The formulation of universal principles derived from repetitive empirical observations." },
  { word: "dialectics", topic: "philosophy", meaning: "The art of discovering truth through discourse, reasoned debate, and contradiction analysis." },
  { word: "rationality", topic: "philosophy", meaning: "The quality of thinking, judging, and acting in strict conformity with reason and evidence." },
  { word: "nomenclature", topic: "science", meaning: "A systematic set of names or terms applied to catalog the natural World." },
  { word: "cryptography", topic: "craft", meaning: "The discipline of securing communications and territorial charters through encrypted ciphers." },
  { word: "semantics", topic: "philosophy", meaning: "The study of meaning in linguistic symbols, words, and logical propositions." }
];

export const VILLAGER_NAMES = [
  "Arthur", "Elara", "Torvald", "Cedric", "Lyra", "Gareth", "Rowan",
  "Silas", "Isabel", "Jasper", "Penelope", "Matthew", "Nora", "Victor",
  "Clara", "Henry", "Beatrice", "Finnian", "Maeve", "Tobias", "Seraphina",
  "Evander", "Gideon", "Miriam", "Alaric", "Cora", "Darius", "Fiona",
  "Aurelius", "Thalassa", "Octavius", "Valeria", "Cassian", "Helena"
];

export const PERSONALITIES = [
  { trait: "Visionary", focus: "future innovation, cosmic exploration, and World evolution" },
  { trait: "Empiricist", focus: "scientific observation, physical laws, and agriculture" },
  { trait: "Philosopher", focus: "peaceful ethics, social harmony, and epistemological truth" },
  { trait: "Caretaker", focus: "citizen well-being, ecological health, and village unity" },
  { trait: "Artisan", focus: "monumental architecture, durable masonry, and metallurgy" }
];

export const MOODS = [
  { mood: "Inspired", icon: "✨", desc: "Formulating novel scientific theories" },
  { mood: "Peaceful", icon: "🕊️", desc: "Rejoicing in a monster-free World" },
  { mood: "Curious", icon: "🔍", desc: "Analyzing environmental World patterns" },
  { mood: "Joyful", icon: "🌻", desc: "Celebrating World civilizational prosperity" },
  { mood: "Scholarly", icon: "📜", desc: "Archiving chronicles, definitions, and laws" }
];

export const TERRITORY_PREFIXES = [
  "The Kingdom of", "The Grand Republic of", "The Sovereign Haven of",
  "The Dominion of", "The Peaceful Realm of", "The Shire of", "The Valley of",
  "The Commonwealth of", "The Sanctuary of", "The Settlement of", "The Citadel of"
];

export const TERRITORY_ROOTS = [
  "Valoria", "Oakhaven", "Solaris", "Elysium", "Aethelgard", "Verdantia",
  "Novaria", "Silverstone", "Borealis", "Arcadia", "Eldoria", "Sunspire",
  "Evergreen", "Highland", "Riverwood", "Dawnstar", "Mythglen", "Ironwood"
];
