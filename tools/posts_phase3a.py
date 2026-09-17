# Phase 3 of docs/reference/article-bank.md — the place cluster (Spiral 2), part A: S7, S8, S10, R23, R24, R25.
# Spiral 2 rule: EVERY post ends at the house. Sources read 2026-09-17:
#   ABS 2021 Census QuickStats — Wynnum SAL33188, Manly SAL31748, Lota SAL31686, Manly West SAL31749 (read on abs.gov.au)
#   qld.gov.au "School catchment areas" · Brisbane City Council FloodWise Property Reports / Flood Awareness Online
#   Translink Cleveland line timetable, one midday sample read via the Transit app, 17 Sep 2026
#   Wikipedia suburb articles (history, distances, schools) · SLQ "Housing a growing state" 2014 · asbestos.qld.gov.au
# Rule 1: no prices, no rents, no mortgage figures, no bands. Census tenure/price figures deliberately left out — they move.

POSTS = {}

# ---------------------------------------------------------------- S7 · is Wynnum a good place to live
POSTS["s7-wynnum"] = dict(
    slug="is-wynnum-a-good-place-to-live",
    section="suburbs",
    title="Is Wynnum a good place to live? An honest look at the good and the annoying",
    h1="Is Wynnum a good place to live?<br>An honest look at the good and the annoying.",
    description="The water, the train, the schools and the village, and the tide going out a kilometre, the salt, the storm season and the seventy-year-old houses. From a builder who has worked in these streets since 1990.",
    lede="Every guide to Wynnum is written by someone selling a house in it. This one is written by a family that builds them, and has since 1990. Here's what's good, what's annoying, and what the houses are actually like once you're inside one.",
    date="2026-09-17", category="Living on the Bayside", image="blog/is-wynnum-a-good-place-to-live.jpg",
    image_alt="The Wynnum foreshore: the jetty, the wading pool, the pines and the old highsets",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of the real street.",
    label=('The Bayside suburbs', 'Wynnum'),
    figure=dict(image="blog/is-wynnum-a-good-place-to-live.png", alt='Map of Wynnum with its three stations, the wading pool and jetty, the schools and the parks', caption='Boundaries &copy; OpenStreetMap contributors.', after='who-lives-here'),
    card_title="Is Wynnum a good place to live? An honest look at the good and the annoying",
    card_blurb="The water, the train, the village and the schools; the tide, the salt, the storms and the seventy-year-old houses. Written by a builder, not an agent.",
    about=["Wynnum", "Living on the Bayside", "Brisbane Bayside"],
    related=["wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family", "does-wynnum-flood", "what-are-bayside-houses-made-of"],
    cta="If you already live here and the house is the problem, not the street, that's exactly the conversation he has most.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Yes, for most families, and for reasons that don't change: the bay at the end of the street, a train to the city, a village centre you can walk to, and a stock of family-sized blocks that most of Brisbane ran out of decades ago.</p>
        <p>The annoying parts are real too. The tide goes out a long way, so the water isn't always where the postcard says. Salt air works on everything. Storm season is a season. And most of the houses were built between the 1940s and the 1970s, which means they're small, tired, or both.</p>
        <p>That last one is why we're allowed to write this. Wynnum's problem is rarely the suburb. It's the house, on a block that's worth staying on.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#who-lives-here">Who actually lives in Wynnum?</a></li>
          <li><a href="#the-good">What's good about it?</a></li>
          <li><a href="#the-annoying">What's annoying about it?</a></li>
          <li><a href="#the-houses">What are the houses like?</a></li>
          <li><a href="#stay-or-go">Stay or go: the question the suburb keeps asking</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="who-lives-here">Who actually lives in Wynnum?</h2>
      <p>Families, mostly, and people who grew up here and never saw a reason to leave.</p>

      <blockquote class="proof">
        <p><b>In the 2021 Census, Wynnum had 14,036 people with a median age of 43. Couple families with children were 43.0% of families, and 70.8% of dwellings were separate houses.</b></p>
        <cite>Australian Bureau of Statistics, 2021 Census QuickStats, Wynnum (Qld). Seven in ten homes are still stand-alone houses on their own block. That's the number that matters to a builder.</cite>
      </blockquote>

      <p>Wynnum was a town before it was a suburb. It had its own shire from 1902 and a town council with its own mayor a dozen years later, and you can still feel it: a main street, a jetty, a memorial park, a high school that's been there since the 1940s. It's a place with a centre, not a subdivision with a shopping centre.</p>

      <h2 class="h2" id="the-good">What's good about it?</h2>
      <ul class="pts">
        <li><strong>The water is the end of the street.</strong> The esplanade runs the length of the suburb. The wading pool, the jetty, Pandanus Beach and the parklands are where families end up on a Sunday whether they planned to or not.</li>
        <li><strong>The train.</strong> Three stations in the suburb on the Cleveland line, and a straight run to the city. <a href="../how-far-is-wynnum-from-brisbane-cbd/">How far it really is, with a real timetable, is here.</a></li>
        <li><strong>A village you can walk to.</strong> Bay Terrace and Edith Street still work as a main street. Coffee, a hardware shop, the doctor, the pub.</li>
        <li><strong>Schools inside the suburb.</strong> A state primary, a state high school and independent options within a few kilometres. <a href="../schools-on-the-bayside-catchments/">The catchments are here.</a></li>
        <li><strong>The blocks.</strong> Flat, regular, on old street grids. The kind of land that's almost gone from the inner suburbs.</li>
        <li><strong>Sixteen kilometres of shoreline.</strong> The Bayside Parklands run along mangroves, mudflats and wetlands that are part of a Ramsar-listed bay. Migratory shorebirds arrive every year. It's not a marina; it's a coast.</li>
      </ul>

      <h2 class="h2" id="the-annoying">What's annoying about it?</h2>
      <p>A fair page says this part out loud.</p>
      <ul class="pts">
        <li><strong>The tide goes out. A long way.</strong> At low tide the water off the esplanade is mudflats to the horizon. If you moved here for swimming off the beach, you'll be swimming at the wading pool. If you moved here for the light and the birds, it's the best part.</li>
        <li><strong>Salt.</strong> Screws rust, paint goes chalky, aluminium pits, the windward side of the house ages faster than the lee. Every house on the bay is in a slow argument with the air.</li>
        <li><strong>Storm season.</strong> October to March, most years. Trees down, gutters overflowing, the odd hailstorm. <a href="../bayside-storm-season-roof-trees-insurance/">What it means for a house is here.</a></li>
        <li><strong>The flats.</strong> Nearly three in ten dwellings are now units or townhouses, and the esplanade end of the suburb has changed. If you want the old Wynnum, it's a few streets back.</li>
        <li><strong>The houses.</strong> Which is the next section.</li>
      </ul>

      <h2 class="h2" id="the-houses">What are the houses like?</h2>
      <p>Old. That isn't a complaint; it's a date.</p>

      <blockquote class="proof">
        <p><b>Brisbane's suburbs &ldquo;became populated with low-set timber houses on quarter acre blocks&rdquo; in the years after 1946, when a Brisbane architect estimated a national shortfall of 300,000 houses.</b></p>
        <cite>State Library of Queensland, <em>Housing a growing state</em>, 2014. Wynnum got its share. The post-war cottage on a flat block near the water is the suburb's basic unit.</cite>
      </blockquote>

      <p>Walk a street two back from the esplanade and you'll see the whole set: a pre-war timber house on stumps, a post-war fibro cottage, a 1960s highset with the rooms built in underneath, a 1970s brick lowset. <a href="../what-are-bayside-houses-made-of/">What each one is made of, and what that means, is here.</a></p>
      <p>What they have in common is that they were built for a family of the 1950s, on a budget of the 1950s, with the materials of the 1950s. Two or three bedrooms, one bathroom, a kitchen at the back, and fibro somewhere. Sixty or seventy years on, they're at the point where the next round of work &mdash; restumping, rewiring, a roof, a second bathroom &mdash; costs real money and still leaves you with a small old house.</p>
      <p>Which is fine, if the house fits. It's the families it doesn't fit that end up ringing us.</p>

      <h2 class="h2" id="stay-or-go">Stay or go: the question the suburb keeps asking</h2>
      <p>Here's the pattern we see, over and over. A family buys a small house in Wynnum because the street is right. Ten years on, the street is still right &mdash; the school, the neighbours, the walk to the water &mdash; and the house has run out of room.</p>
      <p>The choice is a bigger house in a suburb they don't want, or a different house on the block they already love. On a good flat Wynnum block, the second option is often the honest one, and it's why there are so many demolition signs on so many fences. <a href="../why-are-so-many-bayside-houses-being-knocked-down/">The reasons are here.</a></p>
      <p>Not every house should come down. Some should be raised and opened up. Some just need a kitchen. The point is that in Wynnum, the suburb almost never turns out to be the problem.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Yes, it's a good place to live,</b> and the reasons are permanent: the bay, the train, the village, the blocks.</li>
          <li><b>The annoying parts are real:</b> the tide goes out, the salt eats things, storm season is a season, and the esplanade has gone to units.</li>
          <li><b>Seven in ten homes are still separate houses</b> &mdash; ABS 2021 &mdash; and most of them are post-war.</li>
          <li><b>The houses are the problem, not the suburb.</b> Small, old, fibro somewhere, on blocks worth keeping.</li>
          <li><b>Families who outgrow the house rarely outgrow the street.</b> That's the whole reason we're here.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Is Wynnum safe?</p>
          <p>We're builders, not the police, so we won't quote a number we didn't measure. The Queensland Police Service publishes crime statistics by suburb online; read them for Wynnum and the suburbs you're comparing it with, over a few years rather than one.</p>
        </div>
        <div>
          <p class="q">Can you swim at Wynnum?</p>
          <p>In the tidal wading pool on the esplanade, yes, and at Pandanus Beach when the tide is in. Off the foreshore at low tide, no &mdash; it's mud to the horizon. That's Moreton Bay, not a fault.</p>
        </div>
        <div>
          <p class="q">Is Wynnum expensive?</p>
          <p>Prices move, and anything we printed would be wrong by the time you read it. Ask an agent for last month's sales, not us. What we can say is that the value on the Bayside sits in the land, which is why so many families rebuild rather than move.</p>
        </div>
        <div>
          <p class="q">Does Wynnum flood?</p>
          <p>Parts of it are mapped for storm tide and overland flow, and council publishes a report for every lot. <a href="../does-wynnum-flood/">What the maps actually show is here.</a></p>
        </div>
      </div>

      <p class="small sources">Sources: Australian Bureau of Statistics, <a href="https://abs.gov.au/census/find-census-data/quickstats/2021/SAL33188" rel="noopener">2021 Census QuickStats, Wynnum</a>; State Library of Queensland, <em>Housing a growing state</em>, 2014; Wynnum history (shire 1902, Pandanus Beach 1987, Bayside Parklands) as recorded on Wikipedia from Brisbane City Council and Queensland Government sources. Read 17 September 2026. Sabre has built on the Bayside since 1990; the observations about houses are a builder's, not a survey. Not planning or financial advice.</p>
''')

# ---------------------------------------------------------------- S8 · Wynnum vs Manly vs Lota
POSTS["s8-compare"] = dict(
    slug="wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family",
    section="suburbs",
    title="Wynnum vs Manly vs Lota: which Bayside suburb suits which family?",
    h1="Wynnum vs Manly vs Lota:<br>which Bayside suburb suits which family?",
    description="Three suburbs on one stretch of bay, three different feels. The census numbers side by side, the train, the harbour, the schools, and what the houses are like in each.",
    lede="They share a coastline, a train line and a postcode boundary, and they're not the same place. Wynnum is the town. Manly is the harbour. Lota is the quiet one at the end. Here's how they differ, with the numbers, and what the houses are like in each.",
    date="2026-09-17", category="Living on the Bayside", image="blog/wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family.jpg",
    image_alt="Three panels: Wynnum's jetty, Manly's boat harbour, Lota's mangrove foreshore",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of the real street.",
    label=('Which suits which family', 'Wynnum &middot; Manly &middot; Lota'),
    figure=dict(image="blog/wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family.png", alt='Map of Wynnum, Manly and Lota with their stations', caption='Boundaries &copy; OpenStreetMap contributors.', after='numbers'),
    card_title="Wynnum vs Manly vs Lota: which Bayside suburb suits which family?",
    card_blurb="Three suburbs, one bay, three different feels. The census numbers side by side, the train, the harbour, the schools, and what the houses are like in each.",
    about=["Wynnum", "Manly", "Lota", "Living on the Bayside"],
    related=["is-wynnum-a-good-place-to-live", "lota-the-quiet-one-between-wynnum-and-manly", "schools-on-the-bayside-catchments"],
    cta="Whichever of the three you're in, if the block is right and the house isn't, that's the walk-through.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p><strong>Wynnum</strong> is the biggest and the most complete: a town centre, three stations, the wading pool, the high school, and the widest mix of houses and flats. <strong>Manly</strong> is smaller and older in median age, built around the boat harbour and the esplanade, with a village of its own. <strong>Lota</strong> is the smallest and the most purely residential &mdash; almost every dwelling is a separate house, and more of its families have children at home than either neighbour.</p>
        <p>If you want to walk to everything, Wynnum. If you want the harbour and the cafes, Manly. If you want a quiet street of houses where the kids ride bikes, Lota. All three have the same underlying housing stock &mdash; post-war timber and fibro, 1960s highsets, 1970s brick &mdash; and the same reason families rebuild: the street is right and the house isn't.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#numbers">What do the numbers say?</a></li>
          <li><a href="#wynnum">Wynnum: the town</a></li>
          <li><a href="#manly">Manly: the harbour</a></li>
          <li><a href="#lota">Lota: the quiet one</a></li>
          <li><a href="#which">Which family suits which?</a></li>
          <li><a href="#houses">What are the houses like in each?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="numbers">What do the numbers say?</h2>
      <p>Same census, same year, side by side. Prices and rents are left out on purpose: they move, and a number printed here would be wrong by the time you read it.</p>
      <div class="tablewrap">
        <table>
          <thead><tr><th>2021 Census</th><th>Wynnum</th><th>Manly</th><th>Lota</th></tr></thead>
          <tbody>
            <tr><td>People</td><td>14,036</td><td>4,273</td><td>3,518</td></tr>
            <tr><td>Median age</td><td>43</td><td>46</td><td>42</td></tr>
            <tr><td>Couple families with children</td><td>43.0%</td><td>41.9%</td><td>48.8%</td></tr>
            <tr><td>Separate houses</td><td>70.8%</td><td>70.6%</td><td>95.3%</td></tr>
            <tr><td>Flats or apartments</td><td>16.2%</td><td>16.1%</td><td>0.7%</td></tr>
            <tr><td>By road from the CBD</td><td>19.6 km</td><td>19.9 km</td><td>19.7 km</td></tr>
          </tbody>
        </table>
      </div>

      <blockquote class="proof">
        <p><b>Lota: 95.3% separate houses, 0.7% flats or apartments, 48.8% couple families with children. Wynnum and Manly: about seven in ten separate houses and one in six flats.</b></p>
        <cite>Australian Bureau of Statistics, 2021 Census QuickStats &mdash; Wynnum, Manly (Qld) and Lota. One table explains most of the difference in how the three feel.</cite>
      </blockquote>

      <h2 class="h2" id="wynnum">Wynnum: the town</h2>
      <p>Wynnum was a shire from 1902 and a town with its own mayor after that, and it still behaves like one. A main street, the jetty, the wading pool, Pandanus Beach, a state high school, three stations on the Cleveland line, the biggest population of the three by a distance.</p>
      <p>It's also where the change is. A sixth of its dwellings are flats, mostly toward the esplanade. If you want the old grid of houses, it's still there, a few streets back. <a href="../is-wynnum-a-good-place-to-live/">The honest guide to Wynnum is here.</a></p>

      <h2 class="h2" id="manly">Manly: the harbour</h2>
      <p>Manly was sold off as the Manly Beach Estate in 1882, named after the Sydney beach, and the harbour has defined it ever since: a 41.8-hectare boat harbour south of Norfolk Point, a village on Cambridge Parade, the esplanade running north to Wynnum.</p>
      <p>It has the oldest median age of the three and the same share of flats as Wynnum, concentrated near the water. There's no state high school in Manly; the nearest is Wynnum State High, on the boundary. It's the suburb people picture when they say &ldquo;the Bayside&rdquo;: boats, cafes, the breeze off the water in the afternoon.</p>

      <h2 class="h2" id="lota">Lota: the quiet one</h2>
      <p>Lota is named after Lota House, built in 1863 by the pastoralist William Duckett White, whose estate grew sugar cane and fodder on the creek flats. The railway came through in 1889; the line beyond it closed in 1960 and reopened in stages through the 1980s, so for a couple of decades Lota was the end of the line.</p>
      <p>It still feels that way, in a good sense. Almost every dwelling is a stand-alone house. Nearly half its families have children at home, the highest of the three. One primary school, no high school, a station, a seawall built as Depression relief work in 1931, and streets where not much happens. <a href="../lota-the-quiet-one-between-wynnum-and-manly/">The Lota portrait is here.</a></p>

      <h2 class="h2" id="which">Which family suits which?</h2>
      <ul class="pts">
        <li><strong>You want to walk to everything and take the train:</strong> Wynnum.</li>
        <li><strong>You have a boat, or want the cafe-and-esplanade life:</strong> Manly.</li>
        <li><strong>You want a quiet street of houses, kids on bikes, and don't mind driving to the shops:</strong> Lota.</li>
        <li><strong>You want a high school in the suburb:</strong> Wynnum. Manly and Lota feed into it.</li>
        <li><strong>You're downsizing to a unit near the water:</strong> Wynnum or Manly. Lota barely has any.</li>
        <li><strong>You want to rebuild on a flat regular block:</strong> any of the three. That's the next section.</li>
      </ul>

      <h2 class="h2" id="houses">What are the houses like in each?</h2>
      <p>The same, underneath. The three suburbs were built up in the same decades from the same materials, and the difference is mostly proportion.</p>
      <p>All three have the pre-war timber house on stumps, the post-war cottage, the 1960s highset with the built-in-under, and the 1970s brick lowset. Wynnum and Manly have added flats on top. Lota has barely added anything, which is why it looks like the Bayside did in 1985. <a href="../what-are-bayside-houses-made-of/">What each type is made of is here.</a></p>
      <p>For a builder, the useful difference is the blocks. Lota's and the back streets of Wynnum's are flat and regular, on an old grid. Manly's climb the hill behind the harbour, and slope changes what a rebuild costs. The esplanade end of all three carries council's flood and storm tide levels, which set the floor height of anything new. <a href="../does-wynnum-flood/">What the flood maps actually show is here.</a></p>
      <p>Whichever you pick, you'll likely be buying a seventy-year-old house on a block that's worth more than it is. Knowing that going in is the whole trick.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Wynnum is the town, Manly is the harbour, Lota is the quiet one.</b> Same coast, different feel.</li>
          <li><b>Lota is 95% separate houses and has the most families with kids;</b> Wynnum and Manly are about 70% houses with a sixth in flats. ABS 2021.</li>
          <li><b>Only Wynnum has a state high school.</b> Manly and Lota feed into it.</li>
          <li><b>All three are about 20 km by road from the CBD</b> and on the same train line.</li>
          <li><b>The houses are the same underneath:</b> post-war timber and fibro, highsets, 1970s brick. The block decides the rebuild.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Which is the most expensive?</p>
          <p>We don't publish prices; they move. Ask an agent for recent sales in each and compare like with like &mdash; a waterfront in one against a waterfront in the other.</p>
        </div>
        <div>
          <p class="q">Which has the best schools?</p>
          <p>Each has a state primary, and all three share Wynnum State High as the nearest state secondary. Which catchment you're in depends on your address, not your suburb name &mdash; <a href="../schools-on-the-bayside-catchments/">check it on EdMap</a>.</p>
        </div>
        <div>
          <p class="q">Is Manly West the same as Manly?</p>
          <p>No. It was part of Manly until 1975, when it became its own suburb, and it's inland, larger and younger. <a href="../whats-the-difference-between-manly-and-manly-west/">The difference is here.</a></p>
        </div>
        <div>
          <p class="q">Which is best for a knockdown rebuild?</p>
          <p>The block decides, not the suburb. A flat regular block in any of the three is a good rebuild block; a steep one in Manly or a storm-tide lot on the esplanade in any of them needs more design. Nathan will tell you which yours is.</p>
        </div>
      </div>

      <p class="small sources">Sources: Australian Bureau of Statistics, 2021 Census QuickStats &mdash; <a href="https://abs.gov.au/census/find-census-data/quickstats/2021/SAL33188" rel="noopener">Wynnum</a>, <a href="https://abs.gov.au/census/find-census-data/quickstats/2021/SAL31748" rel="noopener">Manly (Qld)</a>, <a href="https://abs.gov.au/census/find-census-data/quickstats/2021/SAL31686" rel="noopener">Lota</a>; suburb histories and road distances as recorded on Wikipedia from Queensland Government and Brisbane City Council sources. Read 17 September 2026. Not planning or financial advice.</p>
''')

