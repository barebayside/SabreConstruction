# Phase 5, part B — Spiral 1 without Nathan: S4, S6 (folds in R3), R7, R12, R13, R14.
# Sources read 2026-09-17:
#   Brisbane City Plan 2014 — Dwelling house (small lot) code (v19 text, docs.brisbane.qld.gov.au): applies to a dwelling house on a small lot;
#     in the Low density residential zone the acceptable outcome is a maximum building height of 7.5 m at side and rear walls, rising at no
#     more than 30 degrees to 9.5 m, and 2 storeys; small lot = under 450 m² (council's Subdividing land fact sheet)
#   Brisbane City Council — "Building a new house" (Dwelling house code / small lot code; code-assessable overlays); "Demolition or removal"
#   Brisbane City Council — "Protected vegetation"; "FloodWise Property Reports"
#   QBCC — Consumer Building Guide v3 (licence check, contract, implied warranties)
#   asbestos.qld.gov.au — houses built before 1990 are likely to contain asbestos (as cited in the asbestos post)
# Rule 1: no prices, no bands, no timelines.

POSTS = {}

# ---------------------------------------------------------------- S4 · buying to knock down
POSTS["s4-buying-to-knock-down"] = dict(
    slug="buying-an-old-house-in-wynnum-or-manly-to-knock-down-what-to-check-before-you-sign",
    section="rules",
    title="Buying an old house in Wynnum or Manly to knock down: what to check before you sign",
    h1="Buying an old house in Wynnum or Manly<br>to knock down: what to check before you sign.",
    description="Eight checks on the block, not the house: the year it was built, the character overlay, the flood report, the trees, the slope and access, the ground, the boundaries and the contract conditions. A builder's list, in the order to run it.",
    lede="If you're buying the house for the block, the house doesn't matter and the block matters completely. Most of what decides whether a rebuild will work is public and free to check before you sign. Here's the list a builder would run on it, in order.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/buying-an-old-house-in-wynnum-or-manly-to-knock-down-what-to-check-before-you-sign.jpg",
    image_alt="A couple on the footpath outside an old Bayside cottage with a For Sale board, phone out, checking the block",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real street.",
    label=("Eight checks before you sign", "Buying to knock down"),
    card_title="Buying an old house in Wynnum or Manly to knock down: what to check before you sign",
    card_blurb="Eight checks on the block, not the house: the year, the character overlay, the flood report, the trees, the slope, the ground, the boundaries and the contract. In the order to run them.",
    about=["Buying to knock down and rebuild", "Wynnum", "Manly", "Character overlay", "Knockdown rebuild"],
    related=["can-we-knock-down-our-house", "check-if-your-street-is-in-the-character-overlay", "rebuilding-in-wynnum-or-manly"],
    cta="Thinking about a block that's on the market? Nathan will walk it with you before you make an offer, and tell you what it would and wouldn't let you build.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Check the block, not the house. In order: the year the house was built and whether the street is in Brisbane's character overlay (a pre-1947 house there may not be allowed to come down); council's FloodWise report on the lot; protected trees; the slope and the access; what's known about the ground; the boundaries and any easements; and what the contract lets you do if a check fails.</p>
        <p>Every one of those is public. The overlay and flood maps are on council's website. The year is in council's archives. The trees are in a council report you can request. The rest a builder reads off the block in an hour.</p>
        <p>The order matters because the first two can end the conversation. A house that council won't let you demolish is not a knockdown rebuild, whatever the listing says.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#year-and-overlay">1 and 2: the year, and the character overlay</a></li>
          <li><a href="#flood">3: the flood report</a></li>
          <li><a href="#trees">4: the trees</a></li>
          <li><a href="#slope-access">5: slope and access</a></li>
          <li><a href="#ground">6: the ground</a></li>
          <li><a href="#boundaries">7: boundaries, easements and services</a></li>
          <li><a href="#contract">8: the contract</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="year-and-overlay">1 and 2: the year, and the character overlay</h2>
      <p>Do these first, together, because between them they decide whether the house can come down at all.</p>
      <p>Council's demolition rules say planning approval is needed to demolish a building in the traditional building character overlay if the whole building was built before 1947, and for anything in the pre-1911 overlay or on a heritage register. Approval isn't automatic. If the house is genuinely pre-1947 and the street is in the overlay, you may be buying a renovation.</p>
      <p><a href="../check-if-your-street-is-in-the-character-overlay/">How to check the street takes five minutes.</a> The year comes from council's archives, or from the agent if they can prove it. Don't take &ldquo;1950s&rdquo; on trust; ask for the source. <a href="../can-we-knock-down-our-house/">The rules themselves are here.</a></p>

      <h2 class="h2" id="flood">3: the flood report</h2>
      <p>Pull council's FloodWise Property Report on the address. It's free and it takes a minute. It tells you which kinds of flooding council maps on the lot, the flood levels, and the minimum habitable floor level a new house would have to meet.</p>
      <p>A flood overlay rarely stops a Bayside rebuild. It does decide whether the house you're imagining is the house you'd get: a lot with a high minimum floor level is a highset house or a house with the garage downstairs, not a lowset one. <a href="../rebuilding-on-a-flood-overlay-block-on-the-bayside/">What that changes is here.</a></p>

      <h2 class="h2" id="trees">4: the trees</h2>
      <p>Brisbane protects mature or prominent trees on private land under its Natural Assets Local Law, and it's an offence to remove or lop a protected one without a permit. Ask council for a protected vegetation report on the property. If the big tree in the middle of the block is on it, the design will bend around it. <a href="../what-happens-to-the-trees-on-the-block-in-a-knockdown-rebuild/">More here.</a></p>

      <h2 class="h2" id="slope-access">5: slope and access</h2>
      <p>Stand on the footpath and look.</p>
      <ul class="pts">
        <li><strong>Which way does the block fall,</strong> and how much? A slope toward the bay means a highset or split design, retaining, or cut and fill. All real work, all before the house.</li>
        <li><strong>How wide is the frontage,</strong> and what's in it? Power lines, a street tree, a narrow crossover and a neighbour built to the boundary change what machinery gets in and how materials arrive.</li>
        <li><strong>Where would the excavator go?</strong> If the answer is &ldquo;through the neighbour's yard,&rdquo; that's a conversation you want before you own the block.</li>
      </ul>

      <h2 class="h2" id="ground">6: the ground</h2>
      <p>You can't drill a soil test on a block you don't own, but you can read the signs. Cracked slabs under the old house, stumps that have moved, doors that bind, and a low, flat block near a creek or the foreshore all hint at reactive clay or fill. Old fill is common on the flats behind the esplanade. The test comes after settlement; the hints come before. <a href="../what-is-a-soil-test-and-why-does-it-change-the-price/">What the test does is here.</a></p>

      <h2 class="h2" id="boundaries">7: boundaries, easements and services</h2>
      <p>Get the title search and the survey plan. Look for easements (a sewer main across the back corner limits where you can build), the position of the sewer and stormwater connections, and whether the fences are actually on the boundaries. On old Bayside blocks they often aren't. Ask where the old septic was, if the house predates the sewer.</p>

      <h2 class="h2" id="contract">8: the contract</h2>
      <p>This is where you protect yourself, and it's a conversation with your solicitor, not us. The principle is simple: if a check can't be finished before you sign, make the contract conditional on it. A building and pest inspection is normal; on a knockdown, the inspection you care about is different, and we've written about that separately. What you want is the freedom to walk away if the overlay, the flood report or the soil turns out to be something other than you were told.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Before committing, check the contractor's licence and history via the QBCC Online Licence Search or by calling the QBCC.&rdquo;</b> The same habit applies to the block: check the public record before you commit, not after.</p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023. It's about builders, and it's the right instinct for buying too.</cite>
      </blockquote>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>The year and the overlay come first.</b> A pre-1947 house in the character overlay may not be allowed to come down.</li>
          <li><b>Pull the FloodWise report</b> before you fall for a lowset plan on a lot that wants a highset.</li>
          <li><b>Ask council for the protected vegetation report.</b> The big tree may be staying.</li>
          <li><b>Slope, access, ground and boundaries</b> are read from the footpath and the title.</li>
          <li><b>Make the contract conditional on what you can't check first.</b> That's your solicitor's job; asking is yours.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">The listing says &ldquo;knockdown rebuild opportunity.&rdquo; Can we rely on that?</p>
          <p>No. It's an agent's description, not a council approval. Check the year and the overlay yourself; it takes minutes and it's the check that matters most.</p>
        </div>
        <div>
          <p class="q">Can a builder look at the block before we buy?</p>
          <p>Yes, and it's the best hour you'll spend. Nathan walks blocks that are on the market. He'll tell you what the slope, the access and the overlays would do to a design, and what he'd want to know before you sign.</p>
        </div>
        <div>
          <p class="q">What if the house is pre-1947 but we'd like to keep it anyway?</p>
          <p>Then the overlay is on your side. A renovation of a character house at the back and underneath is usually simpler than changing the front. Different job, different post: <a href="../knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is/">rebuild or renovate is here</a>.</p>
        </div>
        <div>
          <p class="q">Is a house with asbestos a reason not to buy?</p>
          <p>On the Bayside it's most houses built before 1990, so no. It's a known job with licensed removal before demolition. It's a cost, not a barrier.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <em>Demolition or removal</em>, <em>Protected vegetation</em>, <em>FloodWise Property Reports</em>; Brisbane City Plan 2014; Queensland Building and Construction Commission, <em>Consumer Building Guide</em> v3. Read 17 September 2026. This is a plain-English guide from a builder, not legal, conveyancing or financial advice. Talk to your solicitor about contract conditions.</p>
''')

# ---------------------------------------------------------------- S6 · small or narrow block (folds in R3)
POSTS["s6-small-block"] = dict(
    slug="can-you-knock-down-and-rebuild-on-a-small-or-narrow-block-in-brisbane",
    section="rules",
    title="Can you knock down and rebuild on a small or narrow block in Brisbane?",
    h1="Can you knock down and rebuild on a<br>small or narrow block in Brisbane?",
    description="Yes. Brisbane City Plan has a code just for houses on small lots (under 450 square metres): two storeys, a height envelope, setbacks and site cover that shape the design. What a small lot is, what the code does, and what it means for the house.",
    lede="A lot of the older Bayside streets were cut up small, and the newer estates are smaller again. Brisbane's planning scheme doesn't stop you building on a small block. It gives the house its own code, and the code shapes what you get. Here's what it says, in plain words, and what a builder does with it.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/can-you-knock-down-and-rebuild-on-a-small-or-narrow-block-in-brisbane.jpg",
    image_alt="A narrow two-storey home going up between two old Bayside cottages, the frame tight to the boundaries",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real job.",
    label=("City Plan's small lot code", "Small or narrow block"),
    card_title="Can you knock down and rebuild on a small or narrow block in Brisbane?",
    card_blurb="Yes. Brisbane City Plan has a code just for houses on lots under 450 square metres. What a small lot is, what the code does to height, setbacks and site cover, and what that means for the design.",
    about=["Small lot Brisbane", "Dwelling house (small lot) code", "Brisbane City Plan 2014", "Knockdown rebuild"],
    related=["does-a-knockdown-rebuild-need-a-development-application", "what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane", "whats-the-difference-between-manly-and-manly-west"],
    cta="Nathan measures the block, reads the code against it and tells you what house it will take &mdash; before a plan is drawn to the wrong envelope.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Yes. Brisbane City Plan 2014 treats a lot under 450 square metres as a <strong>small lot</strong>, and a house on one is assessed against the <strong>Dwelling house (small lot) code</strong> instead of the ordinary Dwelling house code. If the design meets the code, it's accepted development and doesn't need a development application on its own account.</p>
        <p>The code shapes the house. In the low density residential zone the acceptable outcome is a building height of 7.5 metres at the side and rear walls, rising at no more than 30 degrees to a maximum of 9.5 metres, and two storeys. Setbacks, site cover, private open space and car parking all have their own outcomes.</p>
        <p>In practice that means a two-storey house that stands close to the boundaries, with the envelope stepping in at the top, and a design that uses every metre carefully. It's a different house from one on a quarter-acre. It's often a very good one.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-is-small">What counts as a small lot?</a></li>
          <li><a href="#the-code">What does the small lot code actually say?</a></li>
          <li><a href="#narrow">What about a narrow block that isn't small?</a></li>
          <li><a href="#the-design">What does it do to the design?</a></li>
          <li><a href="#approval">Does a small lot need a DA?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-is-small">What counts as a small lot?</h2>
      <p>Council's definition is by area: a lot smaller than 450 square metres, or a rear (battle-axe) lot smaller than 600 square metres excluding the access strip.</p>
      <p>That catches more Bayside blocks than people expect. Some of the older streets in Wynnum and Manly were subdivided small a century ago. The newer estates in Wakerley and parts of Manly West were cut small on purpose. The only way to know is the survey plan or council's City Plan online tool, which shows the lot area by address.</p>

      <h2 class="h2" id="the-code">What does the small lot code actually say?</h2>
      <p>Its purpose, in council's words, is to assess the suitability of development on a small lot. The parts that shape a house, in the low density residential and character residential zones:</p>
      <ul class="pts">
        <li><strong>Height.</strong> A maximum of 7.5 metres above ground at the side and rear walls, increasing at no more than 30 degrees to a maximum of 9.5 metres, and two storeys. That angled envelope is why small-lot houses step in at the top.</li>
        <li><strong>Setbacks.</strong> Minimum distances from the street and the side and rear boundaries, with reduced side setbacks allowed for habitable space on small lots, and provision for built-to-boundary walls.</li>
        <li><strong>Site cover.</strong> A maximum share of the lot the house can cover.</li>
        <li><strong>Car parking.</strong> Where a garage is provided, a parking space in front of it, and a street-frontage setback for the garage.</li>
        <li><strong>Privacy and open space.</strong> Outcomes for overlooking and for a usable outdoor area.</li>
      </ul>

      <blockquote class="proof">
        <p><b>In the Low density residential zone, the acceptable outcome is a &ldquo;maximum building height of 7.5m above ground level at side and rear walls, increasing at no more than 30 degrees to a maximum building height of 9.5m above ground level&rdquo; and two storeys.</b></p>
        <cite>Brisbane City Council, Brisbane City Plan 2014, <em>Dwelling house (small lot) code</em>, section 9.3.8. The exact figures are in the current version of the code; the designer works to that.</cite>
      </blockquote>

      <h2 class="h2" id="narrow">What about a narrow block that isn't small?</h2>
      <p>A long thin block of 500 or 600 square metres isn't a small lot, so the ordinary Dwelling house code applies. But the frontage still decides the house.</p>
      <p>A narrow frontage means the house is long and the living areas can't all face the street. Side setbacks eat a bigger share of the width. Access for machinery and deliveries is tighter. The design answer is usually the same as on a small lot: go up, put the living area at the back or upstairs where the light is, and treat the side boundaries as walls to design against rather than gaps to waste.</p>

      <h2 class="h2" id="the-design">What does it do to the design?</h2>
      <p>Four things a builder plans for on a small or narrow Bayside block:</p>
      <ul class="pts">
        <li><strong>Two storeys, nearly always.</strong> The floor area the family needs won't fit on one level inside the site cover and setbacks.</li>
        <li><strong>The envelope shapes the roof.</strong> The 30-degree plane from the 7.5-metre side wall is why the upper floor steps in or the roof pitches inward.</li>
        <li><strong>Light comes from above and behind.</strong> With neighbours close on both sides, the design puts glass on the street, the rear and the roof, not the sides.</li>
        <li><strong>The build is tighter.</strong> Scaffolding, deliveries, the crane for the frame, the excavator &mdash; all of it happens within a few metres of two neighbours. That's a planning job, and the neighbours should hear about it before the first truck.</li>
      </ul>
      <p>A package plan drawn for an estate lot usually doesn't fit a small Bayside block, for the same reason it doesn't fit a sloping one: it wasn't drawn for the envelope. <a href="../what-is-a-knockdown-rebuild-package/">That post is here.</a></p>

      <blockquote class="proof">
        <p><b>&ldquo;The block size and the shape of the block will change dramatically what you can fit on there, and what kind of layout. And if the street&rsquo;s heritage listed, you may need to tie in with the buildings around you.&rdquo;</b></p>
        <cite>Nathan Brain, builder at Sabre, on camera, October 2026.</cite>
      </blockquote>

      <h2 class="h2" id="approval">Does a small lot need a DA?</h2>
      <p>Not because it's small. Council's guidance is that a house that complies with the small lot code (and any other applicable code) is accepted development, so it goes straight to a building certifier. It needs a development application for the same reasons any house does: a code-assessable overlay on the lot, such as flood, character or a mapped tree. <a href="../does-a-knockdown-rebuild-need-a-development-application/">The two approvals are explained here.</a></p>
      <p>If the design can't meet the code &mdash; a wall higher than the envelope, a setback shorter than the outcome &mdash; it becomes assessable, and that's usually where a good designer changes the design rather than lodging the application.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Under 450 square metres is a small lot,</b> and a house on it is assessed against the small lot code.</li>
          <li><b>Two storeys, 7.5 metres at the side walls rising to 9.5,</b> in the low density zone. The envelope shapes the roof.</li>
          <li><b>Narrow blocks that aren't small still design like small ones:</b> go up, light from above and behind.</li>
          <li><b>Small doesn't mean a DA.</b> Comply with the code and it's accepted development; overlays are what trigger applications.</li>
          <li><b>The build is tight.</b> Tell the neighbours, plan the deliveries, design to the boundaries.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can we build to the side boundary?</p>
          <p>The code makes provision for built-to-boundary walls and reduced side setbacks on small lots, with limits on length and height. Whether your block can depends on what the neighbours have and the current version of the code. A designer who works in the code will tell you.</p>
        </div>
        <div>
          <p class="q">Is a small lot harder to build on?</p>
          <p>Tighter, not harder. The design work is more careful and the site logistics take more planning. The house that comes out of it is often more thoughtful for it.</p>
        </div>
        <div>
          <p class="q">How do we find out our lot size?</p>
          <p>The survey plan on your title, or council's City Plan online tool by address. Don't guess from the fence lines; on old blocks they aren't always on the boundary.</p>
        </div>
        <div>
          <p class="q">Does the code change?</p>
          <p>Yes. City Plan is amended from time to time, and the figures here are from the version read on the date below. The designer and certifier work to the version in force when the application is made.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, Brisbane City Plan 2014, <a href="https://docs.brisbane.qld.gov.au/City%20Plan/v19_00_20200501/TEXT/Part%209%20-%20Development%20codes/DwellingHseSmallLotCode.docx" rel="noopener">Dwelling house (small lot) code</a> (section 9.3.8) and <em>Subdividing land</em> fact sheet (small lot definition); <a href="https://www.brisbane.qld.gov.au/building-and-planning/getting-started-on-your-project/residential-projects/new-house" rel="noopener">Building a new house: approvals and requirements</a>. Read 17 September 2026. City Plan is amended; check the current code for your lot. This is a plain-English guide, not planning advice.</p>
''')

