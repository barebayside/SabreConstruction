# Phase 5, part F — the last three Spiral 2 posts that need nobody: S11, R30, R32. (R26 and R34 stay skipped — price posts.)
# Sources read 2026-09-17:
#   ABS 2021 Census QuickStats — Wynnum SAL33188 (14,036 people, median age 43, 70.8% separate houses); Manly SAL31748 (4,273, median age
#     46, 70.6%); Lota SAL31686 (3,518, 42, 95.3%); Manly West SAL31749 (12,436, 41, 78.0%) — as cited in the Phase 3 posts
#   Brisbane City Council — Brisbane Severe Weather Alert ("Storm season typically lasts from October to March"); FloodWise Property Reports;
#     Flood Awareness Online (storm tide, creek, overland flow)
#   Translink — one midday Cleveland-line sample read 17 Sep 2026: Central 12:17 -> Wynnum Central 12:57 -> Manly 1:00 -> Lota 1:03
#   qld.gov.au — school catchment areas (EdMap); Get Ready Queensland — "Protect your home"
#   Queensland Department of Housing / QBCC — Livable Housing Design Standard (NCC 2022) has applied to new homes in Queensland since
#     1 October 2023: a step-free entry, wider internal doors and corridors on the entry level, and bathroom walls built to take grabrails later;
#     time-limited exemptions to 30 September 2026 for some narrow, small and steep lots
#   Queensland Government — asbestos.qld.gov.au (pre-1990 houses)
# Spiral 2 rule: every post ends at the house. Rule 1: no prices, no rents, no bands.

POSTS = {}

