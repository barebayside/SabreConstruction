# Phase 5 of docs/reference/article-bank.md — finishing Spiral 1 without Nathan, part A: S1, S2, R4, R6, R11/R38, R18.
# Sources read 2026-09-17:
#   Brisbane City Council — "Building a new house: approvals and requirements" (code-assessable overlays list; Dwelling house code;
#     "All houses are Class 1a buildings under the Building Code of Australia and need building approval");
#     "Demolition or removal" (building approval via a licensed certifier; planning approval triggers; plumbing approval to cap the drain)
#   Brisbane City Council — "Protected vegetation" (Natural Assets Local Law 2003: four categories; permit; penalties; property enquiry report)
#   QBCC — Consumer Building Guide v3 (effective July 2023): contract price s2, cooling-off ss35-39, deposits ss33-34, variations ss40-41,
#     implied warranties ss19-29, cost-plus warning; "Contracts and agreement types" (reviewed 27 Jun 2025): cost-plus definition,
#     "50% to 100% greater than anticipated", Home Warranty non-completion not available; "Deposits and progress payments" (27 Jun 2025)
#   Standards Australia AS 2870 (Residential slabs and footings) — site classes A, S, M, H1, H2, E, P
# Rule 1: no prices, no bands, no timelines. The whole point of S1 is that nobody can give you the number without the block.

POSTS = {}

