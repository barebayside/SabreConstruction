# Phase 3 of docs/reference/article-bank.md — the place cluster (Spiral 2), part B: R27, R28, R29, R31, R35.
# Every post ends at the house. Sources read 2026-09-17: ABS 2021 Census (Manly West SAL31749 read on abs.gov.au;
# Lota SAL31686; other suburb totals as published by the ABS and recorded on Wikipedia), Brisbane City Council
# "Brisbane Severe Weather Alert", Get Ready Queensland "Protect your home", Wikipedia suburb histories,
# SLQ "Housing a growing state" 2014, asbestos.qld.gov.au. No prices, no bands.

POSTS = {}

# ---------------------------------------------------------------- R27 · Manly vs Manly West
POSTS["r27-manly-west"] = dict(
    slug="whats-the-difference-between-manly-and-manly-west",
    section="suburbs",
    title="What's the difference between Manly and Manly West?",
    h1="What's the difference between<br>Manly and Manly West?",
    description="Manly is the harbour suburb of 4,273 people; Manly West is the inland suburb of 12,436 that was split off it in 1975. Different age, different housing, different schools, and a different kind of block to build on.",
    lede="One's on the water and one isn't, and that's only the start. Manly West was part of Manly until 1975, and the fifty years since have made them different suburbs with the same name. Here's what actually differs, and what it means if you're building in either.",
    date="2026-09-17", category="Living on the Bayside", image="blog/whats-the-difference-between-manly-and-manly-west.jpg",
    image_alt="Looking down a Manly hill street to the boat harbour, the flatter suburb inland behind",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of the real street.",
    label=('One suburb until 1975', 'Manly or Manly West'),
    figure=dict(image="blog/whats-the-difference-between-manly-and-manly-west.png", alt='Map of Manly and Manly West, one suburb until 1975', caption='Boundaries &copy; OpenStreetMap contributors.', after='how-they-split'),
    card_title="What's the difference between Manly and Manly West?",
    card_blurb="Manly is the harbour suburb of 4,273 people; Manly West is the inland one of 12,436, split off in 1975. Different age, housing, schools, and a different block to build on.",
    about=["Manly", "Manly West", "Living on the Bayside"],
    related=["wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family", "schools-on-the-bayside-catchments", "what-are-bayside-houses-made-of"],
    cta="Either side of the line, if the block is right and the house isn't, he'll walk it with you.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Manly is the small coastal suburb around the boat harbour and the esplanade: 4,273 people at the 2021 Census, median age 46, a village on Cambridge Parade, a primary school and no high school.</p>
        <p>Manly West is the much larger suburb inland of it: 12,436 people, median age 41, more families with children, more separate houses, two state primaries and the Moreton Bay colleges. It was part of Manly until it was gazetted as its own suburb in 1975.</p>
        <p>Same postcode, same train line, same name on the letterbox &mdash; but a different feel, a different housing stock, and different rules on the block. Manly's blocks climb the hill and carry the storm tide levels near the water; Manly West's are flatter, later, and more often brick.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#how-they-split">How did one suburb become two?</a></li>
          <li><a href="#numbers">What do the numbers say?</a></li>
          <li><a href="#feel">What do they feel like?</a></li>
          <li><a href="#schools">What about schools?</a></li>
          <li><a href="#houses">What are the houses like in each?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="how-they-split">How did one suburb become two?</h2>
      <p>Manly started as the Manly Beach Estate, auctioned in 1882 and named, apparently, after the Sydney beach. It grew along the water and up the hill behind it. The land further west stayed farms and bush much longer, and filled with houses after the war.</p>
      <p>In 1975 the western part was officially gazetted as its own suburb, Manly West. Manly West State School had already opened there in 1958, and Wondall Heights in 1966, which tells you when the streets went in.</p>

      <h2 class="h2" id="numbers">What do the numbers say?</h2>
      <div class="tablewrap">
        <table>
          <thead><tr><th>2021 Census</th><th>Manly</th><th>Manly West</th></tr></thead>
          <tbody>
            <tr><td>People</td><td>4,273</td><td>12,436</td></tr>
            <tr><td>Median age</td><td>46</td><td>41</td></tr>
            <tr><td>Couple families with children</td><td>41.9%</td><td>47.4%</td></tr>
            <tr><td>Separate houses</td><td>70.6%</td><td>78.0%</td></tr>
            <tr><td>By road from the CBD</td><td>19.9 km</td><td>17.6 km</td></tr>
          </tbody>
        </table>
      </div>

      <blockquote class="proof">
        <p><b>Manly West: 12,436 people, median age 41, 47.4% couple families with children, 78.0% separate houses. Manly: 4,273 people, median age 46, 41.9% and 70.6%.</b></p>
        <cite>Australian Bureau of Statistics, 2021 Census QuickStats, Manly West and Manly (Qld). Three times the people, five years younger, more kids, more houses. That's the whole difference in one row.</cite>
      </blockquote>

      <h2 class="h2" id="feel">What do they feel like?</h2>
      <p><strong>Manly</strong> is the harbour. The 41.8-hectare boat harbour, the esplanade, the village, the breeze off the water in the afternoon, and a population that skews older and has been there a long time. It's the suburb people picture when they say &ldquo;the Bayside.&rdquo;</p>
      <p><strong>Manly West</strong> is where the families are. Bigger, flatter, more suburban, with Manly Road running through it, the two colleges, the two state primaries, and streets of houses that went up from the late 1950s on. You don't see the water from most of it. You can get to it in five minutes.</p>

      <h2 class="h2" id="schools">What about schools?</h2>
      <p>Manly has Manly State School (opened 1910) and no secondary school; the nearest state high is Wynnum State High on the boundary with Wynnum.</p>
      <p>Manly West has Manly West State School and Wondall Heights State School, plus Moreton Bay College and Moreton Bay Boys' College. Which catchment an address falls in follows the streets, not the suburb name &mdash; <a href="../schools-on-the-bayside-catchments/">check it on EdMap</a>.</p>

      <h2 class="h2" id="houses">What are the houses like in each?</h2>
      <p>This is where the 1975 line matters to a builder.</p>
      <p><strong>Manly's</strong> houses are older on average and more mixed: pre-war timber on the streets near the harbour, post-war cottages, highsets on the hill, and a sixth of dwellings now flats near the water. The blocks slope, and the ones near the esplanade carry council's storm tide levels. A rebuild in Manly is a design job: the fall, the aspect, the floor height. <a href="../rebuilding-on-a-flood-overlay-block-on-the-bayside/">What an overlay does to a design is here.</a></p>
      <p><strong>Manly West's</strong> houses are later and more uniform: the 1960s highset and, from the 1970s, brick veneer on a slab. The blocks are flatter and more regular, and the housing is at the age where kitchens and bathrooms have been done twice and the layout still doesn't fit. A rebuild in Manly West is more often a straightforward flat-block job, and the question is whether a brick house on a slab can be changed enough to be worth keeping. <a href="../what-are-bayside-houses-made-of/">Usually the honest answer is in what it's made of.</a></p>
      <p>Either way, the families we meet on both sides of the line are the same family: right street, wrong house.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Manly West was part of Manly until 1975.</b> Fifty years on, they're different suburbs.</li>
          <li><b>Manly is the harbour: smaller, older, a village.</b> Manly West is three times the people, younger, more families.</li>
          <li><b>Manly has no high school;</b> Manly West has two primaries and the two colleges.</li>
          <li><b>Manly's blocks slope and carry storm tide levels;</b> Manly West's are flatter, later and more brick.</li>
          <li><b>The rebuild conversation is the same on both sides:</b> the street is right and the house isn't.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Do they share a postcode?</p>
          <p>Yes, 4179, along with Lota. Which is part of why people mix them up.</p>
        </div>
        <div>
          <p class="q">Is Manly West on the water?</p>
          <p>No. It's inland of Manly and Lota. The water is a short drive or a long walk.</p>
        </div>
        <div>
          <p class="q">Which is better for a family?</p>
          <p>The census says more families with children choose Manly West, and it has the schools. Manly has the harbour and the village. It depends what you want to walk to.</p>
        </div>
        <div>
          <p class="q">Which is easier to rebuild in?</p>
          <p>Flat, regular blocks are easier, and Manly West has more of them. Manly's slopes and storm-tide lots need more design, and that's a cost question on each block, not a rule.</p>
        </div>
      </div>

      <p class="small sources">Sources: Australian Bureau of Statistics, 2021 Census QuickStats &mdash; <a href="https://abs.gov.au/census/find-census-data/quickstats/2021/SAL31749" rel="noopener">Manly West</a> and <a href="https://abs.gov.au/census/find-census-data/quickstats/2021/SAL31748" rel="noopener">Manly (Qld)</a>; suburb histories (Manly Beach Estate 1882, Manly West gazetted 1975, school dates) as recorded on Wikipedia from Queensland Government sources. Read 17 September 2026. Not planning or financial advice.</p>
''')

# ---------------------------------------------------------------- R28 · Lota
POSTS["r28-lota"] = dict(
    slug="lota-the-quiet-one-between-wynnum-and-manly",
    section="suburbs",
    title="Lota: the quiet one between Wynnum and Manly",
    h1="Lota: the quiet one<br>between Wynnum and Manly.",
    description="A suburb of 3,518 people where 95% of dwellings are separate houses and nearly half the families have kids at home. Its history, its one school, its station, and what its post-war houses are like to change.",
    lede="Lota is the Bayside suburb people drive through on the way to somewhere else, which is exactly why the people who live there like it. Here's what it is, how it got that way, and what its houses are like once you're inside one.",
    date="2026-09-17", category="Living on the Bayside", image="blog/lota-the-quiet-one-between-wynnum-and-manly.jpg",
    image_alt="A quiet Lota foreshore street: mangroves, the creek mouth, two old highsets and a heron",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of the real street.",
    label=('The Bayside suburbs', 'Lota'),
    figure=dict(image="blog/lota-the-quiet-one-between-wynnum-and-manly.png", alt='Map of Lota with its station, its school and Lota Creek', caption='Boundaries &copy; OpenStreetMap contributors.', after='what-it-is'),
    card_title="Lota: the quiet one between Wynnum and Manly",
    card_blurb="3,518 people, 95% separate houses, nearly half the families with kids at home. Its history, its one school and its station, and what its post-war houses are like to change.",
    about=["Lota", "Living on the Bayside"],
    related=["wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family", "what-are-bayside-houses-made-of", "why-are-so-many-bayside-houses-being-knocked-down"],
    cta="Lota's blocks are the kind we like best: flat, regular, and worth keeping. He'll walk yours with you.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Lota is the small residential suburb south of Manly, on the bay, with a station on the Cleveland line, one state primary school and not much else &mdash; which is the point.</p>
        <p>At the 2021 Census it had 3,518 people, a median age of 42, and the highest share of couple families with children of the three bayside suburbs at 48.8%. Almost every dwelling is a separate house: 95.3%, with flats at 0.7%.</p>
        <p>It was a pastoral estate in the 1860s, got its railway in 1889, was the end of the line from 1960 until the 1980s, and built up in the post-war decades with the small timber and fibro houses that now sit on some of the flattest blocks on the Bayside. That's the house story, and it's why Lota is quietly rebuilding.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-it-is">What is Lota?</a></li>
          <li><a href="#history">How did it get that way?</a></li>
          <li><a href="#living">What's it like to live in?</a></li>
          <li><a href="#houses">What are the houses like?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-it-is">What is Lota?</h2>
      <p>A suburb of houses. The train line runs through it from Manly to the south, over Lota Creek and into Ransome. Lota State School is on Richard Street. The esplanade runs along the bay with a seawall in front of it. Wynnum is two stations north; the Redlands start over the creek.</p>

      <blockquote class="proof">
        <p><b>Lota, 2021 Census: 3,518 people, median age 42, 48.8% couple families with children, 95.3% separate houses, 0.7% flats or apartments.</b></p>
        <cite>Australian Bureau of Statistics, 2021 Census QuickStats, Lota. Compare Wynnum and Manly at about 70% houses and 16% flats. Lota hasn't gone to units, and that decides how it feels.</cite>
      </blockquote>

      <h2 class="h2" id="history">How did it get that way?</h2>
      <p>The Quandamooka people knew Lota and Manly together as Narlung. In 1860 the land was acquired by William Duckett White, an Irish-born pastoralist and politician, in partnership for some of it with Queensland's first premier, Robert Herbert. The suburb takes its name from Lota House, which Duckett White built in 1863 at the heart of an estate growing sugar cane and fodder on the creek flats.</p>
      <p>The Cleveland railway opened through Lota in 1889. In 1960 the line beyond Lota closed, and for more than twenty years Lota was the end of the line, until it reopened in stages between 1983 and 1987. The seawall along the esplanade was built in 1931 as Depression relief work.</p>
      <p>Lota State School opened in 1952, which is the year that matters for the houses. The streets filled in the decade either side of it.</p>

      <h2 class="h2" id="living">What's it like to live in?</h2>
      <ul class="pts">
        <li><strong>Quiet.</strong> No main street, no harbour, no wading pool of its own. Those are in Manly and Wynnum, a few minutes away.</li>
        <li><strong>Flat.</strong> Old grid streets on flat ground, the kind you can ride a bike down.</li>
        <li><strong>Family.</strong> Nearly half the families have children at home, the highest on this stretch of coast.</li>
        <li><strong>Connected.</strong> One station, a forty-something-minute all-stops train to Central, and the Redlands over the creek. <a href="../how-far-is-wynnum-from-brisbane-cbd/">The timetable sample is here.</a></li>
        <li><strong>Honest about the bay.</strong> The tide goes out to mudflats, the esplanade carries storm tide levels near the water, and the salt works on everything. Same as the rest of the Bayside.</li>
      </ul>

      <h2 class="h2" id="houses">What are the houses like?</h2>
      <p>Post-war, mostly, and not much has replaced them yet.</p>

      <blockquote class="proof">
        <p><b>After 1946, when a Brisbane architect estimated a national shortfall of 300,000 houses, Brisbane's suburbs &ldquo;became populated with low-set timber houses on quarter acre blocks.&rdquo;</b></p>
        <cite>State Library of Queensland, <em>Housing a growing state</em>, 2014. Lota's school opened in 1952 and the streets around it are that era: small, light, fibro somewhere, on blocks the family has usually outgrown.</cite>
      </blockquote>

      <p>Walk Lota's streets and you'll find the post-war cottage, the 1960s highset with the rooms built in underneath, and a scattering of 1970s brick. Very little of the newer stock that changed the esplanade end of Wynnum. <a href="../what-are-bayside-houses-made-of/">What each type is made of is here.</a></p>
      <p>For a builder, that's a specific opportunity. Lota's blocks are flat and regular, on an old grid, near a station, in a suburb of houses with a school in it. The house on the block is often seventy years old, small, and clad in something from before 1990. The land carries the value. When a family has outgrown the cottage, the honest options on a block like that are a raise, an extension, or a new house designed for it &mdash; and the last one is why the demolition signs are starting to appear in Lota too. <a href="../why-are-so-many-bayside-houses-being-knocked-down/">Why it's happening across the Bayside is here.</a></p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Lota is a suburb of houses:</b> 95% separate dwellings, almost no flats. ABS 2021.</li>
          <li><b>It has the most families with kids</b> on this stretch of the bay.</li>
          <li><b>Pastoral estate 1860s, railway 1889, end of the line 1960&ndash;1980s, school 1952.</b> The houses are that last date.</li>
          <li><b>Flat, regular blocks near a station</b> with seventy-year-old houses on them.</li>
          <li><b>Raise, extend or rebuild</b> &mdash; the block is worth keeping either way.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Does Lota have shops?</p>
          <p>Not a main street. Manly's village and Wynnum's centre are a few minutes away, and most families treat them as their own.</p>
        </div>
        <div>
          <p class="q">Is there a high school in Lota?</p>
          <p>No. The nearest state secondary is Wynnum State High School. <a href="../schools-on-the-bayside-catchments/">The catchments are here.</a></p>
        </div>
        <div>
          <p class="q">Does Lota flood?</p>
          <p>The esplanade end carries storm tide mapping, and Lota Creek runs along the southern boundary. Council maps every lot; read the FloodWise report for your address. <a href="../does-wynnum-flood/">How to read it is here.</a></p>
        </div>
        <div>
          <p class="q">Is Lota in the character overlay?</p>
          <p>Some streets may be; it's mapped street by street. Most of Lota's houses are post-war and outside the pre-1947 rules, but <a href="../check-if-your-street-is-in-the-character-overlay/">check your own address</a> before you plan anything.</p>
        </div>
      </div>

      <p class="small sources">Sources: Australian Bureau of Statistics, <a href="https://abs.gov.au/census/find-census-data/quickstats/2021/SAL31686" rel="noopener">2021 Census QuickStats, Lota</a>; Lota history (Lota House 1863, railway 1889 and 1960&ndash;87, seawall 1931, school 1952, Narlung) as recorded on Wikipedia from Queensland Government and Brisbane City Council sources; State Library of Queensland, <em>Housing a growing state</em>, 2014. Read 17 September 2026. Not planning or financial advice.</p>
''')