# ---------------------------------------------------------------- R7 · keep the pool, the shed, the fence
POSTS["r7-keep-pool-shed-fence"] = dict(
    slug="can-we-keep-the-pool-the-shed-or-the-front-fence-in-a-knockdown-rebuild",
    section="rebuild",
    title="Can we keep the pool, the shed or the front fence in a knockdown rebuild?",
    h1="Can we keep the pool, the shed or the<br>front fence in a knockdown rebuild?",
    description="Sometimes, and it's worth asking. What decides whether a pool, a shed, a fence, a driveway or a retaining wall survives a rebuild: where it sits, what it's made of, what the machinery needs, and what the rules say about it.",
    lede="Nobody wants to pay to demolish a pool they like. Whether it can stay is a real question with a real answer, and the answer is different for the pool, the shed, the fence and the driveway. Here's what decides each one.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/can-we-keep-the-pool-the-shed-or-the-front-fence-in-a-knockdown-rebuild.jpg",
    image_alt="A cleared block with the old pool fenced off and kept, the new slab poured beside it, the front fence still standing",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real job.",
    label=("What stays and what goes", "The pool, the shed, the fence"),
    card_title="Can we keep the pool, the shed or the front fence in a knockdown rebuild?",
    card_blurb="Sometimes. What decides whether the pool, the shed, the fence, the driveway or the retaining wall survives: where it sits, what it's made of, what the machinery needs, and the rules.",
    about=["Knockdown rebuild", "Swimming pool", "Demolition", "Brisbane Bayside"],
    related=["what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane", "what-happens-to-the-trees-on-the-block-in-a-knockdown-rebuild", "how-much-of-the-old-house-can-be-reused"],
    cta="Walk Nathan around the yard and point at what you'd like to keep. He'll tell you what can stay, what it costs to keep it, and what it does to the design.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Sometimes. A pool can often stay if it's sound, it isn't where the new house or the machinery needs to be, and the new design is drawn around it. A shed can stay if it's clear of the work and legally there. A front fence can stay if it isn't in the way of the crossover and the deliveries. A driveway usually goes, because the new house rarely sits where the old one did.</p>
        <p>What decides it is position, condition, access and rules. Position: is it where the house, the excavator or the crane needs to be? Condition: is it worth keeping? Access: can the job happen around it? Rules: pool fencing, boundary setbacks and council's requirements still apply to anything that stays.</p>
        <p>Keeping something isn't free. Protecting a pool through a demolition and a build is work, and a kept fence can cost more in slow deliveries than a new one. Ask for the honest comparison.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#pool">Can the pool stay?</a></li>
          <li><a href="#shed">Can the shed stay?</a></li>
          <li><a href="#fence">Can the front fence stay?</a></li>
          <li><a href="#driveway">What about the driveway and retaining walls?</a></li>
          <li><a href="#the-cost-of-keeping">What does keeping something cost?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="pool">Can the pool stay?</h2>
      <p>This is the one people care about most, and the one with the most conditions.</p>
      <ul class="pts">
        <li><strong>Position.</strong> If the pool sits where the new house goes, or where the excavator has to pass to get to the back, it goes. If it's in a corner the design can leave alone, it can stay.</li>
        <li><strong>Condition.</strong> A concrete pool with a sound shell and working plumbing is worth keeping. A fibreglass shell that's lifted, or a pool with old pipework you can't trace, is a liability under a new house.</li>
        <li><strong>The work around it.</strong> Demolition next to a pool means protecting the shell from machinery, keeping rubble out of it, and dealing with a big hole full of water on a construction site for months. It's done; it's planned for.</li>
        <li><strong>The rules.</strong> Pool safety barriers are law in Queensland and the new fence and the new house have to meet them. A kept pool is a design input like the floor level: the barrier, the doors and the windows facing it all have to comply.</li>
      </ul>

      <h2 class="h2" id="shed">Can the shed stay?</h2>
      <p>Usually the easiest yes, if two things are true: it's out of the way, and it was approved.</p>
      <p>A shed at the back corner, clear of the house footprint and the machinery path, can be left alone and worked around. A shed that was never approved, or that sits inside a setback, can become a problem when the certifier looks at the whole site for the new house. Council's demolition page notes you don't need planning approval to demolish a free-standing outbuilding built after 1946, which is often the simpler path if the shed is marginal.</p>

      <h2 class="h2" id="fence">Can the front fence stay?</h2>
      <p>Often, and it depends on the crossover.</p>
      <p>The trucks, the excavator and the frame delivery come through the front. If the existing crossover and gate are wide enough and in the right place for the new driveway, the fence can stay and be protected. If the new house moves the driveway, a section comes out and goes back later. A heritage-style timber fence on an old Wynnum street is worth the trouble; a tired paling fence usually isn't.</p>

      <h2 class="h2" id="driveway">What about the driveway and retaining walls?</h2>
      <p>The driveway almost always goes. The new house rarely sits exactly where the old one did, and the garage rarely lands where the carport was. The old slab is broken up with the rest.</p>
      <p>Retaining walls are different. A sound engineered wall holding a sloped Bayside block can be the most valuable thing on the site, and the design keeps it. A stack of sleepers leaning outward is not a retaining wall for a new house's purposes, and the engineer will say so.</p>

      <h2 class="h2" id="the-cost-of-keeping">What does keeping something cost?</h2>
      <p>Ask for it as a comparison, not a yes or no. Keeping a pool means protection, slower machinery access, and design constraints. Keeping a fence can mean a section removed and reinstated. Sometimes the honest answer is that demolishing and replacing is cheaper than protecting, and sometimes it isn't. A builder should be able to tell you which before the design is finished.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Position, condition, access, rules.</b> Those four decide everything in the yard.</li>
          <li><b>A sound pool out of the machinery's way can stay,</b> and the new house is designed to the pool barrier laws around it.</li>
          <li><b>An approved shed clear of the work stays easily.</b> An unapproved one is simpler gone.</li>
          <li><b>The fence depends on the crossover.</b> The driveway almost always goes.</li>
          <li><b>Keeping isn't free.</b> Ask for the comparison, not the wish.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Does a kept pool need a new fence?</p>
          <p>Whatever is around it at the end has to meet Queensland's pool safety laws, and the new house's doors and windows facing the pool are part of that. Usually the barrier is redone as part of the landscaping. The pool safety certificate is checked at the end.</p>
        </div>
        <div>
          <p class="q">Can we keep the old carport?</p>
          <p>Only if it's clear of the new house, structurally sound and legally there. Most aren't all three. It's often the first thing to go, because it's where the site sheds and the deliveries end up.</p>
        </div>
        <div>
          <p class="q">What about the old mango tree by the pool?</p>
          <p>Trees are a different rule. If it's mature and prominent it may be protected under council's local law regardless of what you'd like. <a href="../what-happens-to-the-trees-on-the-block-in-a-knockdown-rebuild/">That post is here.</a></p>
        </div>
        <div>
          <p class="q">Who decides what stays?</p>
          <p>You do, with the facts. The builder tells you what's possible and what it costs; the designer draws around it; the certifier and the engineer check that what stays meets the rules.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <em>Demolition or removal</em> (free-standing outbuildings built after 1946); Queensland Government, pool safety laws (barriers and pool safety certificates); Brisbane City Plan 2014, Dwelling house code. Read 17 September 2026. This is a plain-English guide from a builder, not legal or engineering advice.</p>
''')

# ---------------------------------------------------------------- R12 · highset
POSTS["r12-highset"] = dict(
    slug="what-does-highset-mean-on-a-bayside-block",
    section="rebuild",
    title="What does &ldquo;highset&rdquo; mean on a Bayside block?",
    h1="What does &ldquo;highset&rdquo; mean<br>on a Bayside block?",
    description="Brisbane's word for a house lifted off the ground on stumps or posts, with the living upstairs and the space below open or built in. Where it came from, why the Bayside has so many, when a new house is designed highset, and what it does and doesn't give you.",
    lede="You'll see it in every Bayside listing: highset, lowset, built-in-under. Nobody explains it because everybody local knows. If you're new, or you're deciding what to build next, here's what the word means, why the Bayside is full of them, and when a new house is drawn highset on purpose.",
    date="2026-09-17", category="Living on the Bayside", image="blog/what-does-highset-mean-on-a-bayside-block.jpg",
    image_alt="A classic highset Queensland house on tall stumps, the open space underneath, a car parked under it",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real house.",
    label=("Local vocabulary", "Highset"),
    card_title="What does &ldquo;highset&rdquo; mean on a Bayside block?",
    card_blurb="Brisbane's word for a house lifted off the ground, living upstairs, space below. Why the Bayside has so many, when a new house is designed that way, and what it gives you.",
    about=["Highset house", "Queenslander", "Brisbane Bayside", "Knockdown rebuild"],
    related=["what-are-bayside-houses-made-of", "rebuilding-on-a-flood-overlay-block-on-the-bayside", "knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is"],
    cta="Wondering whether your block wants a highset? Nathan will tell you from the slope, the flood report and the ground, at the walk-through.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>A <strong>highset</strong> house is one lifted off the ground high enough to use the space underneath: on timber stumps or steel posts, with the living areas upstairs. A <strong>lowset</strong> house sits on the ground, on a slab or low stumps. <strong>Built-in-under</strong> is a highset whose underneath has been closed in for rooms, a garage or a rumpus, usually decades after it was built.</p>
        <p>The Bayside has so many because the old timber houses were built that way for air, for the slope and for the damp, and because the 1950s and 60s highsets gave families a cheap way to double the house later.</p>
        <p>A new house is designed highset today for two reasons that haven't changed &mdash; a sloping block and a flood level &mdash; and one that has: the breeze and the view off the bay are worth going up for.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#the-words">Highset, lowset, built-in-under: the words</a></li>
          <li><a href="#why-so-many">Why does the Bayside have so many?</a></li>
          <li><a href="#new-highset">When is a new house designed highset?</a></li>
          <li><a href="#what-it-gives">What does a highset give you, and cost you?</a></li>
          <li><a href="#old-highset">What about the old highset you already have?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="the-words">Highset, lowset, built-in-under: the words</h2>
      <ul class="pts">
        <li><strong>Highset.</strong> The floor is well above the ground &mdash; high enough to walk under, park under or build under. Stumps or posts, stairs to the front door, the living upstairs.</li>
        <li><strong>Lowset.</strong> The floor is at or near the ground. A slab, or short stumps you can't stand under.</li>
        <li><strong>Built-in-under.</strong> A highset whose underneath has been enclosed. Sometimes done well, with proper ceiling height and approvals. Often done in the 1970s with fibro sheeting and a low ceiling, which is where a lot of the Bayside's asbestos lives.</li>
        <li><strong>Raise and build under.</strong> The renovation version: lift an old highset higher, then build a full ground floor beneath it.</li>
      </ul>

      <h2 class="h2" id="why-so-many">Why does the Bayside have so many?</h2>
      <p>Three reasons, in order of age.</p>
      <p>The pre-war timber houses went up on stumps because that's how Queensland built: air under the floor for the heat and the damp, easy to level on a slope, and the stumps kept the termites visible. Wynnum and Manly's older streets are full of them.</p>
      <p>The post-war and 1960s highsets were the cheap family house of the day. A timber-framed box upstairs, a concrete slab and posts underneath, and the promise that you could build in downstairs when the kids arrived. Most did. That's the built-in-under.</p>
      <p>And the Bayside slopes toward the water on most of its streets. A highset takes a slope without cut and fill.</p>

      <h2 class="h2" id="new-highset">When is a new house designed highset?</h2>
      <p>Two hard reasons and one good one.</p>
      <ul class="pts">
        <li><strong>The flood level.</strong> Council's FloodWise report gives a minimum habitable floor level. On a low lot near the bay or a creek, meeting it means the living areas go up and the ground floor holds the garage, the laundry and storage. <a href="../rebuilding-on-a-flood-overlay-block-on-the-bayside/">More here.</a></li>
        <li><strong>The slope.</strong> A block that falls toward the water can take a highset with the ground floor at the low end and the upper floor at street level, without retaining walls everywhere.</li>
        <li><strong>The bay.</strong> One storey up is where the breeze and the view start on most Bayside streets. A house that puts the living room there is the reason people stay.</li>
      </ul>

      <blockquote class="proof">
        <p><b>Council's FloodWise Property Report gives the minimum habitable floor level a new house must meet on a lot with flood planning requirements.</b> On the Bayside that level is what most often decides whether the new house is highset or lowset.</p>
        <cite>Brisbane City Council, <em>FloodWise Property Reports</em>, Brisbane City Plan 2014. The report is free and takes a minute to pull for your address.</cite>
      </blockquote>

      <h2 class="h2" id="what-it-gives">What does a highset give you, and cost you?</h2>
      <p>It gives you the ground floor: garage, storage, a rumpus, a flat that can be hosed out if the water ever does come. It gives you the breeze, the outlook and a house that sits the way the street's houses sit.</p>
      <p>It costs you stairs, which matter more at seventy than at forty, and a structure that has to carry the upper floor: posts, a suspended floor, more engineering than a slab on the ground. On a flat, dry block with no flood level, a lowset is the simpler house. The block decides.</p>

      <h2 class="h2" id="old-highset">What about the old highset you already have?</h2>
      <p>It's the most common house on the Bayside, and the most common question. The upstairs is often sound hardwood; the built-in-under is often the problem: low ceilings, fibro, damp, and work that was never approved. The honest options are to renovate the top and redo the bottom, to raise and build under properly, or to start again with a house designed to the flood level and the slope from day one. <a href="../knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is/">How to tell which is here.</a></p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Highset means lifted off the ground with usable space underneath.</b> Lowset sits on the ground. Built-in-under is a highset closed in later.</li>
          <li><b>The Bayside is full of them</b> because of the old timber houses, the 1960s family box, and the slope.</li>
          <li><b>A new highset is drawn for the flood level, the slope, or the bay.</b> Usually one of the first two.</li>
          <li><b>It gives a ground floor and the breeze; it costs stairs and structure.</b> The block decides which is right.</li>
          <li><b>The old built-in-under is usually the problem,</b> not the house on top.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Is a highset the same as a two-storey house?</p>
          <p>Not quite. A two-storey house has two full floors of living. A highset has the living upstairs and a lower level that may be open, part-enclosed or fully built in. The modern versions blur together: a house designed to a flood level with the garage and a rumpus downstairs is both.</p>
        </div>
        <div>
          <p class="q">Does highset mean the house floods less?</p>
          <p>It means the living areas sit above the level council has mapped. What's below that level is built to get wet and be cleaned out. That's the whole point of designing to the report.</p>
        </div>
        <div>
          <p class="q">Can we build a lowset on a flood overlay block?</p>
          <p>It depends on the minimum floor level in the report against the ground level of the lot. Sometimes a slab raised on fill meets it. Sometimes it doesn't and the house goes up. The report and a builder on the block will tell you.</p>
        </div>
        <div>
          <p class="q">Are the old stumps a problem?</p>
          <p>Often. Timber stumps rot and move; concrete ones crack. Restumping is a common Bayside job and the first thing to look at under an old highset. Nathan looks under the house before anything else at a walk-through.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <em>FloodWise Property Reports</em>; State Library of Queensland, <em>Housing a growing state</em> (2014), on the Queensland timber house and the post-war highset; Brisbane City Plan 2014. Read 17 September 2026. Plain-English guidance from a builder, not engineering or planning advice.</p>
''')