# ---------------------------------------------------------------- S1 · what decides the cost
POSTS["s1-what-decides-cost"] = dict(
    slug="what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane",
    section="rebuild",
    title="What decides the cost of a knockdown rebuild in Brisbane?",
    h1="What decides the cost of a<br>knockdown rebuild in Brisbane?",
    description="Not a price. The nine things that move it: the old house, what's in its walls, the block, the overlays, the ground, the size, the finish, the site access and where you live meanwhile. From a Bayside builder.",
    lede="Every calculator on the internet gives you a number for this, and every one of them is guessing, because none of them has stood on your block. Here is what actually moves the cost of a knockdown rebuild, in the order a builder thinks about it. No figures &mdash; the honest version doesn't have any until someone has walked your site.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane.jpg",
    image_alt="A builder's notebook on the bonnet of a ute in front of an old highset, the block and its slope behind",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real job.",
    label=("The nine things that move it", "What decides the cost"),
    card_title="What decides the cost of a knockdown rebuild in Brisbane?",
    card_blurb="Not a price. The nine things that move it: the old house and what's in it, the block, the overlays, the ground, the size, the finish, the access and where you live meanwhile.",
    about=["Knockdown rebuild cost", "Knockdown rebuild", "Brisbane Bayside"],
    related=["what-asbestos-removal-means-for-a-knockdown-rebuild", "rebuilding-on-a-flood-overlay-block-on-the-bayside", "what-is-a-knockdown-rebuild-package"],
    cta="The walk-through is where the number comes from. Nathan looks at the house, the block and the overlays, and tells you what each one does to the cost before anyone draws a line.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>The cost of a knockdown rebuild is decided by nine things, and only two of them are the ones people expect: the size of the new house and the level of finish. The other seven belong to the old house and the block, and they're the reason two families with the same floor plan end up with very different numbers.</p>
        <p>They are: what the old house is made of and what's in it (asbestos), how it comes down, the slope and access of the block, which council overlays apply (character, flood), what the soil test says, how the new house meets the ground, and where you live while it happens.</p>
        <p>Anyone who gives you a figure before they've checked those seven is quoting the house, not the job. We don't publish a price for the same reason we don't guess your floor level: the block decides it, and a walk-through takes an hour.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#why-no-number">Why won't anyone give a straight number?</a></li>
          <li><a href="#old-house">What does the old house add?</a></li>
          <li><a href="#the-block">What does the block decide?</a></li>
          <li><a href="#the-rules">What do the overlays and the ground do?</a></li>
          <li><a href="#new-house">What about the new house itself?</a></li>
          <li><a href="#meanwhile">What does living somewhere else cost the job?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="why-no-number">Why won't anyone give a straight number?</h2>
      <p>Because the honest ones can't yet, and the others are quoting something else.</p>
      <p>A &ldquo;from&rdquo; price is the price of a house on a flat, clear, dry lot with nothing in the way. Most Bayside blocks are not that. They have a seventy-year-old house on them, a slope toward the water, a tree council cares about, and a flood level in the FloodWise report.</p>
      <p>Each of those adds work that has to be done before the new house exists. That's why the same plan lands differently on different blocks, and why the quote you can trust is the one written after someone has stood on yours.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Allowances (items or services for which the price is not fixed when the contract is signed) should be kept to a minimum as the final cost often exceeds the estimate in the contract.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023. The regulator's own warning: a price with a lot of allowances in it isn't a price yet.</cite>
      </blockquote>

      <h2 class="h2" id="old-house">What does the old house add?</h2>
      <p>Three things, and the first is the one nobody budgets for.</p>
      <ul class="pts">
        <li><strong>What it's made of.</strong> Most Bayside houses from before 1990 have asbestos somewhere: fibro sheeting, eaves, the bathroom, the built-in-under. Licensed removal happens before demolition and is its own job with its own paperwork. <a href="../what-asbestos-removal-means-for-a-knockdown-rebuild/">What that involves is here.</a></li>
        <li><strong>How it comes down.</strong> A small post-war cottage on a clear block is a short job for a demolition contractor. A big highset wedged between two neighbours, with a pool and a slab underneath, is not.</li>
        <li><strong>What's under and around it.</strong> Old slabs, old footings, old sheds, buried rubbish, a septic tank from before the sewer came through. It all has to leave before anyone can dig.</li>
      </ul>

      <h2 class="h2" id="the-block">What does the block decide?</h2>
      <p>Two things above all: slope and access.</p>
      <p><strong>Slope</strong> decides how the house meets the ground. A flat block takes a slab. A block that falls toward the bay takes cut and fill, retaining, or a highset design, and each of those is real work. It's also why a flat-block package plan doesn't fit &mdash; <a href="../what-is-a-knockdown-rebuild-package/">that post is here</a>.</p>
      <p><strong>Access</strong> decides what machinery can get in and how materials arrive. A narrow frontage on a quiet Wynnum street with power lines down the front and a neighbour's fence a metre from the boundary changes how everything is delivered and lifted.</p>
      <p>Then the smaller ones: where the sewer and stormwater run, whether the block is a corner, where the street trees are, and what the neighbours have built to the boundary.</p>

      <h2 class="h2" id="the-rules">What do the overlays and the ground do?</h2>
      <p>Council's overlays don't usually stop a rebuild on the Bayside. They add design work and sometimes an application.</p>
      <ul class="pts">
        <li><strong>The character overlay.</strong> If the house was built in 1946 or earlier and the street is in the overlay, demolition needs a development application before anything else. <a href="../can-we-knock-down-our-house/">The rules are here.</a></li>
        <li><strong>The flood overlays.</strong> They set a minimum habitable floor level. That can push the design highset, which is a different house from a lowset one. <a href="../rebuilding-on-a-flood-overlay-block-on-the-bayside/">What that changes is here.</a></li>
        <li><strong>The soil test.</strong> A geotechnical report classifies your ground under the Australian Standard for residential slabs and footings. Sand and rock need simple footings. Reactive clay needs engineered ones. The letter on that report moves the price of everything below the floor.</li>
        <li><strong>Protected trees.</strong> A tree council protects under its local law stays, and the design works around it. That is not a small thing on a block with one big gum in the middle.</li>
      </ul>

      <h2 class="h2" id="new-house">What about the new house itself?</h2>
      <p>This is the part people expect, and it still matters: size, storeys, and finish.</p>
      <p>Size is the obvious one. But shape counts too &mdash; a long thin house has more wall for the same floor than a square one, and a two-storey house has a smaller, cheaper roof and slab for the same rooms than a sprawling single storey.</p>
      <p>Finish is where the widest range lives. The same room can be fitted out plainly or expensively, and the difference is entirely the family's choice. That's the one lever you control completely, and the one we'd rather you spend your decisions on than on things the block has already decided.</p>

      <h2 class="h2" id="meanwhile">What does living somewhere else cost the job?</h2>
      <p>It isn't in the contract, and it's part of the cost. During a knockdown rebuild the family lives somewhere else, and rent or a relative's spare room for the length of the build belongs in the budget beside the house. The length of that build is a question for the builder you choose, in writing, with a date for practical completion in the contract. Ask for it.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Nine things move the cost, and seven belong to the old house and the block,</b> not the new house.</li>
          <li><b>Asbestos, slope, access and the soil test</b> are the four that surprise people most.</li>
          <li><b>Overlays usually change the design, not whether you can build.</b> Check character and flood first.</li>
          <li><b>Finish is the one lever you fully control.</b> Spend your decisions there.</li>
          <li><b>A price with allowances in it isn't a price yet</b> &mdash; the QBCC's words, not ours.</li>
          <li><b>The number comes from the block.</b> Nobody honest has it before they've stood on it.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Why won't Sabre put a starting price on the website?</p>
          <p>Because we'd be quoting a flat, clear lot, and we don't build on many of those. A number that changes the moment we see your block isn't useful to you, and we'd rather be the builder who told you what moves it.</p>
        </div>
        <div>
          <p class="q">Is a two-storey house always dearer than a single storey?</p>
          <p>Not for the same rooms. A two-storey house sits on a smaller slab under a smaller roof, and on a sloping or small block it's often the sensible shape. What costs more is the extra floor area, not the extra floor.</p>
        </div>
        <div>
          <p class="q">What should we have ready before we ask for a quote?</p>
          <p>The year the house was built, council's FloodWise report on the lot, and a rough idea of the rooms you need. Everything else Nathan reads off the block at the walk-through.</p>
        </div>
        <div>
          <p class="q">Will the quote have allowances in it?</p>
          <p>Some items can't be fixed until they're chosen or checked &mdash; that's what an allowance is for. The QBCC's guidance is to keep them to a minimum. Ask any builder to point to each one and say why it's there.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023); Brisbane City Council, <em>Building a new house: approvals and requirements</em> and <em>Protected vegetation</em>; Standards Australia AS 2870 <em>Residential slabs and footings</em>. Read 17 September 2026. This is a plain-English guide, not a quote, and not financial advice.</p>
''')

# ---------------------------------------------------------------- S2 · rebuild or renovate
POSTS["s2-rebuild-or-renovate"] = dict(
    slug="knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is",
    section="rebuild",
    title="Knockdown rebuild or renovate: how to tell which one your house is",
    h1="Knockdown rebuild or renovate:<br>how to tell which one your house is.",
    description="The six checks a builder runs on an old Bayside house before saying keep it or start again: the bones, the year, what you want it to become, the block, the ground and the money you'd spend either way.",
    lede="Some houses want a renovation. Some want to be replaced. Most families ask us this question already leaning one way, and the honest answer sometimes sends them the other. Here are the six checks we run before we say either word.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is.jpg",
    image_alt="Two Bayside houses side by side: one lifted and being renovated, one cleared to the slab for a rebuild",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of real jobs.",
    label=("The six checks", "Rebuild or renovate?"),
    card_title="Knockdown rebuild or renovate: how to tell which one your house is",
    card_blurb="The six checks a builder runs on an old Bayside house before saying keep it or start again. Sometimes the honest answer is the one you didn't want.",
    about=["Knockdown rebuild vs renovation", "Renovating a Queenslander", "Brisbane Bayside"],
    related=["what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane", "what-are-bayside-houses-made-of", "can-we-knock-down-our-house"],
    cta="This is the exact question the walk-through answers. Nathan goes through the house room by room and tells you which one it is, and why.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Renovate when the bones are good, the house can become what you need without fighting it, and the rules or the street give you a reason to keep it. Rebuild when the bones are tired, the plan can only get there by replacing most of the house anyway, or the block wants a different house from the one that's on it.</p>
        <p>The six checks: the structure, the year it was built, what you want it to become, the block, the ground under it, and what the two paths would each cost you &mdash; not just in money, but in the house you end up with.</p>
        <p>A pre-1947 house in the character overlay can tip the answer toward renovating on its own, because council may not let it come down. A post-war lowset with a cracked slab and rooms too small for the family usually tips the other way.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#the-bones">Check one: what are the bones like?</a></li>
          <li><a href="#the-year">Check two: what year was it built?</a></li>
          <li><a href="#the-brief">Check three: what do you need it to become?</a></li>
          <li><a href="#the-block">Check four: what does the block want?</a></li>
          <li><a href="#the-ground">Check five: what's under it?</a></li>
          <li><a href="#the-money">Check six: what does each path really cost?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="the-bones">Check one: what are the bones like?</h2>
      <p>Start with what holds the house up.</p>
      <p>A hardwood-framed Queenslander on sound stumps, with a straight roofline and dry subfloor, has bones worth keeping. Termite damage, rotten bearers, a roof that has sagged, stumps that have moved, or a slab that has cracked and lifted are a different story.</p>
      <p>A builder can tell most of this from under the house and in the roof space in under an hour. If the frame is going, you're not renovating, you're rebuilding in stages and paying twice.</p>

      <h2 class="h2" id="the-year">Check two: what year was it built?</h2>
      <p>The year decides two things at once.</p>
      <ul class="pts">
        <li><strong>Whether council will let it come down.</strong> A house built in 1946 or earlier, in a street inside Brisbane's traditional building character overlay, needs a development application to demolish and council may say no. <a href="../can-we-knock-down-our-house/">The rules are here</a>, and <a href="../check-if-your-street-is-in-the-character-overlay/">how to check your street is here</a>.</li>
        <li><strong>What's in the walls.</strong> Anything before 1990 probably has asbestos somewhere, and both paths have to deal with it &mdash; a renovation that disturbs it, or a demolition that removes it.</li>
      </ul>

      <h2 class="h2" id="the-brief">Check three: what do you need it to become?</h2>
      <p>This is the check families skip, and it's the one that decides most cases.</p>
      <p>Write down what the house has to do in ten years. Bedrooms, a second living area, a bathroom the kids can use without going through your room, somewhere for a parent to stay. Then hold that against the plan you've got.</p>
      <p>If the old house can get there by opening a wall and adding a room, renovate. If getting there means moving the kitchen, lifting the house, building in underneath, replacing the roof and rewiring the lot, you've described a new house with an old one in the way.</p>

      <h2 class="h2" id="the-block">Check four: what does the block want?</h2>
      <p>Old houses were put where they were put. The block might want something else.</p>
      <p>A house sitting at the front of a deep block, facing the wrong way for the sun and the breeze off the bay, with the backyard nobody uses, is a common Bayside shape. A renovation keeps that arrangement. A rebuild can turn the house around. On a sloping block, a rebuild can also put the living areas where the view is instead of where the 1960s put them.</p>

      <h2 class="h2" id="the-ground">Check five: what's under it?</h2>
      <p>Two things: the flood level and the soil.</p>
      <p>If council's FloodWise report puts a minimum habitable floor level above your current floor, a renovation that keeps the floor where it is keeps the problem. A new house is designed to the level from the start. <a href="../rebuilding-on-a-flood-overlay-block-on-the-bayside/">What that changes is here.</a></p>
      <p>And if you're going to add weight to an old house &mdash; a second storey, a slab under it &mdash; the ground has to carry it. A soil test tells you whether it can, and what the footings need to be. On a house that's already moved, that answer can settle the question.</p>

      <h2 class="h2" id="the-money">Check six: what does each path really cost?</h2>
      <p>Not the number &mdash; nobody has that yet. The shape.</p>
      <ul class="pts">
        <li><strong>A renovation is priced on what you find.</strong> Every old wall opened is a small unknown, and the QBCC's guidance on allowances applies: the more of the price that's an estimate, the less of a price it is.</li>
        <li><strong>A rebuild is priced on the block.</strong> Once the old house is gone and the soil test is in, most of the unknowns are gone with it.</li>
        <li><strong>Both paths mean living somewhere else</strong> for part of the time. A big renovation is rarely done around a family.</li>
        <li><strong>The house you end up with is different.</strong> A renovated house is a better old house. A rebuilt one is a new house, with new footings, new wiring, new plumbing, and the statutory warranties that come with new work.</li>
      </ul>

      <blockquote class="proof">
        <p><b>Schedule 1B of the QBCC Act &ldquo;sets out statutory warranties which are deemed to be part of all regulated domestic building contracts, even if not stated in the contract. The warranty period is 6 years from completion, termination or cessation of the work for breaches resulting in structural defects; 1 year for all other breaches.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023. That applies to the new work either way &mdash; but on a rebuild, all of the house is new work.</cite>
      </blockquote>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Six checks: bones, year, brief, block, ground, money.</b> Run all six before you decide.</li>
          <li><b>Good bones and a pre-1947 date in the overlay lean toward renovating.</b> Council may decide that for you.</li>
          <li><b>If the brief means replacing most of the house, it's a rebuild</b> with an old house in the way.</li>
          <li><b>The block and the flood level can want a different house</b> from the one that's on it.</li>
          <li><b>A renovation is priced on what you find; a rebuild on the block.</b> That's the difference in the two quotes.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Will a builder who does rebuilds always say rebuild?</p>
          <p>Some will. The walk-through is free precisely so the answer can be honest, whichever way it goes &mdash; and a builder who only ever says rebuild is telling you something about the builder, not the house.</p>
        </div>
        <div>
          <p class="q">Can we renovate a pre-1947 house in the character overlay?</p>
          <p>Usually yes, and often that's the path the overlay is steering you toward. Work that changes the front or the character elements may need council's approval; work at the back and underneath is generally easier. A designer who knows the overlay code will tell you which is which.</p>
        </div>
        <div>
          <p class="q">What about raising the house and building in underneath?</p>
          <p>It's a real option on a highset with good bones and a level block, and a lot of Bayside houses have had it done. It's still a major job with a soil test, engineering and a period living elsewhere. Run the same six checks on it.</p>
        </div>
        <div>
          <p class="q">How fast can we get an answer?</p>
          <p>One walk-through. Nathan goes under the house, into the roof and around the block, and you'll have his honest view before he leaves.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023); Brisbane City Council, <em>Demolition or removal</em> and <em>Traditional building character overlay</em>, Brisbane City Plan 2014; <em>FloodWise Property Reports</em>. Read 17 September 2026. Plain-English guidance from a builder, not structural, planning or financial advice.</p>
''')