# ---------------------------------------------------------------- S11 · moving from interstate
POSTS["s11-interstate"] = dict(
    slug="moving-to-brisbanes-bayside-from-interstate-what-nobody-tells-you",
    section="living",
    title="Moving to Brisbane's Bayside from interstate: what nobody tells you",
    h1="Moving to Brisbane's Bayside from interstate:<br>what nobody tells you.",
    description="The humidity, the tide, the storm season, the train, the school catchments, the word 'highset', and what a seventy-year-old timber house is actually like to live in. An honest briefing from a family that has built here since 1990.",
    lede="You've looked at the map, seen the water, done the sums on the house prices back home and booked the removalist. Good. Here's the part the listings leave out: what the weather does, what the tide does, what the houses are made of, and the handful of local words you'll need by the end of the first week. From a family that builds here, not one selling here.",
    date="2026-09-17", category="Living on the Bayside", image="blog/moving-to-brisbanes-bayside-from-interstate-what-nobody-tells-you.jpg",
    image_alt="A removals truck unloading outside an old highset on a Bayside street, boxes on the footpath, the bay at the end of the road",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real street.",
    label=("What nobody tells you", "Moving here"),
    card_title="Moving to Brisbane's Bayside from interstate: what nobody tells you",
    card_blurb="The humidity, the tide, the storm season, the train, the catchments, the word &lsquo;highset&rsquo;, and what a seventy-year-old timber house is really like to live in.",
    about=["Moving to Brisbane", "Brisbane Bayside", "Wynnum", "Manly", "Living on the Bayside"],
    related=["is-wynnum-a-good-place-to-live", "wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family", "what-are-bayside-houses-made-of"],
    cta="If you've bought the block and the house on it is the problem, that's the conversation Nathan has most. Bring the interstate questions too; he's heard them all.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Seven things. <strong>The humidity</strong> is real from November to March and the houses here are built for it, which is why the old ones are up on stumps with the windows open. <strong>The tide</strong> goes out a long way on Moreton Bay, so &ldquo;waterfront&rdquo; means mudflats twice a day and the water some way off. <strong>Storm season</strong> runs October to March by council's reckoning, and the afternoon storm is a habit, not an event.</p>
        <p><strong>The train</strong> to the city is the Cleveland line, about forty minutes from Wynnum Central on the timetable we read. <strong>School catchments</strong> are drawn by the state and the house you buy decides the school. <strong>&ldquo;Highset&rdquo;</strong> is the word for a house lifted off the ground, and most of them are. And the houses themselves are mostly 1940s to 1970s timber and fibro, often with asbestos somewhere, on blocks that are bigger than the house deserves.</p>
        <p>That last fact is the one that matters most for the next ten years, and it's the reason this post is on a builder's website.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#weather">What does the weather actually do?</a></li>
          <li><a href="#the-tide">What's the tide about?</a></li>
          <li><a href="#getting-around">How do you get to the city?</a></li>
          <li><a href="#schools">How do schools work here?</a></li>
          <li><a href="#the-words">The words you'll need</a></li>
          <li><a href="#the-houses">What are the houses like to live in?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="weather">What does the weather actually do?</h2>
      <p>Summer is hot and wet, not just hot. The humidity arrives around November and stays until the end of March, and the difference from a Melbourne or Adelaide summer is that the nights don't cool off much. Houses here cope with it by design: raised floors for air underneath, wide eaves, verandahs, windows on opposite walls for the breeze off the bay in the afternoon. The old ones were doing this before anyone had air-conditioning.</p>
      <p>Then there's the storm season.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Storm season typically lasts from October to March.&rdquo;</b> Council's advice covers roofs, gutters, trees and an emergency kit, and the afternoon storm with hail and wind is part of a Brisbane summer, not a rare one.</p>
        <cite>Brisbane City Council, <em>Brisbane Severe Weather Alert</em>. For what it means for an old house's roof and trees, <a href="../bayside-storm-season-roof-trees-insurance/">this post</a>.</cite>
      </blockquote>

      <p>Winter, by contrast, is the reason people stay: dry, bright, mild, and the best months on the water.</p>

      <h2 class="h2" id="the-tide">What's the tide about?</h2>
      <p>Moreton Bay is shallow and the tidal range is large enough that the water goes out a long way from the Wynnum and Manly foreshore at low tide, leaving sand and mudflats. Twice a day. It surprises people who expected a beach. What you get instead is the wading pool at Wynnum, the boat harbour at Manly, the jetty, and a foreshore that changes character every six hours.</p>
      <p>The tide also matters for houses. Council maps storm tide as one of the kinds of flooding a block can be exposed to, and the streets one back from the water carry a minimum floor level for anything new. <a href="../does-wynnum-flood/">What the flood maps show is here.</a></p>

      <h2 class="h2" id="getting-around">How do you get to the city?</h2>
      <p>The Cleveland line. Wynnum has three stations (Wynnum North, Wynnum, Wynnum Central), then Manly and Lota. On the midday timetable we sampled, Central to Wynnum Central was forty minutes, and Manly and Lota a few minutes more. Peak services vary; check Translink for yours. By road it depends entirely on the hour. <a href="../how-far-is-wynnum-from-brisbane-cbd/">The honest version is here.</a></p>

      <h2 class="h2" id="schools">How do schools work here?</h2>
      <p>State schools have catchments drawn by the Department of Education, and a child is guaranteed a place at the school whose catchment the home address is in. The department's EdMap tool shows the catchment for any address. Independent and Catholic schools run their own enrolment. The practical point for a buyer from interstate: the house you buy decides the state school, so check the address before you fall for the house. <a href="../schools-on-the-bayside-catchments/">The Bayside's schools and how catchments work are here.</a></p>

      <h2 class="h2" id="the-words">The words you'll need</h2>
      <ul class="pts">
        <li><strong>Highset / lowset.</strong> Lifted off the ground on stumps or posts, or sitting on it. <a href="../what-does-highset-mean-on-a-bayside-block/">More here.</a></li>
        <li><strong>Built-in-under.</strong> A highset whose underneath was closed in for rooms, usually decades ago.</li>
        <li><strong>Queenslander.</strong> The pre-war timber house: verandahs, iron roof, VJ walls, stumps.</li>
        <li><strong>Fibro.</strong> Fibre-cement sheeting. Pre-1990, it usually contains asbestos.</li>
        <li><strong>VJs.</strong> Vertical-joint timber wall boards. People pay to keep them.</li>
        <li><strong>The overlay.</strong> Council's character overlay; pre-1947 houses in it may not be allowed to come down.</li>
        <li><strong>Knockdown rebuild.</strong> What a lot of the streets are doing, one house at a time.</li>
      </ul>

      <h2 class="h2" id="the-houses">What are the houses like to live in?</h2>
      <p>Charming, and small, and tired, in roughly that order.</p>
      <p>Seven in ten homes in Wynnum and Manly are separate houses on their own block, and most were built between the 1940s and the 1970s. That means timber frames that have lasted, rooms sized for a smaller family, kitchens and bathrooms from a different era, stumps that may have moved, and asbestos in the fibro somewhere. The blocks under them are generous. The houses on top often aren't.</p>
      <p>Which is why so many families who move here for the street end up rebuilding on it a few years later. <a href="../why-are-so-many-bayside-houses-being-knocked-down/">That story is here</a>, and <a href="../what-are-bayside-houses-made-of/">what the houses are made of is here</a>. If you're buying the house for the block, <a href="../buying-an-old-house-in-wynnum-or-manly-to-knock-down-what-to-check-before-you-sign/">check these eight things first</a>.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Humid summers and a storm season from October to March.</b> The houses are built for it; the old ones were first.</li>
          <li><b>The tide goes out a long way.</b> Waterfront means mudflats twice a day and a foreshore that changes every six hours.</li>
          <li><b>The train is the Cleveland line,</b> about forty minutes to Wynnum Central on the service we read.</li>
          <li><b>The address decides the state school.</b> Check EdMap before the house.</li>
          <li><b>The houses are 1940s&ndash;70s timber and fibro on good blocks.</b> Charming, small, tired &mdash; and often rebuilt.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Is it cooler by the water?</p>
          <p>The afternoon sea breeze is real and the old houses were sited for it. It doesn't fix the humidity; it makes it bearable. A house designed to catch it matters more here than almost anywhere in Brisbane.</p>
        </div>
        <div>
          <p class="q">Do we need to worry about flooding?</p>
          <p>Check council's free FloodWise report on any address before you buy. The Bayside's flood kinds are storm tide, creek and overland flow rather than the river. It usually changes what you'd build, not whether you'd live there.</p>
        </div>
        <div>
          <p class="q">Which suburb?</p>
          <p>Wynnum is the town, Manly the harbour, Lota the quiet one, Manly West the flatter newer one, Wakerley and Gumdale newer again. <a href="../wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family/">The comparison is here.</a></p>
        </div>
        <div>
          <p class="q">Should we buy the old house and rebuild later?</p>
          <p>Plenty do. Buy the block for the street and the school; treat the house as the thing you'll decide about once you've lived in it a winter. Nathan will walk it with you before you make an offer.</p>
        </div>
      </div>

      <p class="small sources">Sources: Australian Bureau of Statistics, 2021 Census QuickStats (Wynnum, Manly); Brisbane City Council, <em>Brisbane Severe Weather Alert</em>, <em>FloodWise Property Reports</em>; Translink, Cleveland line timetable (one midday service read 17 September 2026); Queensland Government, <em>School catchment areas</em> (EdMap) and <em>asbestos.qld.gov.au</em>. Read 17 September 2026. Plain-English guidance from a builder; not property, financial or planning advice.</p>
''')

# ---------------------------------------------------------------- R30 · the foreshore
POSTS["r30-foreshore"] = dict(
    slug="what-is-the-wynnum-manly-foreshore-actually-like-to-live-near",
    section="living",
    title="What is the Wynnum&ndash;Manly foreshore actually like to live near?",
    h1="What is the Wynnum&ndash;Manly foreshore<br>actually like to live near?",
    description="The salt, the wind, the tide going out, the king tides, the storm-tide overlay, and what all of it does to a house over twenty years. A builder's honest account of the best streets on the Bayside and what they ask of the buildings on them.",
    lede="The streets along the water are the ones everybody wants, and the houses on them work harder than any others on the Bayside. Salt, wind, tide and weather all come off the bay, and a house near the foreshore is either built for that or slowly losing to it. Here's what living there is actually like, and what it means for the house.",
    date="2026-09-17", category="Living on the Bayside", image="blog/what-is-the-wynnum-manly-foreshore-actually-like-to-live-near.jpg",
    image_alt="An esplanade street at dusk, the bay beyond the seawall, salt haze in the air, a row of old houses with weathered iron roofs",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real street.",
    label=("Salt, wind, tide", "Living on the foreshore"),
    card_title="What is the Wynnum&ndash;Manly foreshore actually like to live near?",
    card_blurb="The salt, the wind, the tide going out, the king tides, the storm-tide overlay, and what all of it does to a house over twenty years. A builder's honest account.",
    about=["Wynnum Manly foreshore", "Coastal living Brisbane", "Salt air corrosion", "Living on the Bayside"],
    related=["does-wynnum-flood", "bayside-storm-season-roof-trees-insurance", "is-wynnum-a-good-place-to-live"],
    cta="If your house is on the water side and it's showing its age, Nathan will walk it and tell you what the salt has done and what a house built for the foreshore would do differently.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Living near the foreshore means four things come off the bay and into your life: <strong>salt</strong>, <strong>wind</strong>, the <strong>tide</strong>, and <strong>weather</strong>. Salt air works on steel, fixings, roofing and paint faster than anywhere inland. The afternoon breeze that makes summer bearable is a wind in a storm. The tide goes out a long way twice a day and comes up to the seawall on a king tide. And the streets closest to the water sit under council's coastal hazard and storm tide mapping, which sets a floor level for anything new.</p>
        <p>None of that is a reason not to live there. It's the reason the houses along the esplanade look the way they do: iron roofs replaced, timber repainted, stumps redone, and, one by one, rebuilt higher and tougher than what stood there before.</p>
        <p>The honest version is that a foreshore house costs more to keep and asks more of its design. The reward is the reason everyone wants the street.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#salt">What does the salt do?</a></li>
          <li><a href="#wind">What does the wind do?</a></li>
          <li><a href="#tide">What does the tide do?</a></li>
          <li><a href="#the-maps">What do council's maps say about the foreshore streets?</a></li>
          <li><a href="#the-house">What does a house built for the foreshore do differently?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="salt">What does the salt do?</h2>
      <p>It corrodes. Salt carried on the air settles on every surface facing the bay and gets into everything that isn't sealed. On an old foreshore house you see it as rust on the roofing iron and the gutters, rusted nails and screws bleeding through paint, corroded hinges and window winders, and pitting on anything aluminium or galvanised that wasn't rated for the coast.</p>
      <p>It's a maintenance load, not a mystery. Materials exist that are made for marine environments, and the difference between a foreshore house that ages well and one that doesn't is mostly whether they were used. Which is a design and specification decision, made once, at the start.</p>

      <h2 class="h2" id="wind">What does the wind do?</h2>
      <p>The afternoon north-easterly off the bay is the reason the old houses along the water were built with their verandahs facing it. In summer it's the best thing about the street.</p>
      <p>In a storm it's the load the house has to carry. The frame's tie-downs, the roof fixings and the way the roof is designed are engineered to a wind classification, and a house on an exposed foreshore street is designed to a higher one than a house three streets back. On an old house nobody engineered it at all, which is what council's storm-season advice about roofs is really about. <a href="../bayside-storm-season-roof-trees-insurance/">That post is here.</a></p>

      <h2 class="h2" id="tide">What does the tide do?</h2>
      <p>Two things, at two scales.</p>
      <p>Every day, it goes out a long way and comes back. The foreshore is sand and mudflats at low tide and water to the seawall at high. It's the rhythm of the place, and it's why the wading pool and the jetty exist.</p>
      <p>A few times a year, on a king tide with a swell behind it, the water reaches the top of the wall and the lowest streets see it in the gutters. That's the ordinary end of what council models as storm tide: the bay pushed up by a storm surge on top of a high tide. The old houses along the water were built before anyone mapped it. The new ones are built to the map.</p>

      <h2 class="h2" id="the-maps">What do council's maps say about the foreshore streets?</h2>

      <blockquote class="proof">
        <p><b>Council's FloodWise Property Report shows which kinds of flooding could affect a property &mdash; river, creek, storm tide and overland flow &mdash; the flood levels at different likelihoods, and the minimum habitable floor level a new house must meet.</b> Storm tide is mapped under the coastal hazard overlay.</p>
        <cite>Brisbane City Council, <em>FloodWise Property Reports</em> and <em>Flood Awareness Online</em>. For a foreshore address, pull the report before you buy or build. It's free and it takes a minute.</cite>
      </blockquote>

      <p>What it means in practice: a new house on the water side usually has its living areas above the mapped level, and the ground floor is the garage, the storage and the room that can be hosed out. <a href="../rebuilding-on-a-flood-overlay-block-on-the-bayside/">What a flood overlay changes for a rebuild is here.</a></p>

      <h2 class="h2" id="the-house">What does a house built for the foreshore do differently?</h2>
      <ul class="pts">
        <li><strong>Materials rated for the coast.</strong> Roofing, gutters, fixings, hardware, balustrades, external lights: all specified for a marine environment, not the standard catalogue.</li>
        <li><strong>A wind design to suit the exposure.</strong> Tie-downs, roof fixings and openings engineered for the site's wind classification.</li>
        <li><strong>The floor level from the report.</strong> Living up, wet-tolerant space down.</li>
        <li><strong>Facing the breeze, shading the west.</strong> The old houses had this right: openings to the north-east, protection from the afternoon sun.</li>
        <li><strong>Maintenance designed in.</strong> Surfaces you can wash the salt off, paint systems made for it, and no hidden steel.</li>
      </ul>
      <p>That's a different specification from a house three streets back, and it should look different on the quote. <a href="../what-should-be-in-a-builders-quote-line-by-line/">What a complete quote carries is here.</a></p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Salt, wind, tide and weather all come off the bay.</b> A foreshore house is built for them or losing to them.</li>
          <li><b>Salt corrodes anything not rated for the coast.</b> That's a specification decision made once.</li>
          <li><b>The breeze is a wind in a storm.</b> Exposed streets are engineered to a higher wind classification.</li>
          <li><b>King tides reach the wall; council maps storm tide.</b> New houses are built to the map.</li>
          <li><b>Pull the FloodWise report for any foreshore address</b> before you buy or build.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Does living on the water mean the house will flood?</p>
          <p>It means council has mapped what the bay could do in a storm-tide event and set a floor level for new houses accordingly. An old house below that level carries the risk; a new one designed to it doesn't carry it the same way. The report for the address is the honest answer.</p>
        </div>
        <div>
          <p class="q">How much more maintenance is a foreshore house?</p>
          <p>Noticeably more on an old one that wasn't built for it: paint, roofing, hardware, stumps. Much less on one specified for the coast. It's the difference between fighting the salt and having planned for it.</p>
        </div>
        <div>
          <p class="q">Are the foreshore streets in the character overlay?</p>
          <p>Many of the older ones are. If the house is pre-1947, demolition needs a development application and council may say no. <a href="../check-if-your-street-is-in-the-character-overlay/">Check the street here.</a></p>
        </div>
        <div>
          <p class="q">Would you build on the water side?</p>
          <p>Yes, designed for it. The best streets on the Bayside deserve houses that can take what the bay gives them.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <em>FloodWise Property Reports</em>, <em>Flood Awareness Online</em> and <em>Brisbane Severe Weather Alert</em>; Brisbane City Plan 2014, coastal hazard overlay. Read 17 September 2026. Plain-English guidance from a builder; not engineering, insurance or planning advice. Wind classification and material specification for a given site are set by the engineer and the designer for that site.</p>
''')