# ---------------------------------------------------------------- S10 · schools and catchments
POSTS["s10-schools"] = dict(
    slug="schools-on-the-bayside-catchments",
    section="living",
    title="Schools on the Bayside: the catchments, and what &ldquo;in catchment&rdquo; is worth",
    h1="Schools on the Bayside: the catchments,<br>and what &ldquo;in catchment&rdquo; is worth.",
    description="What a state school catchment is in Queensland, how to check yours on EdMap, the state and independent schools across Wynnum, Manly, Lota and Manly West, and why catchment is the reason so many families rebuild instead of moving.",
    lede="Catchment is the quiet reason behind half the rebuilds on the Bayside. The kids are in the school, the school is tied to the address, and the address is tied to a house that's run out of room. Here's how catchments actually work, where the schools are, and what that does to the decision.",
    date="2026-09-17", category="Living on the Bayside", image="blog/schools-on-the-bayside-catchments.jpg",
    image_alt="Three children in school hats walking a Bayside footpath toward the school gate",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of the real street.",
    label=('Catchments, in plain words', 'Bayside schools'),
    figure=dict(image="blog/schools-on-the-bayside-catchments.png", alt='Map of the Bayside state and independent schools; locations only, catchments are on EdMap', caption="School locations only. Catchment boundaries are on the Department of Education's EdMap. Boundaries &copy; OpenStreetMap contributors.", after='the-schools'),
    card_title="Schools on the Bayside: the catchments, and what &ldquo;in catchment&rdquo; is worth",
    card_blurb="How Queensland state school catchments work, how to check yours on EdMap, where the Bayside schools are, and why catchment is the reason so many families rebuild instead of moving.",
    about=["School catchments", "Wynnum", "Manly", "Living on the Bayside"],
    related=["wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family", "why-are-so-many-bayside-houses-being-knocked-down", "is-wynnum-a-good-place-to-live"],
    cta="If the school is the reason you can't move, the house is the thing to change. He'll tell you whether yours can.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>In Queensland, every state school has a catchment: the area where its core intake of students must live. If your home is inside it, your child is entitled to a place. Outside it, you're applying, and a school with an enrolment management plan can say no.</p>
        <p>You check yours on the Department of Education's EdMap by typing in your address. It's the address that counts, not the suburb name &mdash; a street can sit in one catchment and the next street in another.</p>
        <p>On the Bayside the state schools are Wynnum State School, Manly State School, Lota State School, Manly West, Wondall Heights and Wynnum West for primary, and Wynnum State High and Brisbane Bayside State College for secondary, with Iona College and the Moreton Bay colleges as the independent options.</p>
        <p>The catchment is why families stay in a house they've outgrown. It ties the school to the block. That's the decision this page is really about.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-is-a-catchment">What is a school catchment in Queensland?</a></li>
          <li><a href="#how-to-check">How do you check which catchment you're in?</a></li>
          <li><a href="#the-schools">Which schools are on the Bayside?</a></li>
          <li><a href="#worth">What is &ldquo;in catchment&rdquo; actually worth?</a></li>
          <li><a href="#the-house">Why catchment is a house question, not a school question</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-is-a-catchment">What is a school catchment in Queensland?</h2>

      <blockquote class="proof">
        <p><b>&ldquo;A school catchment area is the geographical location where a state school's core intake of students must live.&rdquo; &ldquo;Catchment areas ensure every Queensland student from Prep to Year 12 is able to enrol at their local state school.&rdquo;</b></p>
        <cite>Queensland Government, <em>School catchment areas</em>, qld.gov.au. The entitlement is to your local school. Anywhere else is an application.</cite>
      </blockquote>

      <p>Some schools also have an enrolment management plan. In the government's words, a plan ensures &ldquo;enough places are kept for local students (i.e. those living in the school's catchment area)&rdquo; and that &ldquo;a fair process is in place for assessing enrolments for students living outside a school's catchment area.&rdquo;</p>
      <p>In plain words: a popular school fills up with local kids first, and out-of-catchment families join a queue that may never move.</p>

      <h2 class="h2" id="how-to-check">How do you check which catchment you're in?</h2>
      <ol>
        <li>Go to the Department of Education's <strong>EdMap</strong> site.</li>
        <li>Type your home address, or a school's name.</li>
        <li>The map shows the catchment boundaries and whether your address is inside.</li>
      </ol>
      <p>Two things people get wrong:</p>
      <ul class="pts">
        <li><strong>The suburb name means nothing.</strong> Catchments follow streets and creeks, not suburb boundaries. Two houses in Manly West can be in different primary catchments.</li>
        <li><strong>Catchments change.</strong> Schools open, close and amalgamate. Wynnum State School itself is the 2010 amalgamation of three older primaries. Check the current map before you buy or plan around a school.</li>
      </ul>

      <h2 class="h2" id="the-schools">Which schools are on the Bayside?</h2>
      <p>A guide, not a catchment map. Check EdMap for your address.</p>
      <div class="tablewrap">
        <table>
          <thead><tr><th>School</th><th>Type</th><th>Where</th><th>Note</th></tr></thead>
          <tbody>
            <tr><td>Wynnum State School</td><td>State primary</td><td>Wynnum</td><td>Formed in 2010 from Wynnum Central, Wynnum North and Lindum State Schools</td></tr>
            <tr><td>Manly State School</td><td>State primary</td><td>Manly</td><td>Opened 1910</td></tr>
            <tr><td>Lota State School</td><td>State primary</td><td>Lota</td><td>Opened 1952</td></tr>
            <tr><td>Manly West State School</td><td>State primary</td><td>Manly West</td><td>Opened 1958</td></tr>
            <tr><td>Wondall Heights State School</td><td>State primary</td><td>Manly West</td><td>Opened 1966</td></tr>
            <tr><td>Wynnum West State School</td><td>State primary</td><td>Wynnum West</td><td>Opened 1922</td></tr>
            <tr><td>Gumdale State School</td><td>State primary</td><td>Gumdale</td><td>Nearest state primary for much of Wakerley</td></tr>
            <tr><td>Wynnum State High School</td><td>State secondary</td><td>Wynnum</td><td>Foundation stone 1941. Nearest state high for Manly and Lota</td></tr>
            <tr><td>Brisbane Bayside State College</td><td>State secondary</td><td>Wynnum West</td><td>Opened 2010; the relocated and renamed Wynnum North State High School (1964)</td></tr>
            <tr><td>Iona College</td><td>Catholic secondary (boys)</td><td>North Road, Wynnum West</td><td>Established 1958</td></tr>
            <tr><td>Moreton Bay College and Moreton Bay Boys' College</td><td>Independent</td><td>Manly West</td><td>Girls' school dates from 1901; boys' college opened 2003</td></tr>
          </tbody>
        </table>
      </div>
      <p>Neither Manly nor Lota has a state secondary school of its own; both look to Wynnum State High. Wakerley has no state school inside the suburb at all, and looks to Gumdale and Manly West for primary and Brisbane Bayside State College for secondary.</p>

      <h2 class="h2" id="worth">What is &ldquo;in catchment&rdquo; actually worth?</h2>
      <p>To a family, it's worth whatever not moving the kids is worth, and that's usually a lot. To the market, it shows up in what buyers will pay for a street, and we'll leave the number to the agents.</p>
      <p>But here's the part the school guides don't say. A catchment is worth nothing if the house inside it doesn't fit your family. And it's worth exactly as much if you replace the house and keep the address.</p>

      <h2 class="h2" id="the-house">Why catchment is a house question, not a school question</h2>
      <p>This is the conversation we have more than any other.</p>
      <p>A family bought a post-war cottage in the right catchment when the kids were small. The kids are now at the school, settled, with friends. The house has two bedrooms and one bathroom. Moving means leaving the catchment, or paying for a bigger house in it, if one comes up.</p>
      <p>The third option is the one the suburb keeps choosing: keep the address, change the house. On a flat Bayside block, a new home designed for the family &mdash; and for the flood level, and the aspect &mdash; keeps the catchment, the neighbours and the walk to school, and replaces the only thing that was wrong. <a href="../why-are-so-many-bayside-houses-being-knocked-down/">It's one of the four reasons the Bayside is rebuilding.</a></p>
      <p>Sometimes the honest answer is a raise or an extension instead. Sometimes it's a renovation. What it almost never is, once the kids are in the school, is a move.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>A catchment is where a state school's core intake must live.</b> Inside it, your child is entitled to a place. Outside, you're applying.</li>
          <li><b>Check your address on EdMap, not your suburb name.</b> Boundaries follow streets, and they change.</li>
          <li><b>Only Wynnum has a state high school;</b> Manly and Lota feed into it. Wakerley has no state school inside the suburb.</li>
          <li><b>Catchment ties the school to the block.</b> That's why families stay in houses they've outgrown.</li>
          <li><b>Keep the address, change the house</b> is the option most families haven't priced.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">If we rebuild, do we lose our place at the school?</p>
          <p>Your entitlement is tied to where you live. If you rent nearby during the build, ask the school how they treat a temporary address before you sign a lease &mdash; and rent inside the catchment if you can. We're builders, not the Department; check with the school.</p>
        </div>
        <div>
          <p class="q">Can we enrol out of catchment?</p>
          <p>You can apply. A school with an enrolment management plan keeps places for in-catchment students first and assesses out-of-catchment applications by its own process. Ask the school directly.</p>
        </div>
        <div>
          <p class="q">Does a suburb's name tell me its schools?</p>
          <p>No. Manly has a primary but no high school; Wakerley has no state school at all; Wynnum State School serves streets well beyond Wynnum. Use the map.</p>
        </div>
        <div>
          <p class="q">Are the independent schools in catchments?</p>
          <p>No. Catchments are a state-school rule. Iona and the Moreton Bay colleges enrol on their own criteria.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Government, <a href="https://www.qld.gov.au/education/schools/find/enrolment/catchment" rel="noopener">School catchment areas</a> and the Department of Education's EdMap; school opening dates and locations as recorded on Wikipedia from Queensland State Archives and school sources. Read 17 September 2026. School lists change; confirm the current catchment for any address on EdMap. Not education or financial advice.</p>