# ---------------------------------------------------------------- R4 · development application
POSTS["r4-da"] = dict(
    slug="does-a-knockdown-rebuild-need-a-development-application",
    section="rules",
    title="Does a knockdown rebuild need a development application in Brisbane?",
    h1="Does a knockdown rebuild need a<br>development application in Brisbane?",
    description="Two approvals, not one. Every new house needs building approval from a certifier. Planning approval (a DA) is only needed when an overlay or the old house triggers it. Council's own list, in plain words.",
    lede="People hear &ldquo;DA&rdquo; and picture a year of council. On most Bayside blocks it doesn't work like that. There are two different approvals, one you always need and one you sometimes need, and council publishes exactly what tips you into the second. Here it is, in plain words.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/does-a-knockdown-rebuild-need-a-development-application.jpg",
    image_alt="A rolled set of house plans and a council notice on the verandah rail of an old Queenslander",
    image_caption="Illustration in the style of Sabre's story frames.",
    label=("Two approvals, not one", "Do we need a DA?"),
    card_title="Does a knockdown rebuild need a development application?",
    card_blurb="Two approvals, not one. Every new house needs a certifier's building approval. A DA is only needed when an overlay or the old house triggers it &mdash; council's own list, in plain words.",
    about=["Development application", "Building approval", "Brisbane City Plan 2014", "Knockdown rebuild"],
    related=["can-we-knock-down-our-house", "rebuilding-on-a-flood-overlay-block-on-the-bayside", "check-if-your-street-is-in-the-character-overlay"],
    cta="Nathan checks the overlays on your lot at the walk-through and tells you which approvals your rebuild will need before anything is drawn.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Every knockdown rebuild needs <strong>building approval</strong>. Council says it plainly: all houses are Class 1a buildings under the Building Code of Australia and need building approval, which a licensed building certifier issues from scaled plans. The demolition needs its own building approval too.</p>
        <p>A <strong>development application</strong> (planning approval from council) is only needed if something on your lot triggers it. For a new house that's a code-assessable overlay: flood, traditional building character, pre-1911, heritage, significant landscape tree, waterway corridor, coastal hazard and a few others. For the demolition it's the old house: a pre-1947 house in the character overlay, or a heritage place, needs a DA to come down.</p>
        <p>So the question isn't &ldquo;do we need a DA?&rdquo; It's &ldquo;which overlays are on our lot, and how old is the house?&rdquo; Both are on council's map, and both take minutes to check.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#two-approvals">What are the two approvals?</a></li>
          <li><a href="#new-house">When does the new house need planning approval?</a></li>
          <li><a href="#demolition">When does the demolition need planning approval?</a></li>
          <li><a href="#accepted">What is &ldquo;accepted development&rdquo;?</a></li>
          <li><a href="#who-does-it">Who does all this?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="two-approvals">What are the two approvals?</h2>
      <p>They come from different people and answer different questions.</p>
      <ul class="pts">
        <li><strong>Building approval</strong> asks: is this building safe and built to the code? A private building certifier, licensed by the QBCC, checks the plans against the Building Code of Australia and the Queensland Development Code, issues the approval, inspects at the mandatory stages and signs off at the end. You always need it. So does the demolition.</li>
        <li><strong>Planning approval</strong> asks: is this the right thing for this piece of land under Brisbane City Plan 2014? It comes from council, through a development application. You need it only when City Plan says a house on your lot is code assessable rather than accepted.</li>
      </ul>

      <blockquote class="proof">
        <p><b>&ldquo;All houses are Class 1a buildings under the Building Code of Australia and need building approval.&rdquo;</b> Council directs you to contact a licensed building certifier and provide scaled, detailed plans from a draftsperson or architect.</p>
        <cite>Brisbane City Council, <em>Building a new house: approvals and requirements</em>. Building approval is not optional and it is not the DA.</cite>
      </blockquote>

      <h2 class="h2" id="new-house">When does the new house need planning approval?</h2>
      <p>When a code-assessable overlay covers the lot. Council lists them. The ones that turn up on the Bayside:</p>
      <ul class="pts">
        <li><strong>Flood overlay</strong> &mdash; common one street back from the bay and along the creeks.</li>
        <li><strong>Traditional building character overlay</strong> and the <strong>pre-1911 overlay</strong> &mdash; the older streets of Wynnum and Manly.</li>
        <li><strong>Coastal hazard overlay</strong> &mdash; the esplanade side.</li>
        <li><strong>Waterway corridors</strong> and <strong>wetlands</strong> &mdash; Lota Creek, the Wynnum creeks, the Ransome and Tingalpa edges.</li>
        <li><strong>Significant landscape tree overlay</strong> &mdash; a block with a mapped tree on it.</li>
        <li><strong>Heritage overlay</strong> &mdash; rare, but real.</li>
      </ul>
      <p>Council's full list also includes airport environs, biodiversity, bushfire, landslide and commercial character. If none apply and the house meets the Dwelling house code, no DA is needed for the house.</p>

      <h2 class="h2" id="demolition">When does the demolition need planning approval?</h2>
      <p>Council's demolition page is specific. Planning approval is needed if the site is on the Queensland Heritage Register, is a local heritage place, is in the pre-1911 overlay, is in the traditional building character overlay and the whole building was built before 1947, or is in certain zones and neighbourhood plans.</p>
      <p>Outside those, demolition of a house still needs building approval from a certifier, and a plumbing approval if the sewer drain has to be capped on the property. Council also says you don't need planning approval to demolish a free-standing outbuilding built after 1946.</p>
      <p>The pre-1947 case is the one that matters on the Bayside, and it's the one <a href="../can-we-knock-down-our-house/">this post walks through</a>.</p>

      <h2 class="h2" id="accepted">What is &ldquo;accepted development&rdquo;?</h2>
      <p>It's council's term for work that doesn't need a planning application, provided it meets the relevant code. For a house that means the Dwelling house code &mdash; or, on a lot under 450 square metres, the Dwelling house (small lot) code &mdash; and any other code that applies.</p>
      <p>The designer self-assesses against the code: height, setbacks, site cover, car parking, the way the house addresses the street. If it complies, it's accepted, and the certifier can approve it. If it doesn't, you're back to a DA, which is often why a design on a tricky block is adjusted rather than lodged.</p>

      <h2 class="h2" id="who-does-it">Who does all this?</h2>
      <p>Not you, mostly. The designer draws to the codes and flags the overlays. The certifier issues the building approvals and does the inspections. If a DA is needed, the designer or a town planner prepares and lodges it. The builder coordinates the lot and reads the conditions before pricing.</p>
      <p>What you do is find out early. Council's City Plan online tool shows every overlay on your lot by address, and the year the house was built is in council's archives. Between them they tell you which path you're on before you've spent anything.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Two approvals.</b> Building approval from a certifier, always. Planning approval from council, only if triggered.</li>
          <li><b>For the new house, overlays trigger the DA:</b> flood, character, pre-1911, coastal, waterway, tree, heritage.</li>
          <li><b>For the demolition, the old house triggers it:</b> pre-1947 in the character overlay, or heritage.</li>
          <li><b>&ldquo;Accepted development&rdquo; means it meets the Dwelling house code</b> and needs no DA.</li>
          <li><b>Check the overlays and the year first.</b> Both are online, both take minutes.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Does a flood overlay always mean a DA?</p>
          <p>Council lists the flood overlay among the code-assessable overlays for a new house, so a lot under it generally goes through a development application. The design shows it meets the flood planning requirements, and the FloodWise report gives the levels. It is paperwork, not a fight.</p>
        </div>
        <div>
          <p class="q">Can the certifier just approve everything?</p>
          <p>Only the building side. A certifier can't grant planning approval, and can't approve a building that needs a DA it doesn't have. What a certifier can do is seek relaxations of some Queensland Development Code or City Plan requirements through a referral to council.</p>
        </div>
        <div>
          <p class="q">Who lodges the DA?</p>
          <p>Usually the designer or a town planner on your behalf. The builder isn't normally the applicant, but a good one reads every condition on the approval before the price is finalised.</p>
        </div>
        <div>
          <p class="q">Do we need a DA to demolish a 1960s house?</p>
          <p>Not for its age. A post-1946 house outside the heritage overlays needs a certifier's building approval to come down, not a planning approval. Other overlays on the lot still apply to what you build next.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <a href="https://www.brisbane.qld.gov.au/building-and-planning/getting-started-on-your-project/residential-projects/new-house" rel="noopener">Building a new house: approvals and requirements</a> and <a href="https://www.brisbane.qld.gov.au/building-and-planning/getting-started-on-your-project/residential-projects/demolition-or-removal" rel="noopener">Demolition or removal</a>; Brisbane City Plan 2014, Dwelling house code and Dwelling house (small lot) code. Read 17 September 2026. The overlays and codes change; check City Plan online for your lot. This is a plain-English guide, not planning advice.</p>
''')

# ---------------------------------------------------------------- R6 · trees
POSTS["r6-trees"] = dict(
    slug="what-happens-to-the-trees-on-the-block-in-a-knockdown-rebuild",
    section="rules",
    title="What happens to the trees on the block in a knockdown rebuild?",
    h1="What happens to the trees on the<br>block in a knockdown rebuild?",
    description="Brisbane protects trees on private land under its Natural Assets Local Law, and it's an offence to touch a protected one without a permit. How to find out which of yours are protected, and what a builder does about it.",
    lede="The big gum in the backyard is either the best thing about your block or the reason the design has to bend. In Brisbane, that isn't always your call. Here's how council protects trees on private land, how to check yours in a few minutes, and what it does to a rebuild.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/what-happens-to-the-trees-on-the-block-in-a-knockdown-rebuild.jpg",
    image_alt="A cleared Bayside block with one huge gum tree fenced off and kept, a new slab poured around it",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real job.",
    label=("Council's local law", "The trees"),
    card_title="What happens to the trees on the block in a knockdown rebuild?",
    card_blurb="Brisbane protects trees on private land under its Natural Assets Local Law. How to check which of yours are protected, and what a builder does about it.",
    about=["Natural Assets Local Law", "Protected vegetation", "Knockdown rebuild", "Brisbane"],
    related=["does-a-knockdown-rebuild-need-a-development-application", "what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane", "wakerley-and-gumdale-the-newer-bayside"],
    cta="Bring council's protected vegetation report to the walk-through, or let Nathan pull it. He'll tell you what the tree does to the design before anyone's attached to a plan.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Some of the trees on your block may be protected, and if they are, they stay unless council issues a permit. Brisbane City Council's Natural Assets Local Law 2003 protects four kinds of vegetation: council's own (street trees, parks), vegetation along waterways and wetlands, significant urban vegetation (mature or prominent trees on private land, native or not), and significant native vegetation on mapped properties.</p>
        <p>Council's words: penalties apply if you interfere with protected vegetation without a permit. That includes lopping, not just felling, and it applies on your own land.</p>
        <p>You can ask council for a protected vegetation report on your property and get a map back. A builder designs around what it shows. On the Bayside, with its creeks, mangroves and old street trees, that report is worth reading before a plan is drawn.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-is-protected">Which trees are protected?</a></li>
          <li><a href="#how-to-check">How do you check your block?</a></li>
          <li><a href="#permit">What if a protected tree is where the house goes?</a></li>
          <li><a href="#unprotected">What about the trees that aren't protected?</a></li>
          <li><a href="#the-build">What does a builder do with a kept tree?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-is-protected">Which trees are protected?</h2>
      <p>Council's local law names four categories, and two of them sit on private land.</p>
      <ul class="pts">
        <li><strong>Council vegetation.</strong> Street trees, park trees, vegetation in natural areas. The tree on the verge in front of your house is council's, not yours.</li>
        <li><strong>Waterway and wetland vegetation.</strong> Along the creeks and the foreshore, fresh or salt, natural or man-made. Lota Creek, the Wynnum creeks and the mangrove edges all count.</li>
        <li><strong>Significant urban vegetation.</strong> Council's words: native and exotic vegetation on private property that is mature and/or prominent in the landscape. The big fig, the old camphor laurel, the gum everyone can see from the street.</li>
        <li><strong>Significant native vegetation.</strong> All native vegetation on properties in council's mapping, from ground covers to large trees.</li>
      </ul>
      <p>Council also lets residents nominate a tree or a group of trees for a vegetation protection order. Old Bayside streets have a few.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Penalties apply if you interfere with protected vegetation without a permit.&rdquo;</b> A property may have protections if it is near or in a waterway corridor, in a bushland area, contains large significant trees even in an urban area, or has heritage values.</p>
        <cite>Brisbane City Council, <em>Protected vegetation</em> (Natural Assets Local Law 2003). It's the owner's job to know, and the map is free.</cite>
      </blockquote>

      <h2 class="h2" id="how-to-check">How do you check your block?</h2>
      <p>Two ways, both from council.</p>
      <ol>
        <li>Open council's <strong>community maps</strong> (the land and environmental map) and look up your address. The protected vegetation layers show on the lot.</li>
        <li>Make a <strong>protected vegetation enquiry</strong> about your property. Council sends back a map of protected vegetation on the lot and a report as a PDF.</li>
      </ol>
      <p>Do the second one. The report is what a designer and a certifier want to see, and it's what you'd need to apply for a permit anyway.</p>

      <h2 class="h2" id="permit">What if a protected tree is where the house goes?</h2>
      <p>Then you apply to council for a permit, and the design might change first.</p>
      <p>Council's guidance is to talk to them about your plans before lodging a development application, and to apply for the vegetation permit after the DA is finalised. In practice that means the tree is part of the design conversation from the start, not a surprise at demolition. A permit isn't automatic. Council can refuse, or condition it, or ask for the design to move.</p>
      <p>There's also the City Plan side: a lot under the <strong>significant landscape tree overlay</strong> is code assessable, which means a new house needs a development application. <a href="../does-a-knockdown-rebuild-need-a-development-application/">That post explains the two approvals.</a></p>

      <h2 class="h2" id="unprotected">What about the trees that aren't protected?</h2>
      <p>Most trees on most suburban blocks aren't in any of the four categories, and those are yours to keep or remove. Check the report before you assume, and check the verge: the street tree is council's even when it's your problem.</p>
      <p>Removal before demolition is a job for an arborist or the demolition contractor, and the stumps and roots come out before anyone digs footings.</p>

      <h2 class="h2" id="the-build">What does a builder do with a kept tree?</h2>
      <p>Designs around it, then protects it.</p>
      <p>A big tree decides where the house can sit, where the driveway goes, and what the footings near it have to do. Roots don't stop at the drip line. The arborist's advice about the protection zone becomes part of the site plan, the tree gets fenced before the excavator arrives, and nothing is stored or parked under it for the length of the job.</p>
      <p>It's more work. It's also usually why the block was worth staying on.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Brisbane protects trees on private land</b> under the Natural Assets Local Law 2003 &mdash; mature or prominent ones, native or not, plus waterway and mapped native vegetation.</li>
          <li><b>It's an offence to touch a protected tree without a permit,</b> including lopping.</li>
          <li><b>Ask council for a protected vegetation report on your lot.</b> It comes back as a map and a PDF.</li>
          <li><b>Talk to council before the DA, apply for the permit after it.</b> Council's own order.</li>
          <li><b>A kept tree shapes the design and gets fenced on site.</b> That's the builder's job.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can we remove a tree on the footpath that's in the way of the driveway?</p>
          <p>Not without council. Street trees are council vegetation under the local law. Talk to council about the crossover and the tree together; sometimes the driveway moves instead.</p>
        </div>
        <div>
          <p class="q">The tree is dangerous. Do we still need a permit?</p>
          <p>Ask council before you act. There are processes for dangerous or dead trees, and an arborist's report is usually the first step. Cutting first and explaining later is exactly what the penalties are for.</p>
        </div>
        <div>
          <p class="q">Does a protected tree stop the rebuild?</p>
          <p>Rarely. It moves the house, the driveway or the footings. Houses get built around big trees all over the Bayside, and often the tree is the reason the family stayed.</p>
        </div>
        <div>
          <p class="q">Who fences the tree during the build?</p>
          <p>The builder, before demolition starts, to the protection zone an arborist sets. It stays fenced until handover.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <a href="https://www.brisbane.qld.gov.au/building-and-planning/supporting-documents-and-online-tools/protected-vegetation" rel="noopener">Protected vegetation</a> and <em>Protected vegetation permits</em> (Natural Assets Local Law 2003); Brisbane City Plan 2014, Significant landscape tree overlay. Read 17 September 2026. Council's mapping is updated from time to time; get the current report for your lot. This is a plain-English guide, not legal or arboricultural advice.</p>
''')