# ---------------------------------------------------------------- R29 · Wakerley and Gumdale
POSTS["r29-wakerley"] = dict(
    slug="wakerley-and-gumdale-the-newer-bayside",
    section="suburbs",
    title="Wakerley and Gumdale: the newer Bayside, and what you give up for it",
    h1="Wakerley and Gumdale: the newer Bayside,<br>and what you give up for it.",
    description="Wakerley is the estate suburb, Gumdale the acreage one. Newer houses, bigger blocks, no state school inside Wakerley, no train, and no water at the end of the street. An honest comparison with the old bayside suburbs.",
    lede="Drive ten minutes inland from Wynnum and the Bayside changes. The houses are newer, the blocks bigger, the streets curve. Wakerley and Gumdale are what families choose when they want space over the water. Here's what you get, what you give up, and what the houses are like.",
    date="2026-09-17", category="Living on the Bayside", image="blog/wakerley-and-gumdale-the-newer-bayside.jpg",
    image_alt="A wide new street of two-storey homes with bushland at the end, a parent and child on bikes",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of the real street.",
    label=('The newer Bayside', 'Wakerley &amp; Gumdale'),
    figure=dict(image="blog/wakerley-and-gumdale-the-newer-bayside.png", alt='Map of Wakerley and Gumdale with the nearest schools; no station', caption='Boundaries &copy; OpenStreetMap contributors.', after='what-they-are'),
    card_title="Wakerley and Gumdale: the newer Bayside, and what you give up for it",
    card_blurb="Wakerley is the estate suburb, Gumdale the acreage one. Newer houses, bigger blocks, no state school in Wakerley, no train, no water at the end of the street. The honest trade.",
    about=["Wakerley", "Gumdale", "Living on the Bayside"],
    related=["ransome-tingalpa-and-gumdale-the-acreage-edge-of-the-bayside", "wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family", "schools-on-the-bayside-catchments"],
    cta="On a big Wakerley or Gumdale block the question is usually what to build, not whether. He'll walk it with you.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Wakerley and Gumdale are the inland, newer half of the Bayside. Wakerley, 8,718 people at the 2021 Census, is the estate suburb: houses mostly from the last thirty years on curved streets, with no state school inside its boundary and no station. Gumdale, 2,298 people, is the acreage suburb next door, with its own state primary and blocks measured in acres rather than square metres.</p>
        <p>What you get is space, newer houses, and blocks the old bayside suburbs can't offer. What you give up is the water at the end of the street, the train, the walkable village, and the seventy-year-old street grid that makes Wynnum, Manly and Lota feel like towns.</p>
        <p>For a builder the difference is the block. Old-bayside rebuilds are about replacing a small house on good land. Wakerley and Gumdale builds are more often about what to do with a lot of land.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-they-are">What are Wakerley and Gumdale?</a></li>
          <li><a href="#what-you-get">What do you get?</a></li>
          <li><a href="#what-you-give-up">What do you give up?</a></li>
          <li><a href="#schools">What about schools?</a></li>
          <li><a href="#houses">What are the houses like, and what gets built?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-they-are">What are Wakerley and Gumdale?</h2>
      <p><strong>Wakerley</strong> is named after an early settler, John William Wakerley. There's a photograph from 1927 of a family in front of a house made of kerosene tins there, which tells you how recently it was bush. It's 17.7 kilometres by road east of the CBD, between Manly West and the acreage suburbs, and it grew fast: 7,804 people in 2011, 8,718 in 2021.</p>
      <p><strong>Gumdale</strong>, south of it, is Brisbane's nearest acreage suburb to the city by most people's reckoning: 2,298 people spread across large blocks, a state primary school, and a rural feel a quarter of an hour from the bay.</p>

      <blockquote class="proof">
        <p><b>Wakerley: 8,718 people at the 2021 Census. Gumdale: 2,298. Manly West, between them and the water: 12,436.</b></p>
        <cite>Australian Bureau of Statistics, 2021 Census. Wakerley has grown by close to a thousand people in a decade. The old bayside suburbs barely move.</cite>
      </blockquote>

      <h2 class="h2" id="what-you-get">What do you get?</h2>
      <ul class="pts">
        <li><strong>Newer houses.</strong> Most of Wakerley's housing is from the last few decades: brick or rendered, on slabs, with garages and ensuites the post-war cottage never had.</li>
        <li><strong>Bigger blocks.</strong> Estate lots in Wakerley; acres in Gumdale.</li>
        <li><strong>Room.</strong> For the shed, the pool, the second living area, the caravan.</li>
        <li><strong>The colleges.</strong> Moreton Bay College and Moreton Bay Boys' College are in Manly West, next door.</li>
        <li><strong>The Gateway.</strong> The motorway is close, which matters if the commute is north or south rather than into the city.</li>
      </ul>

      <h2 class="h2" id="what-you-give-up">What do you give up?</h2>
      <ul class="pts">
        <li><strong>The water.</strong> It's a drive, not a walk. The wading pool, the jetty and the harbour belong to the old suburbs.</li>
        <li><strong>The train.</strong> No station in Wakerley or Gumdale. The Cleveland line runs through Wynnum, Manly and Lota.</li>
        <li><strong>The village.</strong> There's no Bay Terrace or Cambridge Parade. Shops are shopping centres.</li>
        <li><strong>A state school inside Wakerley.</strong> There isn't one. Next section.</li>
        <li><strong>The old grid.</strong> Curved streets and cul-de-sacs are quieter, and they're also longer to walk out of.</li>
      </ul>

      <h2 class="h2" id="schools">What about schools?</h2>
      <p>Wakerley has no government school inside its boundary. The nearest state primaries are Gumdale State School to the south and Manly West State School to the north-east; the nearest state secondary is Brisbane Bayside State College in Wynnum West. Which catchment a Wakerley address falls in depends on the street. <a href="../schools-on-the-bayside-catchments/">Check EdMap.</a></p>
      <p>Gumdale has its own state primary. The independent colleges in Manly West serve both.</p>

      <h2 class="h2" id="houses">What are the houses like, and what gets built?</h2>
      <p>This is where the two halves of the Bayside are different jobs.</p>
      <p>In Wynnum, Manly and Lota the house is usually the problem and the land is the prize: a small post-war cottage or a tired highset on a flat block near the water, with the family grown out of it. <a href="../why-are-so-many-bayside-houses-being-knocked-down/">That's the classic knockdown rebuild.</a></p>
      <p>In Wakerley the houses are newer, so the knockdown case is rarer. The work there is more often an extension, a second storey, or a big renovation on a house that's structurally fine but was built to a project-home plan that doesn't suit the family. On a brick-on-slab house that's a design-and-engineering question, and worth asking early.</p>
      <p>In Gumdale the block is the brief. An acreage lot can carry a house designed from scratch for the site: the aspect, the fall, the trees, where the shed and the pool go. It's the one part of the Bayside where a family can build a house that isn't shaped by what was there before.</p>
      <p>Different jobs, same rule: the design starts with the block. A plan picked from a range doesn't know it's on an acre, any more than it knows it's on a storm tide lot in Manly.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Wakerley is the estate suburb, Gumdale the acreage one.</b> Newer, bigger, inland.</li>
          <li><b>You get space and newer houses.</b> You give up the water, the train and the village.</li>
          <li><b>No state school inside Wakerley;</b> Gumdale and Manly West primaries, Brisbane Bayside State College for secondary.</li>
          <li><b>Old-bayside rebuilds replace a small house on good land.</b> Wakerley work is more often extension; Gumdale is building to the block.</li>
          <li><b>Either way, the design starts with the block,</b> not a plan from a range.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Is Wakerley part of the Bayside?</p>
          <p>Depends who you ask. It's in the same pocket, next to Manly West, and most people count it. It just isn't on the bay.</p>
        </div>
        <div>
          <p class="q">Can we knock down and rebuild in Wakerley?</p>
          <p>Yes, if the numbers work. With newer houses the sums often favour extending instead. A builder who does both will tell you which yours is; we do both.</p>
        </div>
        <div>
          <p class="q">Is Gumdale really acreage?</p>
          <p>Mostly. It's known for large lots and a rural feel, with some newer smaller subdivisions at the edges. Check the lot size on the title, not the suburb name.</p>
        </div>
        <div>
          <p class="q">Are there flood overlays out there?</p>
          <p>Creek and overland flow mapping runs inland too. Read the FloodWise report for the specific lot. <a href="../does-wynnum-flood/">How to read one is here.</a></p>
        </div>
      </div>

      <p class="small sources">Sources: Australian Bureau of Statistics, 2021 Census populations for Wakerley, Gumdale and Manly West (Manly West read on abs.gov.au, SAL31749; others as published by the ABS and recorded on Wikipedia); Wakerley and Gumdale histories and school facts as recorded on Wikipedia from Queensland Government sources. Read 17 September 2026. Not planning or financial advice.</p>
''')

# ---------------------------------------------------------------- R31 · storm season
POSTS["r31-storms"] = dict(
    slug="bayside-storm-season-roof-trees-insurance",
    section="living",
    title="Bayside storm season: what it means for your roof, your trees and your insurance",
    h1="Bayside storm season: what it means for<br>your roof, your trees and your insurance.",
    description="Brisbane's storm season runs October to March. What Get Ready Queensland says to check on a house before it starts, what a builder looks at on an old Bayside house, and why the storm is often the first honest look at the roof.",
    lede="Every October the afternoons get heavy, and every Bayside house gets tested. Here's what council and the state say to check before the season, what a builder actually looks at on a seventy-year-old house, and why the first big storm is often the day a family decides about the house.",
    date="2026-09-17", category="Living on the Bayside", image="blog/bayside-storm-season-roof-trees-insurance.jpg",
    image_alt="A highset Bayside house under a dark storm sky, gutters overflowing, a gum bending toward the roof",
    image_caption="Illustration in the style of Sabre's story frames.",
    label=('October to March', 'Storm season'),
    card_title="Bayside storm season: what it means for your roof, your trees and your insurance",
    card_blurb="October to March, every year. What Get Ready Queensland says to check before it starts, what a builder looks at on an old Bayside house, and why the storm is the first honest look at the roof.",
    about=["Storm season", "Brisbane Bayside", "Home maintenance"],
    related=["what-are-bayside-houses-made-of", "does-wynnum-flood", "is-wynnum-a-good-place-to-live"],
    cta="If the last storm told you something about the house you didn't want to know, that's a walk-through, not a panic.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Brisbane City Council puts storm season at October to March, and tells you to prepare for heavy rain, strong winds and hail. On the Bayside add the salt-laden wind off the bay, and the trees.</p>
        <p>Before it starts, the state's Get Ready Queensland checklist is short: check the roof and repair it; keep gutters and downpipes clear; trim trees and branches near the buildings; fix rust, loose fittings and rotting or termite-affected timber; secure loose items; check the insurance covers the house and contents.</p>
        <p>On an old Bayside house, three of those six are the whole story. Roofing screws and gutters rust in salt air. Timber rots where the paint failed. And the roof is the part nobody has looked at in years. Storm season is when a house tells you the truth about itself.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#when">When is storm season, and what does it bring?</a></li>
          <li><a href="#checklist">What does the state say to check?</a></li>
          <li><a href="#roof">What does a builder look at on an old Bayside roof?</a></li>
          <li><a href="#trees">What about the trees?</a></li>
          <li><a href="#insurance">What about insurance?</a></li>
          <li><a href="#the-house">Why the storm is often the decision</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="when">When is storm season, and what does it bring?</h2>

      <blockquote class="proof">
        <p><b>&ldquo;Storm season typically lasts from October to March. During this time, prepare for potential heavy rain, strong winds, hail and other severe weather conditions.&rdquo;</b></p>
        <cite>Brisbane City Council, <em>Brisbane Severe Weather Alert</em>. Council runs an alert service for severe storms and flooding in the Brisbane area; sign up before October, not during it.</cite>
      </blockquote>

      <p>On the Bayside the storms arrive from the west and south-west in the late afternoon, and the wind that follows comes off the bay carrying salt. That combination &mdash; a hot day, a black sky at four o'clock, hail, then a night of salt wind &mdash; is the Bayside summer. Houses here are built for it or they aren't.</p>

      <h2 class="h2" id="checklist">What does the state say to check?</h2>

      <blockquote class="proof">
        <p><b>&ldquo;Check the condition of your roof and repair if needed.&rdquo; &ldquo;Keep gutters and downpipes clear of leaves and other blockages.&rdquo; &ldquo;Trim trees and branches that are close to your buildings.&rdquo; &ldquo;Fix any rust, loose fittings and rotting or termite-affected timber.&rdquo; &ldquo;Secure loose items that could cause damage if blown around in high winds.&rdquo; &ldquo;Make sure to check your insurance policy has enough cover for your home and contents.&rdquo;</b></p>
        <cite>Get Ready Queensland, <em>Protect your home</em>, Queensland Government. Six lines. On a post-war Bayside house, the first and the fourth are the ones that cost money.</cite>
      </blockquote>

      <h2 class="h2" id="roof">What does a builder look at on an old Bayside roof?</h2>
      <p>The state says &ldquo;check the roof.&rdquo; Here's what that means when the roof is sixty years old and three streets from the bay.</p>
      <ul class="pts">
        <li><strong>The screws and the sheets.</strong> Salt air corrodes roofing screws from the head down. A sheet that's held by rust is a sheet that lifts in a gust.</li>
        <li><strong>The gutters.</strong> Old steel gutters rust through at the joins and behind the fascia, where nobody sees it until the water is running down the inside of the wall.</li>
        <li><strong>The flashings.</strong> Around the chimney, the vent pipes, the change of pitch. The places a roof leaks are rarely the middle of a sheet.</li>
        <li><strong>The battens and the frame.</strong> Under the sheets, in a hardwood-framed house, the battens may be fine at seventy. Where the roof has leaked for years, they aren't.</li>
        <li><strong>Tiles.</strong> On a 1970s brick house, cracked tiles, slipped ridge capping and mortar that's gone to sand. Hail finds all three.</li>
      </ul>
      <p>A roof plumber can fix most of this. What they can't fix is a roof that's at the end of its life on a house that's at the end of its life, and that's the conversation storm season starts.</p>

      <h2 class="h2" id="trees">What about the trees?</h2>
      <p>The Bayside's old suburbs have old trees, and the state's advice is to trim the ones close to the buildings. Two things to know locally.</p>
      <ul class="pts">
        <li><strong>Some trees are protected.</strong> Brisbane City Council has vegetation protection rules, and some trees on private land can't be removed without approval. Check before you cut, not after.</li>
        <li><strong>The tree that falls is usually the neighbour's.</strong> Talk to them in September, not in the dark in December.</li>
      </ul>
      <p>If you're planning a rebuild, the trees on the block are one of the first things a builder and a designer look at &mdash; what stays, what's protected, what the new house has to be designed around.</p>

      <h2 class="h2" id="insurance">What about insurance?</h2>
      <p>We're builders, not insurers, so this is short. The state's checklist says make sure the policy has enough cover for the house and contents. Two things a builder would add:</p>
      <ul class="pts">
        <li><strong>Insure the rebuild cost, not the purchase price.</strong> On the Bayside the land is most of the value; the house is what the insurer pays to replace. Ask your insurer how they set the sum insured.</li>
        <li><strong>Tell them what the house is.</strong> Age, construction, roof type, whether it's been rewired. A new house designed to current standards and flood levels is a different risk from a 1960s house that wasn't, and it's worth saying so.</li>
      </ul>

      <h2 class="h2" id="the-house">Why the storm is often the decision</h2>
      <p>Here's the pattern. A family has been meaning to do something about the house for years. Then a storm lifts a sheet, or the gutter gives up and the water comes through the ceiling, or the tree comes down on the carport. The insurer sends someone. The someone says the roof needs replacing, and while they're up there, the frame under it has been wet for a decade.</p>
      <p>Now the family is pricing a new roof on a small old house with fibro walls and one bathroom, on a block that's worth more than the house. And they ask the question that was always coming: is this the house we want to spend that on?</p>
      <p>Sometimes yes. A sound hardwood house with a new roof has decades in it. Sometimes no, and the storm has just told them what a builder would have. <a href="../why-are-so-many-bayside-houses-being-knocked-down/">Why that answer is so common on the Bayside is here.</a> Either way, the honest thing is to get the whole house looked at, not just the roof, before the money goes anywhere.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>October to March, every year.</b> Heavy rain, wind, hail &mdash; plus salt wind off the bay.</li>
          <li><b>The state's list is six lines:</b> roof, gutters, trees, rust and rot, loose items, insurance.</li>
          <li><b>On an old Bayside house the roof is the story.</b> Screws, gutters, flashings, and what's under them.</li>
          <li><b>Check before you cut a tree.</b> Some are protected, and the one that falls is usually next door's.</li>
          <li><b>The storm often starts the house decision.</b> Get the whole house looked at before the roof money goes anywhere.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">When should we do the checks?</p>
          <p>September, before council's October start. Roof plumbers and arborists are booked out once the first storm has been through.</p>
        </div>
        <div>
          <p class="q">Can we clean the gutters ourselves?</p>
          <p>On a lowset, many people do. On a highset, it's a ladder job at height, and on a pre-1990 house the eaves may be fibro &mdash; don't drill, cut or pressure-wash them. <a href="../what-asbestos-removal-means-for-a-knockdown-rebuild/">The asbestos rules are here.</a></p>
        </div>
        <div>
          <p class="q">Does a new house handle storms better?</p>
          <p>It's built to the current wind, water and flood requirements, with new fixings and flashings, and designed for the block. That's not a guarantee against a big storm; it's a different starting point.</p>
        </div>
        <div>
          <p class="q">Should we wait until after storm season to start a build?</p>
          <p>Ask your builder how they sequence the roof. A house that's framed and roofed before the wet is a different job from one that's open to it, and that's a scheduling conversation, not a rule.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <a href="https://www.brisbane.qld.gov.au/community-support-and-safety/natural-disasters-and-emergencies/brisbane-severe-weather-alert" rel="noopener">Brisbane Severe Weather Alert</a>; Get Ready Queensland, <a href="https://www.getready.qld.gov.au/getting-ready/protect-your-home" rel="noopener">Protect your home</a>, Queensland Government. Read 17 September 2026. The roof and tree observations are a builder's, not an inspection of any particular house. Not insurance, arboricultural or legal advice.</p>
''')