''')

# ---------------------------------------------------------------- R23 · how far from the CBD
POSTS["r23-distance"] = dict(
    slug="how-far-is-wynnum-from-brisbane-cbd",
    section="living",
    title="How far is Wynnum from Brisbane CBD, really? Train, car, peak hour",
    h1="How far is Wynnum from Brisbane CBD,<br>really? Train, car, peak hour.",
    description="About 20 km by road and 22 km by rail. A real timetable sample puts Central to Wynnum Central at 40 minutes. What decides the car time, and why it matters for where you build.",
    lede="Ask three Wynnum people how far it is to the city and you'll get three answers, because there are three: the road, the rail line, and the peak hour. Here are the measured ones, and the honest one.",
    date="2026-09-17", category="Living on the Bayside", image="blog/how-far-is-wynnum-from-brisbane-cbd.jpg",
    image_alt="A train pulling into a small Bayside station, commuters on the platform, the bay between the houses",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of the real street.",
    label=('By train and by road', 'Wynnum to the city'),
    figure=dict(image="blog/how-far-is-wynnum-from-brisbane-cbd.png", alt='Schematic of the Cleveland line from Central to Lota with the times from one midday service', caption='Schematic, one midday service read 17 September 2026. Check Translink for yours.', after='by-train'),
    card_title="How far is Wynnum from Brisbane CBD, really? Train, car, peak hour",
    card_blurb="About 20 km by road, 22 km by rail, 40 minutes on a real midday train. What decides the car time, and why it's a question about where you live, not where you work.",
    about=["Wynnum", "Commute", "Living on the Bayside"],
    related=["is-wynnum-a-good-place-to-live", "wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family", "lota-the-quiet-one-between-wynnum-and-manly"],
    cta="Most families we build for already made the commute decision years ago. The house is what changed.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Wynnum is 19.6 kilometres by road east of the Brisbane GPO, and Wynnum Central station is 22.44 kilometres from Central by rail on the Cleveland line, in Translink Zone 2.</p>
        <p>On a real midday timetable we read on 17 September 2026, a train leaving Central at 12:17 reached Wynnum Central at 12:57, Manly at 1:00 and Lota at 1:03: forty minutes, give or take, station to station. Peak services stop at fewer stations and can be quicker; check Translink for the one you'd catch.</p>
        <p>By car there is no fixed number, because the difference is entirely the time of day. Nobody can give you one except your own trial run at the hour you'd actually leave.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#by-road">How far is it by road?</a></li>
          <li><a href="#by-train">How long is the train, really?</a></li>
          <li><a href="#by-car">What decides the car time?</a></li>
          <li><a href="#manly-lota">What about Manly and Lota?</a></li>
          <li><a href="#the-house">Why it's a question about the house</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="by-road">How far is it by road?</h2>
      <p>19.6 kilometres by road from the Brisbane GPO to the centre of Wynnum, going east along Wynnum Road or the Port of Brisbane Motorway and Lytton Road. Manly is 19.9 and Lota 19.7 &mdash; the three are effectively the same distance out, on the same stretch of coast.</p>
      <p>Twenty kilometres is not far. Plenty of Brisbane suburbs that think of themselves as inner are ten. The distance was never the issue; the road is.</p>

      <h2 class="h2" id="by-train">How long is the train, really?</h2>

      <blockquote class="proof">
        <p><b>Central 12:17 &rarr; Wynnum Central 12:57 &rarr; Manly 1:00 &rarr; Lota 1:03.</b> Forty minutes to Wynnum Central, forty-six to Lota, on an all-stops midday service.</p>
        <cite>Translink Cleveland line timetable, one weekday service, read via the Transit app on 17 September 2026. One sample, off-peak, all stations. Your train will differ; the shape won't.</cite>
      </blockquote>

      <p>The Cleveland line runs from Cleveland through Lota, Manly, Wynnum Central, Wynnum and Wynnum North, then Lindum and Hemmant, and on through Cannon Hill and Coorparoo into the city. Three of the line's stations are inside Wynnum. Wynnum Central is 22.44 kilometres from Central by rail.</p>
      <p>It's a straight run, no change of train, and the line has been there since 1889. That's the thing Wynnum has that most suburbs twenty kilometres out don't: a fixed number. Whatever the road is doing, the train is forty minutes.</p>

      <h2 class="h2" id="by-car">What decides the car time?</h2>
      <p>Four things, and none of them is the distance.</p>
      <ul class="pts">
        <li><strong>The time you leave.</strong> The same twenty kilometres is a different road at 6:30, 7:45 and 9:15.</li>
        <li><strong>Which road.</strong> Wynnum Road through the suburbs, or the Port of Brisbane Motorway to the Gateway and in. Both have their bad days.</li>
        <li><strong>Where in the city.</strong> The CBD, the hospital precinct, South Bank and the airport are four different trips.</li>
        <li><strong>The rain.</strong> Brisbane traffic in a downpour is a different city.</li>
      </ul>
      <p>The only honest number is your own: drive it, on the day and at the hour you'd actually do it, before you decide anything. Anyone who gives you one number is telling you about one hour of one day.</p>

      <h2 class="h2" id="manly-lota">What about Manly and Lota?</h2>
      <p>Three and six minutes further down the line, respectively, on the service above, and a few hundred metres further by road. For practical purposes the three suburbs share a commute. The difference is whether you can walk to the station, and which one.</p>

      <h2 class="h2" id="the-house">Why it's a question about the house</h2>
      <p>People ask this question when they're deciding whether to move to the Bayside. The families we build for asked it ten years ago, answered it, and stayed.</p>
      <p>What changed for them isn't the commute. It's that the post-war cottage they bought because it was near the station has run out of room, and the choice is a bigger house somewhere with a worse commute, or a different house on the block they already have &mdash; the one that's a walk from the train. <a href="../why-are-so-many-bayside-houses-being-knocked-down/">That's most of the demolition signs on the Bayside.</a></p>
      <p>Which is to say: the forty minutes is part of what the block is worth. It's one of the reasons the land carries the value and the house doesn't.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>19.6 km by road, 22.44 km by rail.</b> Manly and Lota are the same distance for practical purposes.</li>
          <li><b>The train is the fixed number:</b> about forty minutes on an all-stops service, no change.</li>
          <li><b>The car is not a number.</b> Time of day, road, destination and rain decide it. Drive it yourself at the real hour.</li>
          <li><b>Three stations inside Wynnum,</b> one each in Manly and Lota. Walking distance to one is worth more than the suburb name.</li>
          <li><b>The commute is part of what the block is worth</b> &mdash; and why families rebuild rather than leave.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
          <div>
          <p class="q">Is there an express train from Wynnum?</p>
          <p>Some peak services skip stations; the timetable changes. Check Translink's journey planner for the specific service, not a blog &mdash; including this one.</p>
        </div>
        <div>
          <p class="q">What zone is Wynnum?</p>
          <p>Wynnum Central is in Translink Zone 2. Fares are Translink's to publish, not ours.</p>
        </div>
        <div>
          <p class="q">Is it quicker to drive to the airport than the city?</p>
          <p>Usually, via the Gateway, but it depends on the hour like everything else. Try it.</p>
        </div>
        <div>
          <p class="q">Does living near the station change what we can build?</p>
          <p>Not directly. What changes the build is the block: its overlays, its slope, its flood level. But a block that's a walk from the train is worth designing for properly, because you won't want to leave it.</p>
        </div>
      </div>

      <p class="small sources">Sources: Translink Cleveland line timetable, one weekday midday service read via the Transit app on 17 September 2026 (a single sample, not a guarantee); rail distance and station facts as recorded on Wikipedia from Queensland Rail; road distances from the Brisbane GPO as recorded on Wikipedia. Timetables change; check Translink before you rely on any time here. Not transport advice.</p>
''')