# ---------------------------------------------------------------- R11 / R38 · fixed price or cost-plus
POSTS["r11-fixed-or-cost-plus"] = dict(
    slug="fixed-price-or-cost-plus-what-do-builders-mean",
    section="builder",
    title="Fixed price or cost-plus: what do builders mean, and which protects you?",
    h1="Fixed price or cost-plus:<br>what do builders mean, and which protects you?",
    description="The two ways a building contract can set the price, in the QBCC's own words. What each one shifts onto you, why the regulator warns about cost-plus, and what to check before signing either.",
    lede="Two builders can quote the same house and mean completely different things by the number. One has fixed it. One has estimated it and will bill you what it costs, plus a margin. Queensland's regulator has strong words about the second. Here's what each contract actually does, and what to ask.",
    date="2026-09-17", category="Dealing with a builder", image="blog/fixed-price-or-cost-plus-what-do-builders-mean.jpg",
    image_alt="Two building contracts side by side on a kitchen table, a pen resting on one",
    image_caption="Illustration.",
    label=("The QBCC's own words", "Fixed price or cost-plus"),
    card_title="Fixed price or cost-plus: what do builders mean, and which protects you?",
    card_blurb="The two ways a contract can set the price, in the regulator's own words. What each shifts onto you, why the QBCC warns about cost-plus, and what to check before you sign.",
    about=["Fixed price contract", "Cost plus contract", "QBCC", "Building contracts Queensland"],
    related=["what-is-the-qbcc-and-what-to-check-on-a-builders-licence", "what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane", "who-are-the-small-independent-builders-on-brisbanes-bayside"],
    cta="Ask Nathan which contract Sabre uses and why, and bring the other builder's contract if you have one. He'll walk you through both.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>A <strong>fixed price</strong> (lump sum) contract states the contract price up front. For contracts of $20,000 or more, the QBCC requires that price to be shown prominently on the first page of the contract schedule. The builder carries the risk of getting it wrong, within the limits of the variations and allowances written into the contract.</p>
        <p>A <strong>cost-plus</strong> contract is one where, in the QBCC's words, the amount the builder is to receive cannot be accurately calculated when the contract is entered into. You pay what the job costs plus the builder's margin. You carry the risk.</p>
        <p>The regulator's view is not neutral. The QBCC strongly recommends legal advice before signing a cost-plus or construction management contract, says they increase your legal risk and reduce your Home Warranty Scheme protection, and reports that final costs under cost-plus are often considerably higher &mdash; 50% to 100% greater than anticipated. Protection for non-completion under the Queensland Home Warranty Scheme isn't available on a cost-plus contract at all.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#fixed">What is a fixed price contract, really?</a></li>
          <li><a href="#cost-plus">What is a cost-plus contract?</a></li>
          <li><a href="#the-warning">What does the QBCC say about cost-plus?</a></li>
          <li><a href="#allowances">Where does a fixed price stop being fixed?</a></li>
          <li><a href="#what-to-ask">What should you check before signing either?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="fixed">What is a fixed price contract, really?</h2>
      <p>It's the standard Queensland domestic building contract, level 2 for work of $20,000 or more, with a price on the front page.</p>
      <p>The price can only move in ways the contract names: a variation you agree to in writing, an allowance that comes in above or below its estimate, or a provisional sum for work that couldn't be priced yet. Everything else is the builder's problem. If the framing timber goes up, that's on them.</p>
      <p>That's the protection. It's also why a careful builder spends time on the block and the soil test before signing one: the more they know, the fewer allowances they need.</p>

      <h2 class="h2" id="cost-plus">What is a cost-plus contract?</h2>
      <p>The builder charges the actual cost of labour, materials and subcontractors, plus a percentage or a fee. There's no fixed total. There's an estimate, and the estimate isn't a promise.</p>
      <p>Cost-plus exists for jobs that genuinely can't be priced: a heritage restoration where nobody knows what's behind the walls, or work that has to start before the design is finished. For a new house on a cleared block, where the design is done and the ground is tested, there's much less reason for it.</p>

      <h2 class="h2" id="the-warning">What does the QBCC say about cost-plus?</h2>
      <p>This much, on its own pages:</p>

      <blockquote class="proof">
        <p><b>&ldquo;QBCC strongly recommends home owners obtain formal legal advice before signing either of these types of contracts which increase your legal risk, reduce your Home Warranty Scheme protection and often result in disputes and cost overruns.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023, on cost-plus and construction management contracts.</cite>
      </blockquote>

      <blockquote class="proof">
        <p><b>Cost-plus contracts carry a lack of price certainty, a high incidence of serious disputes, and a disincentive for the contractor to minimise costs because payment is proportionate to them. The QBCC says reports show final costs &ldquo;often considerably higher at 50% to 100% greater than anticipated,&rdquo; and that protection for non-completion under the Queensland Home Warranty Scheme is not available.</b></p>
        <cite>Queensland Building and Construction Commission, <em>Contracts and agreement types</em>, reviewed 27 June 2025. The regulator's summary, not ours.</cite>
      </blockquote>

      <p>That last point is the one to hold onto. If a builder on a cost-plus contract can't finish, the scheme that would otherwise help you complete the house doesn't apply to that contract.</p>

      <h2 class="h2" id="allowances">Where does a fixed price stop being fixed?</h2>
      <p>At the allowances, and it pays to count them.</p>
      <p>An allowance is an item the price can't fix yet because you haven't chosen it or nobody's checked it: tiles, tapware, sometimes the site works. The QBCC's guide says allowances should be kept to a minimum because the final cost often exceeds the estimate. A fixed price with a long list of allowances behaves a lot like a cost-plus contract for those items.</p>
      <p>Ask for each allowance to be pointed at, and ask why it's there. A builder who has done the soil test and walked the block should have very few on the site side.</p>

      <h2 class="h2" id="what-to-ask">What should you check before signing either?</h2>
      <ul class="pts">
        <li><strong>The contract type</strong>, in words, on the front. Fixed price, cost-plus or construction management.</li>
        <li><strong>The price and its allowances.</strong> The QBCC checklist asks you to check what proportion of the total is allowances.</li>
        <li><strong>The deposit.</strong> For a contract of $20,000 or more the maximum before work starts on site is 5%, with an exception up to 20% where more than half the work is done off site.</li>
        <li><strong>The start and practical completion dates</strong>, and how the completion date moves.</li>
        <li><strong>The Consumer Building Guide.</strong> The builder must give it to you before you sign a contract at or over $20,000. If you haven't got it, don't sign.</li>
        <li><strong>The cooling-off period.</strong> Five business days after you receive the signed contract and the guide, with a small cost to withdraw.</li>
        <li><strong>The licence.</strong> Search it on the QBCC's register before anything else. <a href="../what-is-the-qbcc-and-what-to-check-on-a-builders-licence/">How is here.</a></li>
      </ul>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Fixed price puts the risk on the builder. Cost-plus puts it on you.</b> That's the whole difference.</li>
          <li><b>The QBCC warns against cost-plus in plain terms</b> and reports final costs 50% to 100% above expectations.</li>
          <li><b>Home Warranty non-completion cover doesn't apply to cost-plus.</b> If the builder can't finish, you're on your own.</li>
          <li><b>A fixed price is only as fixed as its allowances.</b> Count them.</li>
          <li><b>Guide, deposit limit, dates, cooling-off, licence.</b> Five checks before you sign anything.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Is cost-plus ever the right choice?</p>
          <p>For work that genuinely can't be scoped before it starts, sometimes. For a new house on a cleared, tested block, it's hard to see why the risk should sit with the family. Get legal advice before you sign one; the regulator says so.</p>
        </div>
        <div>
          <p class="q">Can a fixed price still go up?</p>
          <p>Only by the routes in the contract: a variation you agree to in writing before the work starts, an allowance that comes in higher, or a provisional sum. Anything else is the builder's cost.</p>
        </div>
        <div>
          <p class="q">What's a construction management contract?</p>
          <p>You engage a licensed builder to manage the job, but you may also have to engage the trades directly and you're ultimately responsible for their performance. The QBCC groups it with cost-plus in its warning, and the same Home Warranty non-completion exclusion applies.</p>
        </div>
        <div>
          <p class="q">Which does Sabre use?</p>
          <p>Ask Nathan at the walk-through. He'll show you the contract and explain every allowance in it before you're asked to sign anything.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023); <a href="https://www.qbcc.qld.gov.au/home-owner-hub/build-renovate/contracts-payments/contracts-agreement-types" rel="noopener">Contracts and agreement types</a> and <a href="https://www.qbcc.qld.gov.au/home-owner-hub/build-renovate/contracts-payments/deposits-progress-payments" rel="noopener">Deposits and progress payments</a> (both reviewed 27 June 2025); Schedule 1B, <em>Queensland Building and Construction Commission Act 1991</em>. Read 17 September 2026. Thresholds and rules change; check the QBCC's current pages. This is a plain-English guide, not legal advice.</p>