# ---------------------------------------------------------------- R35 · Ransome, Tingalpa and Gumdale
POSTS["r35-ransome"] = dict(
    slug="ransome-tingalpa-and-gumdale-the-acreage-edge-of-the-bayside",
    section="suburbs",
    title="Ransome, Tingalpa and Gumdale: the acreage edge of the Bayside",
    h1="Ransome, Tingalpa and Gumdale:<br>the acreage edge of the Bayside.",
    description="Where the Bayside stops being suburbs. Ransome, Sabre's home suburb of 429 people, Tingalpa's post-war streets, and Gumdale's acreages. What each is, and what gets built there.",
    lede="South and west of the bayside suburbs, the blocks get bigger and the streets get fewer. This is where Sabre lives now, at Ransome, and it's the part of the Bayside almost nobody writes about. Here's what these three places are, and what it's like to build in them.",
    date="2026-09-17", category="Living on the Bayside", image="blog/ransome-tingalpa-and-gumdale-the-acreage-edge-of-the-bayside.jpg",
    image_alt="An acreage block: a long gravel drive, post-and-rail fences, big gums, a horse, the house set well back",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of the real street.",
    label=('The acreage edge', 'Ransome &middot; Tingalpa &middot; Gumdale'),
    figure=dict(image="blog/ransome-tingalpa-and-gumdale-the-acreage-edge-of-the-bayside.png", alt="Map of Ransome, Tingalpa and Gumdale with Sabre's base at 40 Molle Road marked", caption='Boundaries &copy; OpenStreetMap contributors.', after='ransome'),
    card_title="Ransome, Tingalpa and Gumdale: the acreage edge of the Bayside",
    card_blurb="Where the Bayside stops being suburbs. Ransome (Sabre's home, 429 people), Tingalpa's post-war streets, and Gumdale's acreages. What each is, and what gets built there.",
    about=["Ransome", "Tingalpa", "Gumdale", "Living on the Bayside"],
    related=["wakerley-and-gumdale-the-newer-bayside", "what-are-bayside-houses-made-of", "who-are-the-small-independent-builders-on-brisbanes-bayside"],
    cta="We're at 40 Molle Road, Ransome. If you're building anywhere on this edge of the Bayside, you're a few minutes from the shed.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Three places, three different things. <strong>Ransome</strong> is a tiny coastal suburb of 429 people on the Redland boundary, most of it undeveloped reserve along the bay, with two small residential pockets &mdash; and now Sabre's home base at 40 Molle Road. <strong>Tingalpa</strong> is a proper post-war suburb of 8,461 people, closer to the city than any of the bayside suburbs, that nearly tripled in size between 1954 and 1980. <strong>Gumdale</strong> is the acreage suburb, 2,298 people on large lots, with its own state school.</p>
        <p>What they share is the edge: big blocks, older subdivisions, creeks and bushland, and no water at the end of the street. For a builder they're three different jobs &mdash; the post-war rebuild in Tingalpa, the acreage design in Gumdale, and the quiet, rare block in Ransome.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#ransome">Ransome: the suburb that's mostly reserve</a></li>
          <li><a href="#tingalpa">Tingalpa: the post-war suburb closer to town</a></li>
          <li><a href="#gumdale">Gumdale: the acreage</a></li>
          <li><a href="#why-here">Why Sabre is based here</a></li>
          <li><a href="#houses">What gets built on this edge?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="ransome">Ransome: the suburb that's mostly reserve</h2>
      <p>Ransome is named after Charles Horace Ransome, who ran a sawmill in the area supplying firewood to the city and to Queensland Railways. It was officially named and bounded in August 1975, the same year Manly West was split from Manly.</p>
      <p>It borders Moreton Bay, but the coast is Ransome Reserve: undeveloped land with walking tracks that stop at the railway line. The people live in two small residential areas, one on Rickertt Road, and the suburb sits on the boundary with the City of Redland, 19.6 kilometres by road from the CBD.</p>

      <blockquote class="proof">
        <p><b>Ransome: 429 people at the 2021 Census. Tingalpa: 8,461. Gumdale: 2,298.</b></p>
        <cite>Australian Bureau of Statistics, 2021 Census, as published for each suburb. Ransome is one of the smallest suburbs in Brisbane by population, and most of its land is reserve. That's the character of the place.</cite>
      </blockquote>

      <h2 class="h2" id="tingalpa">Tingalpa: the post-war suburb closer to town</h2>
      <p>Tingalpa is the odd one out here: not acreage, and not really bayside. It's 13.2 kilometres by road east of the CBD &mdash; six kilometres closer than Wynnum &mdash; and it's a post-war suburb through and through. The name may come from an Aboriginal expression for a fat kangaroo, or from Tingalpa Creek; the creek was surveyed in 1841.</p>
      <p>The date that matters for the houses: Tingalpa's population nearly tripled between 1954 and 1980, from about 1,400 people. The streets went in across those decades, which means the housing is the 1950s cottage, the 1960s highset and the 1970s brick lowset, on blocks that are flat and regular. It's Wynnum's housing stock without the esplanade &mdash; and the same rebuild conversation, six kilometres closer to town.</p>

      <h2 class="h2" id="gumdale">Gumdale: the acreage</h2>
      <p>Gumdale is where the Bayside turns rural. Large lots, a state primary school, bushland and creeks. It's generally described as Brisbane's nearest acreage suburb to the city, with newer smaller subdivisions at the edges. <a href="../wakerley-and-gumdale-the-newer-bayside/">Gumdale and its estate neighbour Wakerley are compared here.</a></p>

      <h2 class="h2" id="why-here">Why Sabre is based here</h2>
      <p>Because it's the middle. From 40 Molle Road, Ransome, we're a few minutes from Wynnum, Manly and Lota to the north, the Redlands to the south, and Wakerley, Gumdale and Tingalpa to the west. Every block we build on is a short drive from the shed, which is what &ldquo;local builder&rdquo; is supposed to mean.</p>
      <p>Sabre has built on the Bayside since 1990. The move to Ransome is a move to the centre of where the work is.</p>

      <h2 class="h2" id="houses">What gets built on this edge?</h2>
      <p>Three different jobs, and it's worth knowing which yours is.</p>
      <p><strong>Tingalpa</strong> is the classic bayside rebuild without the bay: a post-war house on a good flat block, outgrown by the family, on land that carries the value. Fibro from before 1990, a highset with rooms built in underneath, the usual list. <a href="../what-are-bayside-houses-made-of/">The field guide to those houses is here</a>, and <a href="../why-are-so-many-bayside-houses-being-knocked-down/">why so many are coming down is here</a>.</p>
      <p><strong>Gumdale</strong> is design to the block. An acreage lot has room for a house drawn for the site &mdash; the fall, the trees, the aspect, the shed and the pool &mdash; rather than fitted to it. It's the part of the Bayside where a family can build without being shaped by what was there before.</p>
      <p><strong>Ransome</strong> is rare. There are very few residential blocks, they don't change hands often, and each one is its own case: bushland, creek and overlay questions that need a builder and a designer on the ground before anyone draws anything.</p>
      <p>The same rule runs through all three: the design starts with the block, and a plan picked from a range doesn't know which of these three places it's standing in.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Ransome is 429 people and mostly reserve,</b> on the Redland boundary. Sabre's home now.</li>
          <li><b>Tingalpa is a post-war suburb six kilometres closer to town than Wynnum,</b> with Wynnum's housing stock and the same rebuild story.</li>
          <li><b>Gumdale is the acreage:</b> design to the block, not a plan from a range.</li>
          <li><b>None of the three has the water at the end of the street.</b> What they have is room.</li>
          <li><b>All three are minutes from the shed.</b> That's what a local builder is.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Is Ransome in Brisbane or the Redlands?</p>
          <p>Brisbane. It's a City of Brisbane suburb on the boundary with the City of Redland. The rules on a Ransome block are Brisbane City Plan rules.</p>
        </div>
        <div>
          <p class="q">Can you get to the bay from Ransome?</p>
          <p>The suburb touches Moreton Bay, but the coast is Ransome Reserve and the walking tracks don't extend past the railway line to the water. For a swim, it's Lota or Manly.</p>
        </div>
        <div>
          <p class="q">Do you build in the Redlands too?</p>
          <p>Yes. Birkdale, Wellington Point, Cleveland and across the Redlands. They're a few minutes south of the shed.</p>
        </div>
        <div>
          <p class="q">Is Tingalpa flood-prone?</p>
          <p>Tingalpa Creek and the overland flow paths off the ridges are mapped by council lot by lot. Read the FloodWise report for the address. <a href="../does-wynnum-flood/">How to read it is here.</a></p>
        </div>
      </div>

      <p class="small sources">Sources: Australian Bureau of Statistics, 2021 Census populations for Ransome, Tingalpa and Gumdale as published by the ABS and recorded on Wikipedia; Ransome, Tingalpa and Gumdale histories (Charles Horace Ransome, gazettal 1975, Ransome Reserve, Tingalpa 1954&ndash;1980 growth, road distances) as recorded on Wikipedia from Queensland Government and Brisbane City Council sources; Sabre Constructions, <em>Meet the team</em> and client facts (40 Molle Rd, Ransome; founded 1990). Read 17 September 2026. Not planning or financial advice.</p>
''')