# ---------------------------------------------------------------- R24 · does Wynnum flood
POSTS["r24-flood"] = dict(
    slug="does-wynnum-flood",
    section="living",
    title="Does Wynnum flood? What the council maps actually show",
    h1="Does Wynnum flood?<br>What the council maps actually show.",
    description="Wynnum isn't on the river. Its flood risk is storm tide, creeks and overland flow, mapped lot by lot by Brisbane City Council. How to read the Flood Awareness Map and the FloodWise report for your address, without the panic.",
    lede="The honest answer is: some of it, from some kinds of water, and council has mapped exactly which lots. This is how to read the maps for your own address, what the four kinds of flooding mean on the bay, and what it changes if you build.",
    date="2026-09-17", category="Living on the Bayside", image="blog/does-wynnum-flood.jpg",
    image_alt="A king tide up to the top of the esplanade seawall, the road and the houses dry above it",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of the real street.",
    label=("Reading council's map", 'Does Wynnum flood?'),
    figure=dict(image="blog/does-wynnum-flood.png", alt="Section diagram of the four sources of flooding council maps: storm tide, creek, overland flow, and the river that isn't Wynnum's", caption='Schematic section, not a flood map.', after='which-water'),
    card_title="Does Wynnum flood? What the council maps actually show",
    card_blurb="Not from the river. Storm tide, creeks and overland flow, mapped lot by lot. How to read council's Flood Awareness Map and FloodWise report for your address, without the panic.",
    about=["Wynnum", "Flooding", "FloodWise Property Report", "Living on the Bayside"],
    related=["rebuilding-on-a-flood-overlay-block-on-the-bayside", "is-wynnum-a-good-place-to-live", "bayside-storm-season-roof-trees-insurance"],
    cta="Bring the FloodWise report for your lot and he'll tell you what the levels do to a design. Or he'll pull it with you.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Parts of Wynnum are mapped for flooding, and the source is not the Brisbane River. Wynnum sits on Moreton Bay, so the water council models comes from storm tide off the bay, from the creeks that drain to it, and from overland flow &mdash; rain running across land before it reaches a drain.</p>
        <p>Brisbane City Council publishes the answer for every lot. The Flood Awareness Map shows the likelihood of each type of flooding for an address, and the FloodWise Property Report gives the levels: flood heights at different likelihoods, and the minimum habitable floor level a new house must meet.</p>
        <p>Most Wynnum lots aren't affected by all four types, and many aren't affected by any. The ones that are usually still get built on &mdash; higher. Read the map for your address before you believe anyone, including us.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#which-water">Which kinds of flooding does Wynnum actually get?</a></li>
          <li><a href="#read-the-map">How do you read council's map for your address?</a></li>
          <li><a href="#what-the-report-says">What does the FloodWise report tell you?</a></li>
          <li><a href="#what-it-doesnt">What don't the maps tell you?</a></li>
          <li><a href="#the-house">What does it change for a house?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="which-water">Which kinds of flooding does Wynnum actually get?</h2>
      <p>Council models four sources, and Wynnum's geography sorts them quickly.</p>
      <ul class="pts">
        <li><strong>River flooding.</strong> Wynnum isn't on the Brisbane River. This is the one people picture from 2011 and 2022, and it's mostly somebody else's problem here.</li>
        <li><strong>Storm tide.</strong> The bay, pushed up by a storm on a high tide. Mapped under council's coastal hazard overlay. This is the one that matters closest to the esplanade.</li>
        <li><strong>Creek and waterway flooding.</strong> Wynnum Creek and the drains to the bay back up when the tide is high and the rain is heavy at the same time.</li>
        <li><strong>Overland flow.</strong> Rain moving across land in a downpour. It follows old gullies and low points that the street grid was laid over, and it turns up on blocks nowhere near a creek.</li>
      </ul>

      <h2 class="h2" id="read-the-map">How do you read council's map for your address?</h2>
      <ol>
        <li>Open council's <a href="https://fam.brisbane.qld.gov.au/" rel="noopener">Flood Awareness Map</a> and choose <strong>I am a resident, business or visitor</strong>.</li>
        <li>Search your address. The <strong>Flooding Overview</strong> panel lists the flood types and their likelihood for your property.</li>
        <li>Click <strong>Technical FloodWise Property Report</strong> for the levels.</li>
      </ol>

      <blockquote class="proof">
        <p><b>&ldquo;The Flood Awareness Map is an easy-to-use online tool that offers general flood awareness information. You can search for a property to see the likelihood of it being affected by different types of flooding.&rdquo;</b></p>
        <cite>Brisbane City Council, <em>FloodWise Property Reports</em>. Council's answer for your lot beats anyone's opinion about your suburb, including a neighbour who's &ldquo;never seen it flood.&rdquo;</cite>
      </blockquote>

      <h2 class="h2" id="what-the-report-says">What does the FloodWise report tell you?</h2>
      <p>Three things you can act on.</p>
      <ul class="pts">
        <li><strong>Flood levels at different likelihoods</strong> &mdash; the 0.2%, 1%, 2%, 5% and 20% AEP events for river, creek and storm tide. A 1% AEP flood has a one-in-a-hundred chance in any given year. It isn't &ldquo;once a century.&rdquo;</li>
        <li><strong>The minimum habitable floor level</strong> for a new house on the lot.</li>
        <li><strong>Which City Plan overlays apply</strong> &mdash; river, creek, overland flow, coastal hazard &mdash; which decides whether there are flood planning requirements for a build.</li>
      </ul>

      <blockquote class="proof">
        <p><b>&ldquo;It is important to note that flooding may still present a risk and could include overland flow, which is shown as a property development flag further down the report.&rdquo;</b></p>
        <cite>Brisbane City Council, <em>FloodWise Property Reports</em>, on lots with no river, creek or storm tide level assigned. Council also notes the report's aerial map does not show overland flow. Read the whole report, not the picture.</cite>
      </blockquote>

      <h2 class="h2" id="what-it-doesnt">What don't the maps tell you?</h2>
      <ul class="pts">
        <li><strong>Whether your house has ever been wet.</strong> The maps are models of likelihood, not a record. A dry history is good news; it isn't the same as no rules.</li>
        <li><strong>What a king tide does to the street.</strong> Nuisance tidal water on low esplanade streets is a different thing from a modelled storm tide, and the map isn't a tide chart.</li>
        <li><strong>What your insurer thinks.</strong> Insurers use their own flood data. Ask them, and tell them if a new house is designed to the current levels.</li>
      </ul>

      <h2 class="h2" id="the-house">What does it change for a house?</h2>
      <p>If your lot carries a flood overlay, a new house has to meet the minimum habitable floor level in the report. Near the bay that often means the living areas go up: a highset house, or a ground floor of garage, laundry and storage with the family upstairs.</p>
      <p>Done from the start, that's a better house, not just a compliant one. The rooms that matter sit where the water can't reach; the ground floor is built to be hosed out. Done as an afterthought &mdash; a plan drawn for a flat estate lot, then lifted &mdash; it's expensive and awkward. <a href="../rebuilding-on-a-flood-overlay-block-on-the-bayside/">What an overlay does to a design is here.</a></p>
      <p>It's also why the old houses matter. A 1960s lowset on a ground-level slab near the esplanade sits below levels that a new house wouldn't be allowed to. Sometimes the flood map is the strongest argument for starting again.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Wynnum's flood risk is storm tide, creeks and overland flow</b> &mdash; not the river.</li>
          <li><b>Council has mapped every lot.</b> Flood Awareness Map for the likelihood, FloodWise report for the levels.</li>
          <li><b>1% AEP is one in a hundred each year,</b> not once a century.</li>
          <li><b>The aerial map doesn't show overland flow.</b> Read the whole report.</li>
          <li><b>An overlay sets the floor level of a new house.</b> Designed to it, that's a better house.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Did Wynnum flood in 2011 and 2022?</p>
          <p>We're not going to characterise past events street by street from memory. Council's flood information site includes historic flood mapping; read it for your address rather than taking anyone's recollection.</p>
        </div>
        <div>
          <p class="q">Is the esplanade the only part affected?</p>
          <p>No. Storm tide is concentrated near the bay, but creek and overland flow mapping follows the low ground wherever it runs. That's why the check is by address, not by distance from the water.</p>
        </div>
        <div>
          <p class="q">Can we still build if we're in an overlay?</p>
          <p>Usually. The overlay sets requirements &mdash; mainly floor height &mdash; that the design has to meet. It's paperwork and design, not a bar.</p>
        </div>
        <div>
          <p class="q">Can you read the report for us?</p>
          <p>Yes. Bring it to the walk-through or we'll pull it together, and Nathan will tell you what the levels do to a design on your block.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <a href="https://www.brisbane.qld.gov.au/planning-and-building/planning-guidelines-and-tools/online-tools/floodwise-property-reports" rel="noopener">FloodWise Property Reports</a> and <a href="https://fam.brisbane.qld.gov.au/" rel="noopener">Flood Awareness Online</a>; Brisbane City Plan 2014. Read 17 September 2026. Council's flood information changes; read the current report for your lot before you decide anything. Not planning, engineering or insurance advice.</p>
''')

# ---------------------------------------------------------------- R25 · things to do with kids
POSTS["r25-kids"] = dict(
    slug="what-to-do-in-wynnum-and-manly-with-kids",
    section="living",
    title="What is there to do in Wynnum and Manly with kids?",
    h1="What is there to do in<br>Wynnum and Manly with kids?",
    description="The tidal wading pool, the jetty, Pandanus Beach, the parklands, the harbour, the train. A local's list, and why the families who use it every weekend end up rebuilding rather than leaving.",
    lede="Not a tourist list. This is what Bayside families actually do with their kids on a Saturday, from people who've raised theirs here. Then the honest bit about why so many of those families end up changing the house instead of the suburb.",
    date="2026-09-17", category="Living on the Bayside", image="blog/what-to-do-in-wynnum-and-manly-with-kids.jpg",
    image_alt="Kids paddling in the tidal wading pool beside the jetty, bikes and towels on the grass",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of the real street.",
    label=('Wynnum &amp; Manly', 'With kids'),
    figure=dict(image="blog/what-to-do-in-wynnum-and-manly-with-kids.png", alt='Map of the Wynnum-Manly foreshore: wading pool and jetty, Eastwood Beach, Cambridge Parade, the boat harbour and the stations', caption='Boundaries &copy; OpenStreetMap contributors.', after='the-water'),
    card_title="What is there to do in Wynnum and Manly with kids?",
    card_blurb="The wading pool, the jetty, Pandanus Beach, sixteen kilometres of parklands, the harbour, the train. A local's list, and why those families end up rebuilding rather than leaving.",
    about=["Wynnum", "Manly", "Families", "Living on the Bayside"],
    related=["is-wynnum-a-good-place-to-live", "schools-on-the-bayside-catchments", "wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family"],
    cta="If the weekends are right and the house isn't, that's the walk-through.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>The water, mostly, and it's free. The Wynnum Wading Pool on the esplanade is a tidal pool with a playground and water park beside it; Pandanus Beach next to the jetty is sand brought from North Stradbroke Island; the Bayside Parklands run sixteen kilometres along the shore through mangroves and wetlands where migratory birds land every year.</p>
        <p>At the Manly end there's the boat harbour, the esplanade to walk or ride, and the village on Cambridge Parade. In between, the foreshore path connects the lot. Add the train to the city, and a weekend fills itself.</p>
        <p>The families who do this every Saturday are the ones who don't leave. They change the house.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#the-water">What's on the water?</a></li>
          <li><a href="#the-parks">What's in the parks?</a></li>
          <li><a href="#manly">What's at the Manly end?</a></li>
          <li><a href="#wet-days">What about wet days and the city?</a></li>
          <li><a href="#the-house">Why these families rebuild instead of leaving</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="the-water">What's on the water?</h2>
      <ul class="pts">
        <li><strong>Wynnum Wading Pool.</strong> A tidal pool on the esplanade, also called the Manly Wading Pool depending on who you ask, with a playground and a water park beside it. The default answer to &ldquo;what are we doing today.&rdquo;</li>
        <li><strong>Pandanus Beach.</strong> Next to the wading pool and the jetty. It's a made beach &mdash; sand brought from North Stradbroke Island in 1987 and held by rock groynes &mdash; and at high tide it's a real swim.</li>
        <li><strong>Wynnum Jetty.</strong> For walking out, fishing off, and watching the tide do its thing. The first jetty here was built in the 1850s with the help of Aboriginal men from the local camp.</li>
        <li><strong>The tide itself.</strong> Low tide takes the water out a long way and leaves mudflats, soldier crabs and birds. Kids who grow up here learn the tide chart before they learn the bus timetable.</li>
      </ul>

      <blockquote class="proof">
        <p><b>&ldquo;The Bayside Parklands provide public access to 16 kilometres of shoreline including mangroves, mudflats and wetlands. Many migratory shorebirds can be seen from the parklands as Moreton Bay is a Ramsar site.&rdquo;</b></p>
        <cite>Wynnum, as recorded on Wikipedia from Brisbane City Council sources. Sixteen kilometres of coast, and a wetland listed under an international treaty, at the end of the street.</cite>
      </blockquote>

      <h2 class="h2" id="the-parks">What's in the parks?</h2>
      <p>The esplanade is one long park with the wading pool in the middle. Behind it, Memorial Park &mdash; Russell Park, as it was &mdash; gave up a corner for the high school in the 1940s. Elanora Park was laid out in the 1930s on the site of the old Aboriginal camp. Kitchener Park is on Bridge Street.</p>
      <p>The foreshore path runs the length of Wynnum and Manly, flat, sealed, and used by every scooter and bike on the Bayside. Most families' Saturday is some combination of the path, the pool and the jetty, in whichever order the tide allows.</p>

      <h2 class="h2" id="manly">What's at the Manly end?</h2>
      <ul class="pts">
        <li><strong>Manly Boat Harbour.</strong> A 41.8-hectare marina south of Norfolk Point, and the reason Manly is the boating suburb. Even without a boat, the harbour walls and the breakwater are a walk.</li>
        <li><strong>Cambridge Parade.</strong> The village. Cafes, the bakery, fish and chips on the grass with the harbour in front of you.</li>
        <li><strong>Darling Point and Rose Bay.</strong> The bits of coast between Wynnum and the harbour: Eastwood Beach, the point, the rocks at low tide.</li>
      </ul>

      <h2 class="h2" id="wet-days">What about wet days and the city?</h2>
      <p>The Cleveland line. Three stations in Wynnum and one in Manly, a forty-minute all-stops run to Central, no change. South Bank, the museum and the city are a train ride with the kids, not a car park search. <a href="../how-far-is-wynnum-from-brisbane-cbd/">The real timetable is here.</a></p>
      <p>And storm season, October to March, is its own entertainment from a verandah &mdash; which brings us to the houses.</p>

      <h2 class="h2" id="the-house">Why these families rebuild instead of leaving</h2>
      <p>Everything on this page is free, close, and doesn't change. The wading pool, the path, the harbour and the train will be the same when the kids are teenagers. That's the thing families work out after a few years here: the suburb is finished. It doesn't need anything.</p>
      <p>The house usually does. The post-war cottage that was fine with one baby has two teenagers in it now, one bathroom, and nowhere to put a bike. And the answer to that is not a suburb with a better wading pool. There isn't one.</p>
      <p>So the family stays, and the house changes. Sometimes a raise, sometimes an extension, sometimes a knockdown rebuild on the same flat block, a walk from the same pool. <a href="../why-are-so-many-bayside-houses-being-knocked-down/">Why that's so common here is its own page.</a></p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>The water is the answer:</b> the wading pool, Pandanus Beach, the jetty, the tide.</li>
          <li><b>Sixteen kilometres of parklands</b> on a Ramsar-listed bay, with a flat path the whole way.</li>
          <li><b>Manly is the harbour and the village;</b> Wynnum is the pool and the town.</li>
          <li><b>The train makes the city a family outing,</b> not a car park search.</li>
          <li><b>The suburb is finished. The house usually isn't.</b> That's why families here rebuild.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Is the wading pool open all year?</p>
          <p>It's a tidal pool on the foreshore, so it's there all year; whether you'd swim in July is a different question. Council maintains it &mdash; check council's site for any closures.</p>
        </div>
        <div>
          <p class="q">Can you swim off the beach?</p>
          <p>At Pandanus Beach when the tide is in, yes. At low tide the bay is mudflats a long way out. That's Moreton Bay, not a fault.</p>
        </div>
        <div>
          <p class="q">Is it good for teenagers?</p>
          <p>The train is the honest answer. Teenagers here can get to the city, South Bank and school on their own, which is worth more than any attraction.</p>
        </div>
        <div>
          <p class="q">Which suburb is best for a young family?</p>
          <p>Depends what you want to walk to. <a href="../wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family/">Wynnum, Manly and Lota compared is here.</a></p>
        </div>
      </div>

      <p class="small sources">Sources: Wynnum and Manly facts (wading pool, Pandanus Beach 1987, Bayside Parklands, Manly Boat Harbour, parks) as recorded on Wikipedia from Brisbane City Council and Queensland Government sources; Translink Cleveland line timetable sample, 17 September 2026. Read 17 September 2026. Check council's website for current opening and closures. Nothing here is a safety rating.</p>
''')