''')

# ---------------------------------------------------------------- R18 · soil test
POSTS["r18-soil-test"] = dict(
    slug="what-is-a-soil-test-and-why-does-it-change-the-price",
    section="rebuild",
    title="What is a soil test, and why does it change the price of a new house?",
    h1="What is a soil test, and why does<br>it change the price of a new house?",
    description="A geotechnical report classifies your ground under the Australian Standard for residential slabs and footings, from A (sand and rock) to E and P (extremely reactive or problem sites). The letter decides the footings, and the footings are a real part of the price.",
    lede="It's a few holes drilled in the yard and a report with a letter on it, and it moves the price of everything below the floor. Here's what a soil test is, what the classes mean, why Bayside ground is what it is, and why a quote written before the test is a guess.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/what-is-a-soil-test-and-why-does-it-change-the-price.jpg",
    image_alt="A small drilling rig taking a soil sample on a cleared Bayside block, a labelled core laid out on the grass",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real job.",
    label=("The letter on the report", "The soil test"),
    card_title="What is a soil test, and why does it change the price?",
    card_blurb="A geotechnical report gives your ground a class, from A (sand and rock) to E and P. The letter decides the footings, and the footings are a real part of the price.",
    about=["Soil test", "Site classification AS 2870", "Footings", "Knockdown rebuild"],
    related=["what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane", "rebuilding-on-a-flood-overlay-block-on-the-bayside", "what-are-bayside-houses-made-of"],
    cta="Nathan reads the site classification with you and explains what it does to the footings and the price, in plain words, before the design is settled.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>A soil test is a geotechnical investigation of your block: a few boreholes, samples taken and tested, and a report that classifies the site under AS 2870, the Australian Standard for residential slabs and footings. The classes run from A (stable sand or rock) through S, M, H1 and H2 (slightly to highly reactive clay) to E (extremely reactive) and P (problem sites, including filled ground).</p>
        <p>Reactive clay swells when wet and shrinks when dry, and the house has to ride that without cracking. The higher the class, the stiffer and deeper the footings and slab have to be, and the more they cost. That's why the letter on the report changes the price.</p>
        <p>The test is done before the engineer designs the footings and before a builder can fix the price of them. A quote written without it has an allowance where the footings should be.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-it-is">What actually happens in a soil test?</a></li>
          <li><a href="#the-classes">What do the classes mean?</a></li>
          <li><a href="#bayside-ground">What is Bayside ground usually like?</a></li>
          <li><a href="#the-price">Why does it change the price?</a></li>
          <li><a href="#when">When is it done, and who orders it?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-it-is">What actually happens in a soil test?</h2>
      <p>A geotechnical technician drills boreholes at points across the block, usually where the house will sit, and logs what comes up: topsoil, fill, clay, sand, rock, and the depth of each. Samples go to a laboratory to measure how much the clay moves with moisture.</p>
      <p>The report classifies the site, notes the depth to firm ground and the water table, flags fill or old footings, and gives the engineer what they need to design the slab and footings. It's a short document with a long effect.</p>

      <h2 class="h2" id="the-classes">What do the classes mean?</h2>
      <p>AS 2870 sorts sites by expected ground movement:</p>
      <ul class="pts">
        <li><strong>A</strong> &mdash; stable sand or rock. Little movement. The simplest footings.</li>
        <li><strong>S</strong> &mdash; slightly reactive clay. Slight movement.</li>
        <li><strong>M</strong> &mdash; moderately reactive. Moderate movement; a common class in Brisbane.</li>
        <li><strong>H1 and H2</strong> &mdash; highly reactive clay. High to very high movement. Stiffened or waffle raft slabs and deeper footings.</li>
        <li><strong>E</strong> &mdash; extremely reactive. Extreme movement; engineered solutions throughout.</li>
        <li><strong>P</strong> &mdash; problem site. Fill, soft ground, unusual water conditions, or ground that varies across the block. Each one needs its own engineering.</li>
      </ul>

      <blockquote class="proof">
        <p><b>AS 2870 classifies residential sites by their predicted characteristic surface movement &mdash; the expected vertical ground movement between fully dry and fully wet &mdash; and prescribes footing and slab systems for each class.</b></p>
        <cite>Standards Australia, AS 2870 <em>Residential slabs and footings</em>. The class is an engineering input, not an opinion, and every certifier and engineer in Queensland works to it.</cite>
      </blockquote>

      <h2 class="h2" id="bayside-ground">What is Bayside ground usually like?</h2>
      <p>Varied, which is the honest answer, and the reason the test matters here.</p>
      <p>Close to the bay there's sand, and old filled ground where the foreshore and the creek flats were built up. Further back the clays begin, and on the acreage edge toward Ransome and Gumdale there are both. A block can change class from the front fence to the back. Old houses on the Bayside show it: the ones with a cracked slab or a door that never shut properly are often on clay that was never accounted for.</p>
      <p>We won't tell you your class from the street. Nobody can. That's what the drill is for.</p>

      <h2 class="h2" id="the-price">Why does it change the price?</h2>
      <p>Because the footings are designed to the class, and the footings are concrete, steel, excavation and time.</p>
      <p>A class A or S site can take a standard slab. An H or E site needs a stiffer slab with deeper edge beams, more reinforcement, sometimes piers to firm ground, and more careful drainage around the house so the moisture in the clay stays even. A P site with old fill might need the fill removed and replaced, or piers through it.</p>
      <p>None of that is optional, and none of it is visible when the house is finished. It's also the part of the price that a &ldquo;from&rdquo; figure for a house doesn't include, because the house doesn't know your ground. <a href="../what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane/">The other things that move the price are here.</a></p>

      <h2 class="h2" id="when">When is it done, and who orders it?</h2>
      <p>Early. On a knockdown rebuild it can be done with the old house still standing, drilled in the yard around it, and the results feed the design before the slab is drawn. The builder or the designer usually orders it, and a geotechnical firm does the work.</p>
      <p>If a builder hands you a fixed price for footings before the test is in, ask what class they've assumed. If they've assumed the best case, the price will move.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>A soil test classifies your ground under AS 2870,</b> from A to P.</li>
          <li><b>Reactive clay moves with moisture,</b> and the footings are designed to ride it.</li>
          <li><b>Higher class, stiffer and deeper footings, higher cost.</b> That's the link to the price.</li>
          <li><b>Bayside ground varies:</b> sand and fill near the water, clay behind it, both on the acreage edge.</li>
          <li><b>Get it done early, before the design is fixed.</b> A footing price without it is an assumption.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can we use the neighbour's soil test?</p>
          <p>As a hint, not a design. Ground changes across a fence line, and the engineer needs bores on your lot where your house will sit. The certifier will expect a report for your address.</p>
        </div>
        <div>
          <p class="q">Does a bad class mean we shouldn't build?</p>
          <p>No. Houses are built on H, E and P sites every week in Brisbane. It means the engineering is heavier and the price reflects it. What you don't want is to find out after the slab is priced.</p>
        </div>
        <div>
          <p class="q">Does the old house's cracking tell us anything?</p>
          <p>It's a clue, and it's why a builder looks under the old house at the walk-through. Cracked slabs, stumps that have moved and doors that bind all point to reactive ground. The test confirms it.</p>
        </div>
        <div>
          <p class="q">Who pays for the soil test?</p>
          <p>It's part of the job, and how it's billed depends on the builder and the stage. Ask. What matters is that it's done before the footing price is fixed.</p>
        </div>
      </div>

      <p class="small sources">Sources: Standards Australia, AS 2870 <em>Residential slabs and footings &mdash; Construction</em> (site classification); Brisbane City Council, <em>Building a new house: approvals and requirements</em>. Read 17 September 2026. This is a plain-English guide from a builder, not geotechnical or engineering advice; the classification for your lot comes from a geotechnical report on your lot.</p>
''')