# ---------------------------------------------------------------- R13 · two storeys in Manly
POSTS["r13-two-storey-manly"] = dict(
    slug="can-we-build-a-two-storey-house-on-our-block-in-manly",
    section="rules",
    title="Can we build a two-storey house on our block in Manly?",
    h1="Can we build a two-storey house<br>on our block in Manly?",
    description="Almost certainly. In Brisbane's low density residential zone the Dwelling house codes allow two storeys within a height envelope; on small lots that's 7.5 metres at the side walls rising to 9.5. What decides it on a Manly block is the slope, the overlays and the neighbours, not a ban.",
    lede="Manly is hilly, the views are up, and the question comes up on every second block: can we go up? In Brisbane's ordinary residential zones the answer is yes, inside an envelope the planning scheme sets. Here's what the envelope is, what can complicate it on a Manly street, and what a two-storey house on a slope actually looks like.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/can-we-build-a-two-storey-house-on-our-block-in-manly.jpg",
    image_alt="A new two-storey home on a steep Manly street, the upper floor looking over the roofs toward the boat harbour",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real street.",
    label=("The height envelope", "Two storeys in Manly"),
    card_title="Can we build a two-storey house on our block in Manly?",
    card_blurb="Almost certainly. Brisbane's codes allow two storeys inside a height envelope. What decides it on a Manly block is the slope, the overlays and the neighbours, not a ban.",
    about=["Two storey house Manly", "Building height Brisbane", "Manly QLD", "Knockdown rebuild"],
    related=["whats-the-difference-between-manly-and-manly-west", "can-you-knock-down-and-rebuild-on-a-small-or-narrow-block-in-brisbane", "does-a-knockdown-rebuild-need-a-development-application"],
    cta="Nathan reads the slope and the overlays on your Manly block and tells you what a two-storey house there would look like, where the living would go, and what the view would be.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Almost certainly yes. Manly's residential streets sit in Brisbane's low density residential zone or, on some of the older streets, the character residential zone (City Plan online shows which yours is), and in those zones the Dwelling house codes provide for a house of two storeys inside a height envelope. On a small lot the acceptable outcome is 7.5 metres at the side and rear walls, rising at no more than 30 degrees to a maximum of 9.5 metres.</p>
        <p>What decides it on your block isn't a ban. It's the slope (Manly's hills are why people want to go up, and also what the envelope is measured from), the overlays (flood on the low streets, character on the old ones), and the neighbours (overlooking and overshadowing are outcomes in the code).</p>
        <p>A two-storey house on a Manly hill usually puts the living areas upstairs for the view over the harbour and the bedrooms below, or the reverse on a block that falls away at the back. The block tells you which.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#the-envelope">What height does the code allow?</a></li>
          <li><a href="#slope">What does Manly's slope do to it?</a></li>
          <li><a href="#overlays">Which overlays could complicate it?</a></li>
          <li><a href="#neighbours">What about the neighbours' view and privacy?</a></li>
          <li><a href="#the-design">What does a two-storey house on a Manly block look like?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="the-envelope">What height does the code allow?</h2>
      <p>Brisbane City Plan 2014 assesses a house against the Dwelling house code, or the Dwelling house (small lot) code on a lot under 450 square metres. Both set a building height envelope for the low density residential and character residential zones.</p>

      <blockquote class="proof">
        <p><b>The small lot code's acceptable outcome in the low density residential zone is &ldquo;a maximum building height of 7.5m above ground level at side and rear walls, increasing at no more than 30 degrees to a maximum building height of 9.5m above ground level&rdquo; and two storeys.</b></p>
        <cite>Brisbane City Council, Brisbane City Plan 2014, <em>Dwelling house (small lot) code</em>. Two storeys is the ordinary outcome, not an exception. The current code is the one the designer works to.</cite>
      </blockquote>

      <p>&ldquo;Above ground level&rdquo; is the phrase that matters on a hill. The envelope follows the ground, so a house on a slope is measured from the slope, not from the street.</p>

      <h2 class="h2" id="slope">What does Manly's slope do to it?</h2>
      <p>It makes the second storey natural and the measurement careful.</p>
      <p>On a block that falls from the street to the back, a house that's one storey at the street can be two at the rear without going near the envelope. On a block that rises from the street, the opposite: the house steps up the hill and the height is measured at each point. Either way the designer works from a survey with levels on it, not from the fence line.</p>
      <p>Slope also means retaining, cut and fill, and footings that change across the block. <a href="../what-is-a-soil-test-and-why-does-it-change-the-price/">The soil test</a> matters more on a hill, not less.</p>

      <h2 class="h2" id="overlays">Which overlays could complicate it?</h2>
      <ul class="pts">
        <li><strong>Traditional building character.</strong> Manly's older streets around the village and the esplanade are in it. If the house is pre-1947, demolition needs a development application first. A new house in the overlay is also code assessable, so the design is checked against the character code for how it sits in the street.</li>
        <li><strong>Flood and coastal hazard.</strong> The low streets near the harbour and the creek. A minimum habitable floor level can push the living upstairs anyway, which on those blocks makes two storeys the answer rather than the question.</li>
        <li><strong>The neighbourhood plan.</strong> City Plan has a Wynnum&ndash;Manly neighbourhood plan with its own provisions for parts of the area. City Plan online shows whether your lot is in one of them.</li>
      </ul>
      <p>None of these say no to two storeys. They say how, and sometimes they say &ldquo;with an application.&rdquo; <a href="../does-a-knockdown-rebuild-need-a-development-application/">The approvals are explained here.</a></p>

      <h2 class="h2" id="neighbours">What about the neighbours' view and privacy?</h2>
      <p>Views aren't protected by the planning scheme. Privacy and overshadowing are addressed by it: the codes have outcomes for overlooking from upper-floor windows and decks, and for the height at the side boundaries that keeps sun on the neighbour's yard.</p>
      <p>On a Manly hill, where everybody's upper floor looks over somebody's roof, this is mostly design: where the windows go, screening on the side of a deck, the envelope stepping in at the top. It's also good manners. Show the neighbours the plan before the certifier does.</p>

      <h2 class="h2" id="the-design">What does a two-storey house on a Manly block look like?</h2>
      <p>Usually one of two houses.</p>
      <p>On a block with the view to the front or the side, the living areas and the main bedroom go upstairs and the kids, the garage and a second living area go below. On a block that falls away at the back, the house enters at street level, the living opens onto the high side of the yard, and the bedrooms sit downstairs with the ground.</p>
      <p>Either way it's a house drawn to the levels on the survey and the lines in the code, which is the reason a plan drawn for a flat estate lot doesn't work here.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Two storeys is the ordinary outcome</b> in Brisbane's low density and character residential zones.</li>
          <li><b>The envelope is measured above ground level,</b> so on a Manly slope it follows the hill.</li>
          <li><b>Character, flood and neighbourhood plans can add an application,</b> not a ban.</li>
          <li><b>Privacy and shadow are in the code; views aren't.</b> Design the windows and the side height for the neighbours.</li>
          <li><b>The living goes where the view is,</b> and the survey decides which floor that is.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can we go three storeys for the view?</p>
          <p>In the low density residential zone the envelope tops out at 9.5 metres and two storeys, with a third-storey element only in narrow circumstances where the topography requires it. Three full storeys is a different zone or a development application, and usually not the answer on a suburban Manly block.</p>
        </div>
        <div>
          <p class="q">Will a two-storey house need a DA?</p>
          <p>Not for being two storeys. It needs one if the lot has a code-assessable overlay, such as flood, character or a mapped tree, or if the design can't meet the code's outcomes.</p>
        </div>
        <div>
          <p class="q">Is a two-storey house dearer?</p>
          <p>For the same floor area it's often the sensible shape: a smaller slab and roof for the same rooms, and on a slope, less earthwork than spreading a single storey across the hill. What costs more is more house, not more floors.</p>
        </div>
        <div>
          <p class="q">Does the same apply in Wynnum, Lota and Manly West?</p>
          <p>The codes are citywide; the zone and the overlays on your lot are what vary. Wynnum and Lota have the same mix of character streets and flood edges. Manly West is flatter and mostly newer, so the slope question is smaller and the overlay question is often nil.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, Brisbane City Plan 2014, <em>Dwelling house code</em> and <a href="https://docs.brisbane.qld.gov.au/City%20Plan/v19_00_20200501/TEXT/Part%209%20-%20Development%20codes/DwellingHseSmallLotCode.docx" rel="noopener">Dwelling house (small lot) code</a>; <a href="https://www.brisbane.qld.gov.au/building-and-planning/getting-started-on-your-project/residential-projects/new-house" rel="noopener">Building a new house: approvals and requirements</a>. Read 17 September 2026. Zones, overlays and codes are checked per lot on City Plan online and change over time. This is a plain-English guide, not planning advice.</p>
''')

# ---------------------------------------------------------------- R14 · how much can be reused
POSTS["r14-reuse"] = dict(
    slug="how-much-of-the-old-house-can-be-reused",
    section="rebuild",
    title="How much of the old house can be reused in a knockdown rebuild?",
    h1="How much of the old house can be<br>reused in a knockdown rebuild?",
    description="Honestly: very little in the new house, and a fair bit elsewhere. What can come out of an old Bayside house and be used again, what can't and why, and what happens to the rest.",
    lede="It feels wasteful to knock down a house full of hardwood. Some of it can go somewhere useful. Almost none of it can go into the new house, and the reasons are worth knowing before you plan around a pile of old timber. Here's the honest list.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/how-much-of-the-old-house-can-be-reused.jpg",
    image_alt="Salvaged hardwood boards, old casement windows and a set of timber stairs stacked neatly on a cleared block",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real job.",
    label=("The honest list", "What can be reused"),
    card_title="How much of the old house can be reused?",
    card_blurb="Honestly: very little in the new house, and a fair bit elsewhere. What comes out of an old Bayside house and gets used again, what can't and why, and where the rest goes.",
    about=["Salvage", "Demolition", "Knockdown rebuild", "Queenslander timber"],
    related=["what-are-bayside-houses-made-of", "what-asbestos-removal-means-for-a-knockdown-rebuild", "can-we-keep-the-pool-the-shed-or-the-front-fence-in-a-knockdown-rebuild"],
    cta="Tell Nathan what you'd like to keep from the old house. He'll tell you what's worth pulling out before the excavator arrives, and what to let go.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Very little goes into the new house. A new home is built to the current Building Code with new, graded, treated materials, and it carries the statutory warranties that come with new work. Old framing, old wiring, old plumbing and old roofing don't meet the standard and can't be certified as if they did.</p>
        <p>A fair bit can be reused <em>elsewhere</em>: hardwood floorboards, VJ boards, casement windows, doors, fretwork, stairs, a claw-foot bath, sometimes the roofing iron. Salvage yards want it and so do renovators. It can also come back into your new house as a feature &mdash; a bench top, a wall of old boards, a door &mdash; where it's decoration, not structure.</p>
        <p>Everything with asbestos in it is removed by a licensed contractor and disposed of; none of that is reused, ever. The rest is sorted for recycling where it can be.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#why-not">Why can't the old house go into the new one?</a></li>
          <li><a href="#worth-saving">What's worth saving?</a></li>
          <li><a href="#as-a-feature">What can come back as a feature?</a></li>
          <li><a href="#never">What's never reused?</a></li>
          <li><a href="#the-rest">What happens to the rest?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="why-not">Why can't the old house go into the new one?</h2>
      <p>Three reasons, and they're not about taste.</p>
      <ul class="pts">
        <li><strong>The code.</strong> A new house is certified against the Building Code of Australia: graded structural timber, termite management, wiring and plumbing to current standards, glazing and energy efficiency that a 1960s window doesn't meet. Old material can't be certified as new.</li>
        <li><strong>The warranty.</strong> New domestic building work in Queensland carries statutory warranties &mdash; six years for structural defects, one year for the rest &mdash; and the builder stands behind the materials. Nobody can warrant seventy-year-old bearers.</li>
        <li><strong>The labour.</strong> Pulling old material out carefully, de-nailing it, storing it and re-fitting it costs more in hours than the material is worth, most of the time. Where it isn't, it's usually the pieces below.</li>
      </ul>

      <blockquote class="proof">
        <p><b>Schedule 1B of the QBCC Act &ldquo;sets out statutory warranties which are deemed to be part of all regulated domestic building contracts, even if not stated in the contract.&rdquo;</b> Structural defects: six years. Other breaches: one year.</p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023. The builder warrants the new work. That's the reason the new work is new.</cite>
      </blockquote>

      <blockquote class="proof">
        <p><b>&ldquo;With a renovation you&rsquo;re trying to tie the old into the new, and nothing&rsquo;s ever perfect. People want it all brand new, and technically it&rsquo;s not. You make it as seamless as you can.&rdquo;</b></p>
        <cite>Nathan Brain, builder at Sabre, on camera, October 2026.</cite>
      </blockquote>

      <h2 class="h2" id="worth-saving">What's worth saving?</h2>
      <p>The things an old Bayside house is famous for.</p>
      <ul class="pts">
        <li><strong>Hardwood floorboards</strong> &mdash; wide, old-growth, and increasingly hard to buy new.</li>
        <li><strong>VJ (vertical joint) wall boards</strong> and tongue-and-groove lining.</li>
        <li><strong>Casement windows, French doors, fanlights, fretwork and balustrades</strong> from the pre-war houses.</li>
        <li><strong>Internal doors</strong>, especially solid timber ones with the old hardware.</li>
        <li><strong>Timber stairs</strong> and posts, where the timber is sound.</li>
        <li><strong>A cast-iron bath</strong>, a pedestal basin, brass tapware.</li>
        <li><strong>Roofing iron</strong>, sometimes, for sheds and fences.</li>
      </ul>
      <p>The condition is everything. Termite-damaged or rotten timber isn't worth the truck.</p>

      <h2 class="h2" id="as-a-feature">What can come back as a feature?</h2>
      <p>Anything that doesn't have to hold the house up or keep the weather out.</p>
      <p>Old floorboards become a bench top, a dining table, a feature wall or a set of shelves. A VJ wall becomes the lining of the new entry. A pair of casements becomes an internal window between the kitchen and the hall. A door becomes the door to the study. The old house numbers go on the new gate.</p>
      <p>It's a good way to keep the house in the house. It's done as joinery and decoration, planned with the designer, and it needs to come out before demolition, carefully, not be rescued from the skip.</p>

      <h2 class="h2" id="never">What's never reused?</h2>
      <ul class="pts">
        <li><strong>Anything containing asbestos.</strong> Fibro sheeting, eaves, vinyl floor tiles, some roofing, the bathroom linings. Licensed removal, wrapped, disposed of at a licensed facility. <a href="../what-asbestos-removal-means-for-a-knockdown-rebuild/">More here.</a></li>
        <li><strong>Wiring, switchboards, plumbing, hot water systems.</strong> Age, standards and safety.</li>
        <li><strong>Structural framing, bearers, joists, stumps.</strong> Can't be graded or certified as new.</li>
        <li><strong>Old insulation, plasterboard, carpet, most kitchens and bathrooms.</strong></li>
      </ul>

      <h2 class="h2" id="the-rest">What happens to the rest?</h2>
      <p>Demolition contractors sort. Concrete and brick go to crushing for road base. Steel and iron go to metal recycling. Clean timber goes to timber recycling or salvage. Asbestos goes to licensed disposal, separately and first. What can't be sorted goes to landfill. Ask the demolition contractor what their recovery rate is; the good ones know.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Almost nothing structural goes into the new house.</b> Code, warranty and labour all say no.</li>
          <li><b>Hardwood boards, VJs, casements, doors, stairs and the bath are worth saving.</b> Condition decides.</li>
          <li><b>Old material comes back as a feature,</b> not as structure: bench tops, walls, internal windows, doors.</li>
          <li><b>Asbestos is never reused,</b> and it leaves first, with a licensed contractor.</li>
          <li><b>Pull it out before demolition, on purpose.</b> Nothing worth keeping survives an excavator.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can we sell the salvage to offset the demolition?</p>
          <p>Sometimes. Salvage yards buy good hardwood, windows and fittings, and some demolition contractors price a job lower if they keep the salvage. Ask both. Don't expect it to change the number much; it's a tidy-up, not a rebate.</p>
        </div>
        <div>
          <p class="q">Can the old roofing iron go on the new house?</p>
          <p>No. New roofing has to meet the current standards for wind, fixing and corrosion, and it's warranted. Old iron makes good fencing and shed roofing.</p>
        </div>
        <div>
          <p class="q">Who takes the pieces out?</p>
          <p>A salvage-minded demolition contractor, or a carpenter before demolition, for anything you want to keep. Tell the builder early so it's in the sequence. Once the excavator starts, it's gone.</p>
        </div>
        <div>
          <p class="q">Is it greener to renovate than rebuild?</p>
          <p>Often, if the house is worth keeping &mdash; and that's a different question, answered <a href="../knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is/">here</a>. If it isn't, a sorted demolition and a well-insulated new house is the honest comparison.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <em>Consumer Building Guide</em> v3 (implied warranties, ss19&ndash;29 of Schedule 1B); Queensland Government, <em>asbestos.qld.gov.au</em> (removal and disposal); Building Code of Australia (National Construction Code) as applied to Class 1a buildings. Read 17 September 2026. Plain-English guidance from a builder, not legal advice.</p>
''')