# ---------------------------------------------------------------- R32 · retiring on the Bayside
POSTS["r32-retire"] = dict(
    slug="is-the-bayside-a-good-place-to-retire",
    section="living",
    title="Is the Bayside a good place to retire, and should you stay in the house?",
    h1="Is the Bayside a good place to retire,<br>and should you stay in the house?",
    description="Why so many people do (the water, the flat foreshore, the train, the village), and the honest question underneath it: whether the highset with the stairs is the house to grow old in. What Queensland's new livable housing standard requires, and the options for staying on the street.",
    lede="Plenty of people retire on the Bayside without moving a metre, because they were already here. The question isn't the suburb. It's the house: two flights of stairs, a bathroom nobody can turn around in, and a block that's worth more to you than anywhere you'd go. Here's what makes the Bayside work for this stage, and the options for staying on the street without staying in a house that's fighting you.",
    date="2026-09-17", category="Living on the Bayside", image="blog/is-the-bayside-a-good-place-to-retire.jpg",
    image_alt="An older couple seen from behind on the Wynnum esplanade path at dawn, the jetty and the flat bay ahead, a bike leaning on the rail",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of real people.",
    label=("Stay on the street", "Retiring here"),
    card_title="Is the Bayside a good place to retire, and should you stay in the house?",
    card_blurb="Why so many do, and the honest question underneath: whether the highset with the stairs is the house to grow old in. Queensland's new livable housing standard, and the options for staying on the street.",
    about=["Retiring on the Bayside", "Livable Housing Design Standard", "Downsizing", "Living on the Bayside"],
    related=["weve-outgrown-the-house-but-we-love-the-street-what-are-the-options", "what-does-highset-mean-on-a-bayside-block", "is-wynnum-a-good-place-to-live"],
    cta="If the street is right and the stairs aren't, that's a design conversation. Nathan walks the house with you and talks about what a single-level life on the same block could look like.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Yes, and the census agrees with the people who live here: Manly's median age is 46 and Wynnum's 43, older than the newer suburbs behind them, and seven in ten homes in both are separate houses on their own block. The flat esplanade path, the water, the train to town, a village you can walk to and neighbours you've had for thirty years are the reasons.</p>
        <p>The honest question is the house. Most Bayside houses are highsets with a flight of stairs to the front door and another inside, bathrooms from the 1960s, and a built-in-under nobody would design today. That's fine at fifty-five. It's the reason people leave streets they love at seventy-five.</p>
        <p>Since 1 October 2023, every new home in Queensland has had to meet the Livable Housing Design Standard: a step-free entry, wider doors and corridors on the entry level, and bathroom walls built to take grabrails later. A house built now is built for the next thirty years by law. That changes what &ldquo;stay or go&rdquo; means.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#why-here">Why do people retire here?</a></li>
          <li><a href="#the-house">Why is the house the real question?</a></li>
          <li><a href="#the-standard">What does the livable housing standard require?</a></li>
          <li><a href="#options">What are the options for staying on the street?</a></li>
          <li><a href="#when-to-go">When is moving the right answer?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="why-here">Why do people retire here?</h2>
      <ul class="pts">
        <li><strong>The foreshore is flat.</strong> The esplanade path from Wynnum to Manly is level, shaded and long, and it's where half the suburb walks in the morning.</li>
        <li><strong>The water.</strong> The wading pool, the jetty, the boat harbour, the club. Things to do that don't cost much and don't need a car.</li>
        <li><strong>The train.</strong> The Cleveland line to the city for the things the suburb doesn't have.</li>
        <li><strong>The village.</strong> Wynnum's main street and Manly's Cambridge Parade: shops, cafés, the doctor, the chemist, walkable.</li>
        <li><strong>The people.</strong> A suburb where the median age is in the forties is a suburb with a lot of people who've been here a long time.</li>
      </ul>

      <blockquote class="proof">
        <p><b>In the 2021 Census Manly's median age was 46 and Wynnum's 43; 70.6% of Manly's dwellings and 70.8% of Wynnum's were separate houses.</b></p>
        <cite>Australian Bureau of Statistics, 2021 Census QuickStats, Manly (Qld) and Wynnum (Qld). Older than the newer suburbs behind them, and living in houses on their own blocks.</cite>
      </blockquote>

      <h2 class="h2" id="the-house">Why is the house the real question?</h2>
      <p>Because the suburb is built for this stage and the houses mostly aren't.</p>
      <p>A highset has stairs to the front door and stairs inside. A 1960s bathroom is a step up, a narrow door and a bath you climb into. Corridors were built to the widths of the day. The built-in-under, if that's where the second bedroom is, means a flight every time. None of that is a problem until the day it is, and that day tends to arrive without warning.</p>
      <p>The families we hear from aren't asking whether to leave the Bayside. They're asking how to stay on a block they own, in a street they know, in a house that doesn't need two good knees.</p>

      <h2 class="h2" id="the-standard">What does the livable housing standard require?</h2>
      <p>Queensland adopted the National Construction Code's Livable Housing Design Standard for new homes from 1 October 2023. In plain words, a new house has to have:</p>
      <ul class="pts">
        <li><strong>A level, step-free entry</strong> from the access path to at least one entrance door.</li>
        <li><strong>Internal doors and corridors on the entry level</strong> wide enough for unimpeded movement between spaces.</li>
        <li><strong>A toilet on the entry level</strong>, subject to some exemptions.</li>
        <li><strong>Bathroom, shower and bath walls built so grabrails can be fitted later</strong> without pulling the linings off.</li>
      </ul>
      <p>There are time-limited exemptions for some narrow, small and steep lots, and protections for the traditional Queenslander, running to 30 September 2026. On a typical Bayside block, though, a new house is now designed for ageing in place whether or not anyone asked for it. That's a quiet, useful change to the stay-or-go sum.</p>

      <h2 class="h2" id="options">What are the options for staying on the street?</h2>
      <ul class="pts">
        <li><strong>Rebuild single-level, or with everything you need on the entry level.</strong> A new house designed to the standard, on the block you own, with the living, the main bedroom and a proper bathroom on one floor. On a flood-overlay block, that entry level may be raised, with a lift or a ramp designed in rather than bolted on.</li>
        <li><strong>A secondary dwelling.</strong> A smaller single-level home on the same block: for you, with the family in the main house, or the reverse. City Plan's definition of a house allows two dwellings on a lot where one is secondary. <a href="../weve-outgrown-the-house-but-we-love-the-street-what-are-the-options/">The options post covers it.</a></li>
        <li><strong>Renovate the ground floor.</strong> On a highset with a sound built-in-under and enough ceiling height, a proper ground-floor bedroom and bathroom can turn the stairs into a choice rather than a necessity. It depends on the ceiling height, the flood level and what's in the walls.</li>
        <li><strong>Sell the big block, buy the small one on the same street.</strong> Not a building job, and sometimes the right one.</li>
      </ul>

      <h2 class="h2" id="when-to-go">When is moving the right answer?</h2>
      <p>When the things that made the Bayside right have stopped mattering, when the block can't take what's needed, or when the years living somewhere else during a rebuild aren't something you want to spend. We'll say so at the walk-through if that's what we see. The point of the list above is that leaving isn't the only way to fix a house that no longer fits.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>The Bayside is built for this stage:</b> flat foreshore, water, train, village, long-standing neighbours.</li>
          <li><b>The houses mostly aren't.</b> Stairs, narrow doors, 1960s bathrooms, built-in-unders.</li>
          <li><b>Every new Queensland home since October 2023 must meet the livable housing standard:</b> step-free entry, wider doors, grabrail-ready walls.</li>
          <li><b>Four ways to stay on the street:</b> rebuild to one level, a secondary dwelling, a ground-floor renovation, or a smaller place on the same street.</li>
          <li><b>Leaving isn't the only fix</b> for a house that no longer fits.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can we build a single-level house on a flood-overlay block?</p>
          <p>It depends on the minimum floor level in council's report against the ground level. Sometimes a raised slab meets it; sometimes the living has to go up, and a lift or a ramp is designed in from the start. The report tells you which. <a href="../rebuilding-on-a-flood-overlay-block-on-the-bayside/">More here.</a></p>
        </div>
        <div>
          <p class="q">Does the livable housing standard make a house look institutional?</p>
          <p>No. Wider doors, a level entry and stronger bathroom walls are invisible in a well-designed house. They just mean you never have to think about it later.</p>
        </div>
        <div>
          <p class="q">Is a secondary dwelling allowed on our block?</p>
          <p>City Plan allows a secondary dwelling as part of a house, subject to the Dwelling house code's provisions, site cover, setbacks and the overlays on the lot. A designer checks it against your block; it's often the quiet answer on a big one.</p>
        </div>
        <div>
          <p class="q">What if we're not sure which option is ours?</p>
          <p>One walk-through. Nathan looks at the house, the block, the flood report and the stairs, and tells you what's open and what he'd do.</p>
        </div>
      </div>

      <p class="small sources">Sources: Australian Bureau of Statistics, 2021 Census QuickStats, Manly (Qld) and Wynnum (Qld); Queensland Department of Housing and Public Works and QBCC, <em>Livable Housing Design Standard</em> (NCC 2022, applying to new Queensland homes from 1 October 2023, with transitional exemptions to 30 September 2026); Brisbane City Council, <em>Building a new house: approvals and requirements</em> (definition of a house) and <em>FloodWise Property Reports</em>. Read 17 September 2026. Plain-English guidance from a builder; not financial, health or planning advice.</p>
''')
