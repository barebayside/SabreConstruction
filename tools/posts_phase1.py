# Phase 1 of docs/reference/article-bank.md — the six posts that need nothing from anyone.
# Every proof point here is quoted from a published source that was read on 2026-09-17:
#   asbestos.qld.gov.au (Queensland Government)   — R9, S9, R33
#   brisbane.qld.gov.au FloodWise Property Reports — R19
#   qbcc.qld.gov.au                                — S12, R16
#   slq.qld.gov.au "Housing a growing state" 2014  — S9, R33
#   Sabre's own Google listing, cleared quotes in the real repo's docs/client-facts.md
# Rule 1: no price, no band, no timeline. Nathan's own detail is still owed on every one of these.

POSTS = {}

# ---------------------------------------------------------------- R9 · asbestos
POSTS["r9-asbestos"] = dict(
    slug="what-asbestos-removal-means-for-a-knockdown-rebuild",
    title="What is asbestos removal going to mean for our rebuild?",
    h1="What is asbestos removal<br>going to mean for our rebuild?",
    description="If your Bayside house went up between the 1940s and the late 1980s, assume asbestos is in it. What has to happen before demolition, who is allowed to do it, and why it moves the price.",
    lede="If your house went up between the 1940s and the late 1980s, assume there's asbestos in it somewhere. That's not a reason to panic and it's not a reason to keep the house. It's a job with rules, and this is what the rules mean for you.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/what-asbestos-removal-means-for-a-knockdown-rebuild.jpg",
    image_alt="Two licensed removalists in coveralls lowering a wrapped fibro sheet from the built-in-under of a 1960s highset",
    image_caption="Illustration in the style of Sabre's story frames. Not a real job.",
    card_title="What is asbestos removal going to mean for our rebuild?",
    card_blurb="Most Bayside houses from before 1990 have it somewhere. Who's allowed to remove it, what happens before the demolisher arrives, and why it moves the price.",
    about=["Asbestos removal", "Knockdown rebuild", "Brisbane Bayside"],
    related=["what-are-bayside-houses-made-of", "why-are-so-many-bayside-houses-being-knocked-down", "can-we-knock-down-our-house"],
    cta="He'll tell you where the asbestos is likely to be in your house, and what that means for the demolition, before anyone quotes anything.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Asbestos was used in Australian building materials from the 1940s to the late 1980s, and it wasn't banned nationally until the end of 2003. Most Bayside houses from that era have it somewhere: fibro sheeting, eaves, wet-area walls, the odd roof.</p>
        <p>Before your old house can be demolished, the asbestos has to come out, and in Queensland that's licensed work. A business needs a class B licence for bonded asbestos and a class A licence for the crumbly kind.</p>
        <p>For you, it means three things. The demolition has a step in front of it. That step has a cost that depends on how much asbestos there is and where it is. And the only way to know that is to have someone look at the house, not the plan.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#is-it-there">Is there asbestos in our house?</a></li>
          <li><a href="#where">Where is it usually hiding?</a></li>
          <li><a href="#who-removes-it">Who is allowed to remove it?</a></li>
          <li><a href="#before-demolition">What happens before the demolisher arrives?</a></li>
          <li><a href="#the-price">Why does it move the price?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="is-it-there">Is there asbestos in our house?</h2>
      <p>If the house was built or renovated between the 1940s and the late 1980s, the honest answer is probably.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Asbestos is a type of building material used in the building industry between the 1940s and late 1980s. The manufacture and use of asbestos products was banned nationally from 31 December 2003.&rdquo;</b></p>
        <cite>Queensland Government, asbestos.qld.gov.au, <em>What is asbestos?</em> That window covers most of the post-war housing on the Bayside, which is why we assume it's there until a test says otherwise.</cite>
      </blockquote>

      <p>The only way to be sure is a sample sent to a laboratory. Looking at it isn't enough &mdash; fibro with asbestos in it and fibro without look the same from the driveway.</p>
      <p>For a knockdown, the practical position is simpler than for a renovation. You're not deciding whether to disturb it. Everything is coming out, so the question is just how much, and what kind.</p>

      <h2 class="h2" id="where">Where is it usually hiding?</h2>
      <p>The common one is bonded asbestos cement, the stuff everyone calls fibro. It's solid and rigid, and the fibres are locked into the cement. In a Bayside house of that era you'd look for it in:</p>
      <ul class="pts">
        <li>Flat and corrugated wall and eave sheeting, especially on the built-in-under rooms of a highset house.</li>
        <li>Bathroom, laundry and kitchen walls behind the tiles.</li>
        <li>Guttering, downpipes and drainage pipes.</li>
        <li>Corrugated roofing sheets and roofing shingles.</li>
        <li>Backing boards behind old electrical switchboards, and some vinyl floor coverings.</li>
      </ul>
      <p>The one people don't expect is the friable kind, where the fibres aren't bound in anything. Some felt carpet underlay is treated as friable asbestos, and so is low-density board, which looks like ordinary sheeting and isn't. The Queensland Government publishes a diagram of the common locations in a 1970s house, and it's worth twenty minutes of your time.</p>

      <h2 class="h2" id="who-removes-it">Who is allowed to remove it?</h2>
      <p>In Queensland there are two licences, and the difference matters for your demolition.</p>

      <blockquote class="proof">
        <p><b>&ldquo;There are two types of asbestos removal licences, friable asbestos (class A) and non-friable asbestos (class B).&rdquo;</b> A business needs a class B licence to remove 10 square metres or more of bonded asbestos. Friable asbestos can only be removed by a class A licence holder.</p>
        <cite>Queensland Government, asbestos.qld.gov.au, <em>Removing or disturbing asbestos</em>, and Workplace Health and Safety Queensland. Ask your demolisher which licence they hold, and check it.</cite>
      </blockquote>

      <p>Homeowners can remove 10 square metres or less of bonded asbestos themselves if they follow the safe work procedures, and more than that only with a certificate from a Queensland Health-approved course. For a whole-house knockdown that's not the conversation. The quantities are far beyond it, and the friable material can't be touched by anyone but a class A removalist.</p>
      <p>So on a rebuild, asbestos removal is a licensed contractor's job, done before the demolition crew starts. It's either part of the demolition contract or a separate trade. Ask which.</p>

      <h2 class="h2" id="before-demolition">What happens before the demolisher arrives?</h2>
      <p>The order is set by the rules, and it's the same on every job.</p>
      <ol>
        <li><strong>Identify.</strong> Someone competent inspects the house and samples anything suspect. You end up with a list of what's there and where.</li>
        <li><strong>Plan.</strong> A licensed removalist has to prepare an asbestos removal control plan for licensed work, and it must be available to the people living in the house.</li>
        <li><strong>Notify.</strong> Certain asbestos work has to be notified to Workplace Health and Safety Queensland before it starts.</li>
        <li><strong>Remove.</strong> The licensed crew strips the asbestos, wrapped and labelled, before anything else comes down.</li>
        <li><strong>Clear.</strong> After licensed removal, a clearance inspection confirms the area is safe for normal use. For friable removal, that's a licensed asbestos assessor.</li>
        <li><strong>Dispose.</strong> Asbestos waste can only be transported and disposed of the way the law says. It doesn't go in a skip with the rest of the house.</li>
      </ol>
      <p>Only after step five does the demolition proper begin. If a quote for demolition doesn't mention any of this, that's the first question to ask.</p>

      <h2 class="h2" id="the-price">Why does it move the price?</h2>
      <p>Because none of the steps above are optional, and every one of them scales with how much asbestos there is.</p>
      <p>A lowset fibro cottage is a different removal job from a highset house where only the eaves and a bathroom are affected. A house with friable material somewhere is a different job again. That's why the honest answer to &ldquo;how much does demolition cost?&rdquo; is &ldquo;after we've looked at the house.&rdquo; We don't publish a number, because a number that doesn't know what's in your walls is a guess.</p>
      <p>What we can tell you at the walk-through is where the asbestos is likely to be, what kind, and roughly what that means for the order of the job. That's usually enough to take the fear out of it.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Built 1940s to late 1980s: assume asbestos.</b> A lab test is the only way to know for sure.</li>
          <li><b>Bonded fibro is the common one</b> &mdash; walls, eaves, wet areas, gutters, some roofs. Friable material (carpet underlay, low-density board) is rarer and stricter.</li>
          <li><b>Removal is licensed work.</b> Class B for bonded, class A for friable. Ask your demolisher which they hold.</li>
          <li><b>It happens before demolition, in a set order:</b> identify, plan, notify, remove, clearance, lawful disposal.</li>
          <li><b>The cost depends on what's there.</b> Nobody can price it from the plans, which is why we look at the house first.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can we just leave it and demolish around it?</p>
          <p>No. Demolishing a house with asbestos still in it is exactly what the rules exist to stop. It comes out first, by a licensed removalist, and the site is cleared before demolition starts.</p>
        </div>
        <div>
          <p class="q">Is it dangerous to live in the house until then?</p>
          <p>Bonded asbestos in good condition, left alone, is generally considered low risk. The danger is in disturbing it &mdash; drilling, cutting, sanding, water-blasting. If you're living there before the rebuild, don't start pulling things apart yourself.</p>
        </div>
        <div>
          <p class="q">Does asbestos affect whether we can knock the house down at all?</p>
          <p>No. That's decided by the year the house was built and whether your street is in council's character overlay. Asbestos affects how the demolition is done and what it costs, not whether it's allowed.</p>
        </div>
        <div>
          <p class="q">Who organises the removal, us or the builder?</p>
          <p>Ask. Sometimes it's inside the demolition contract, sometimes it's a separate trade. At Sabre it's part of the conversation at the walk-through, before anyone signs anything.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Government, asbestos.qld.gov.au &mdash; <em>What is asbestos?</em>, <em>How was asbestos used?</em>, <em>Removing or disturbing asbestos</em>, <em>Asbestos removal work</em>, <em>Homeowner's certificate to remove asbestos</em>, <em>Clearance inspections</em> and <em>Transport and disposal of asbestos waste</em>; Workplace Health and Safety Queensland, asbestos licences. Read 17 September 2026. This is a plain-English guide, not health, legal or planning advice. Rules change; check the current position before you decide anything.</p>
''')

# ---------------------------------------------------------------- R19 · flood overlay
POSTS["r19-flood"] = dict(
    slug="rebuilding-on-a-flood-overlay-block-on-the-bayside",
    title="Rebuilding on a flood overlay block on the Bayside: what changes?",
    h1="Rebuilding on a flood overlay block<br>on the Bayside: what changes?",
    description="Council's flood overlays don't stop most Bayside rebuilds. They change the design: how high the floor has to be, where the living areas go, and what the FloodWise report says about your lot.",
    lede="A flood overlay on your block sounds like the end of the conversation. On the Bayside it usually isn't. It changes what gets designed, not whether you can build. Here's how to read council's own report on your lot, and what it does to a new house.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/rebuilding-on-a-flood-overlay-block-on-the-bayside.png",
    image_alt="Diagram: a 1960s lowset sitting below the flood level beside a new highset designed above the minimum habitable floor level",
    image_caption="Schematic. The levels for your lot come from council's FloodWise report.",
    card_title="Rebuilding on a flood overlay block on the Bayside: what changes?",
    card_blurb="How to pull council's FloodWise report on your lot, what the four kinds of flooding mean near the water, and what an overlay does to the design of a new house.",
    about=["Flood overlay", "FloodWise Property Report", "Knockdown rebuild", "Brisbane Bayside"],
    related=["what-are-bayside-houses-made-of", "check-if-your-street-is-in-the-character-overlay", "what-asbestos-removal-means-for-a-knockdown-rebuild"],
    cta="Bring the FloodWise report, or don't &mdash; he'll pull it with you and walk the block with the levels in hand.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>A flood overlay on your Bayside block usually doesn't stop a knockdown rebuild. It sets rules for the new house: mainly how high the habitable floor has to sit, and what has to be shown in the approval.</p>
        <p>Brisbane City Council publishes the numbers for your lot in a FloodWise Property Report. It shows which of the four kinds of flooding apply &mdash; river, creek, storm tide and overland flow &mdash; the flood levels at different likelihoods, and the minimum habitable floor level a new house must meet.</p>
        <p>Near the water, storm tide and overland flow are the ones that matter most. For a builder, the report is a design input like the slope or the soil. It changes where the living areas go, how the house meets the ground, and sometimes whether the house is highset. It rarely changes whether there's a house at all.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-is-it">What is a flood overlay, and which one do we have?</a></li>
          <li><a href="#the-report">How do we get council's report on our lot?</a></li>
          <li><a href="#four-kinds">Which of the four kinds of flooding matter on the Bayside?</a></li>
          <li><a href="#the-design">What does it do to the design of a new house?</a></li>
          <li><a href="#the-approval">What does it do to the approval?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-is-it">What is a flood overlay, and which one do we have?</h2>
      <p>An overlay is a map layer in Brisbane City Plan 2014 that tells council, and you, that a rule applies to your land on top of the ordinary zoning. The character overlay is one. The flood overlays are another set.</p>
      <p>There isn't one flood overlay. Council maps flooding from rivers, from creeks and waterways, from storm tide off the bay, and from overland flow &mdash; the water that runs across land in a downpour before it reaches a drain. A block can be in none, one or several.</p>
      <p>So the first job is not to worry about &ldquo;the flood overlay.&rdquo; It's to find out which ones touch your lot, and at what level.</p>

      <h2 class="h2" id="the-report">How do we get council's report on our lot?</h2>
      <p>Council publishes it online, and you don't need to ask anyone.</p>
      <ol>
        <li>Go to council's <a href="https://fam.brisbane.qld.gov.au/" rel="noopener">Flood Awareness Map</a>. Choose <strong>I am a resident, business or visitor</strong>, then search the map for your address.</li>
        <li>The <strong>Flooding Overview</strong> panel shows which types of flooding could affect the property, and how likely each is.</li>
        <li>Click <strong>Technical FloodWise Property Report</strong>. Council says it downloads in about 20 seconds.</li>
      </ol>

      <blockquote class="proof">
        <p><b>The FloodWise Property Report &ldquo;includes technical flood information for building and development&rdquo; and is &ldquo;based on the latest adopted flood planning information in Council's planning scheme, Brisbane City Plan 2014.&rdquo;</b> It shows flood levels for the 0.2%, 1%, 2%, 5% and 20% AEP events, the minimum habitable floor level, and which City Plan overlays for river, creek, overland flow and coastal hazard apply.</p>
        <cite>Brisbane City Council, <em>FloodWise Property Reports</em>. That report is the document a builder and a certifier work from. Print it before you talk to anyone.</cite>
      </blockquote>

      <p>Two things to know when you read it.</p>
      <ul class="pts">
        <li><strong>AEP means annual exceedance probability.</strong> A 1% AEP flood has a one-in-a-hundred chance of happening in any given year. It's not &ldquo;once a century.&rdquo; It can happen two years running.</li>
        <li><strong>The aerial map in the report does not show overland flow.</strong> Council says so on the page. A lot that looks clear on the picture can still carry an overland flow flag further down the report.</li>
      </ul>

      <h2 class="h2" id="four-kinds">Which of the four kinds of flooding matter on the Bayside?</h2>
      <p>Wynnum, Manly and Lota don't sit on the Brisbane River, so river flooding is rarely the issue it is in the western suburbs. What the Bayside has instead:</p>
      <ul class="pts">
        <li><strong>Storm tide.</strong> The bay pushed up by a storm and a high tide together. Council maps it under the coastal hazard overlay, and it's the one that decides floor levels closest to the water.</li>
        <li><strong>Creek and waterway flooding.</strong> The creeks that drain to the bay back up when the tide is high and the rain is heavy at the same time.</li>
        <li><strong>Overland flow.</strong> The one nobody expects on a block that's never been near a creek. In a Queensland downpour, water runs across land before the drains can take it, and low points on old blocks collect it.</li>
      </ul>

      <blockquote class="proof">
        <p><b>&ldquo;It is important to note that flooding may still present a risk and could include overland flow, which is shown as a property development flag further down the report.&rdquo;</b></p>
        <cite>Brisbane City Council, <em>FloodWise Property Reports</em>, on lots where no river, creek or storm tide level has been assigned. In plain words: no levels on the graph does not mean no flood rules on the lot.</cite>
      </blockquote>

      <h2 class="h2" id="the-design">What does it do to the design of a new house?</h2>
      <p>This is where an overlay stops being a worry and becomes a brief.</p>
      <p><strong>The floor goes up.</strong> The report gives a minimum habitable floor level. Bedrooms and living areas have to sit at or above it. On a lot near the water that can mean the house is highset, or the ground floor holds the garage, laundry and storage while the family lives upstairs.</p>
      <p><strong>The plan turns around.</strong> A house designed for the level, rather than fitted to it afterwards, puts the rooms that matter where the water can't reach and uses the space underneath for the things that can get wet.</p>
      <p><strong>The materials change downstairs.</strong> What's below the flood level is built to be hosed out, not rebuilt. That's a detail decision, and it's cheap to get right at the drawing stage and expensive to get right later.</p>
      <p>This is the reason we'd rather design to your block than fit a plan to it. A package house drawn for a flat estate lot doesn't know your floor level. Your block does.</p>

      <h2 class="h2" id="the-approval">What does it do to the approval?</h2>
      <p>If a flood overlay applies, the report tells you there are flood planning requirements for development. The design has to show it meets them. That's part of the normal approval, handled by the designer and the certifier, and it's paperwork rather than a fight.</p>
      <p>What it isn't, on the Bayside, is a bar. Streets one back from the esplanade have been rebuilt to the current levels for years, and you can see the result: the living areas up, the ground floor open or built for storage.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>A flood overlay usually changes the design, not the answer.</b> On the Bayside a rebuild on an overlay block is normal.</li>
          <li><b>Pull the FloodWise Property Report yourself.</b> Council's Flood Awareness Map, your address, one button.</li>
          <li><b>Storm tide and overland flow are the Bayside ones.</b> River flooding is mostly somebody else's problem.</li>
          <li><b>1% AEP means one in a hundred each year</b> &mdash; not once a century.</li>
          <li><b>The report sets the minimum habitable floor level.</b> Design to it from the start and the house gets better, not just compliant.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Our house has never flooded. Why is there an overlay?</p>
          <p>The overlays are modelled, not a record of what's happened. Council maps where water would go in events of a given likelihood, including ones that haven't occurred in your time on the block. A dry history is good news; it isn't the same as no rules.</p>
        </div>
        <div>
          <p class="q">Does an overlay mean we can't have a lowset house?</p>
          <p>It depends on the minimum habitable floor level in your report against the ground level on your lot. Sometimes a lowset house on a raised slab meets it. Sometimes the numbers push you highset. The report and a builder on the block will tell you which.</p>
        </div>
        <div>
          <p class="q">Will it change our insurance?</p>
          <p>We're builders, not insurers, so ask yours. What we can say is that a new house designed to the current flood levels is a different proposition from a 1960s house that wasn't, and it's worth telling the insurer that.</p>
        </div>
        <div>
          <p class="q">Can you read the report for us?</p>
          <p>Yes. Bring it to the walk-through, or we'll pull it together. Nathan will tell you what the levels mean for your block and what they'd do to a design.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <a href="https://www.brisbane.qld.gov.au/planning-and-building/planning-guidelines-and-tools/online-tools/floodwise-property-reports" rel="noopener">FloodWise Property Reports</a> and <a href="https://fam.brisbane.qld.gov.au/" rel="noopener">Flood Awareness Online</a>; Brisbane City Plan 2014. Read 17 September 2026. This is a plain-English guide, not planning, engineering or insurance advice. Council's flood information is updated from time to time; read the current report for your lot before you decide anything.</p>
''')

# ---------------------------------------------------------------- S9 · what the houses are made of
POSTS["s9-houses"] = dict(
    slug="what-are-bayside-houses-made-of",
    title="What are the houses on the Bayside actually made of?",
    h1="What are the houses on the Bayside<br>actually made of?",
    description="Pre-war timber on stumps, post-war fibro and chamferboard, the 1960s highset with the built-in-under, 1970s brick. What each Bayside house type is like to live in, to change, and to knock down.",
    lede="Walk any street in Wynnum, Manly or Lota and you're walking through seventy years of Brisbane building, one house at a time. Each era built a different house. Each one ages differently, changes differently, and comes down differently. Here's the field guide.",
    date="2026-09-17", category="Living on the Bayside", image="blog/what-are-bayside-houses-made-of.jpg",
    image_alt="Four Bayside houses on one street: pre-war Queenslander, post-war cottage, 1960s highset, 1970s brick",
    image_caption="Illustration of the four common Bayside house types. Not a real street.",
    card_title="What are the houses on the Bayside actually made of?",
    card_blurb="Pre-war timber, post-war fibro, the 1960s highset, 1970s brick. What each one is like to live in, to change, and to knock down &mdash; from a builder who's opened up all of them.",
    about=["Queensland houses", "Post-war housing", "Brisbane Bayside", "Wynnum", "Manly"],
    related=["why-are-so-many-bayside-houses-being-knocked-down", "what-asbestos-removal-means-for-a-knockdown-rebuild", "can-we-knock-down-our-house"],
    cta="He'll tell you which of these your house is, what's behind the walls, and what that means for the choice between changing it and starting again.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Four kinds of house make up most of the Bayside's streets, and you can date them from the footpath.</p>
        <p><strong>Pre-1947:</strong> timber on stumps, tin roof, vertical-joint walls inside. <strong>Late 1940s to 1950s:</strong> the post-war cottage, lowset timber or fibro, small and simple, built fast during a national housing shortage. <strong>1960s to 1970s:</strong> the highset, chamferboard or brick upstairs, with rooms built in underneath later. <strong>1970s onward:</strong> brick veneer on a concrete slab.</p>
        <p>What they're made of decides what happens to them next. Timber on stumps can be raised, moved and opened up. Fibro from before 1990 almost always contains asbestos. Brick on a slab can't be lifted, and when it stops suiting the family, the honest options narrow to a big renovation or starting again.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#pre-war">The pre-war timber house: what's it made of?</a></li>
          <li><a href="#post-war">The post-war cottage: why is it so small?</a></li>
          <li><a href="#highset">The highset: what's really underneath?</a></li>
          <li><a href="#brick">The brick house on a slab: what can and can't change?</a></li>
          <li><a href="#salt">What does the bay do to all of them?</a></li>
          <li><a href="#what-next">Which ones get changed, and which get replaced?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="pre-war">The pre-war timber house: what's it made of?</h2>
      <p>Hardwood frame on timber or concrete stumps. Weatherboard outside, single-skin vertical-joint boards inside, so the wall between two rooms is one board thick. Casement windows, a corrugated iron roof, a verandah that has usually been closed in at least once.</p>
      <p>They were built to breathe. Air under the floor, air through the walls, air across the verandah. That's why they're bearable in February without machinery, and why they're cold in July.</p>
      <p>If your house is one of these and your street is in council's character overlay, the rules about knocking it down are different. That's the one type where the year matters more than the condition &mdash; <a href="../can-we-knock-down-our-house/">the rules in plain words are here</a>.</p>

      <h2 class="h2" id="post-war">The post-war cottage: why is it so small?</h2>
      <p>Because there was nothing to build it with.</p>

      <blockquote class="proof">
        <p><b>&ldquo;In 1946, Brisbane architect Robert Cummings estimated that there was a shortfall of 300,000 houses nationwide.&rdquo;</b> Brisbane suburbs &ldquo;became populated with low-set timber houses on quarter acre blocks.&rdquo;</p>
        <cite>State Library of Queensland, <em>Housing a growing state</em>, 2014. The shortage is why the post-war cottage is small, plain and built from whatever could be had &mdash; and why so many of them are on the good blocks.</cite>
      </blockquote>

      <p>The typical one is lowset, a couple of steps up, timber or fibro clad, with a hipped tin or tile roof, two or three small bedrooms and one bathroom. Materials were rationed, so the frame is lighter than a pre-war house and the rooms are tighter.</p>
      <p>On the Bayside these sit on some of the best land there is: flat blocks near the water and the train, bought when nobody wanted to live that far out. The house was never the point. The block was, and still is.</p>

      <h2 class="h2" id="highset">The highset: what's really underneath?</h2>
      <p>The 1960s and 70s Bayside house is up on posts, with chamferboard or brick upstairs and a concrete slab below. It was built high for air and for the car, with a laundry and a workshop under the floor.</p>
      <p>Then families grew, and the space underneath got built in. Rumpus room, extra bedroom, second bathroom, often by the owner, often over a weekend. This is the part a builder looks at first, because:</p>
      <ul class="pts">
        <li><strong>The head height often isn't legal habitable height.</strong> The floor above was never meant to be a ceiling. Those downstairs rooms are often not rooms on paper.</li>
        <li><strong>The cladding underneath is very often fibro.</strong> And fibro from that era is where the asbestos is.</li>
        <li><strong>The slab downstairs sits at ground level,</strong> which on a Bayside block can be below the flood planning level for a new house.</li>
      </ul>

      <blockquote class="proof">
        <p><b>&ldquo;Asbestos cement sheeting was commonly used in building materials from 1940s to the late 1980s in both domestic residences and other structures.&rdquo;</b> Non-friable asbestos materials &ldquo;are the most common in domestic houses. They are commonly called 'fibro', 'asbestos cement' and 'AC sheeting'.&rdquo;</p>
        <cite>Queensland Government, asbestos.qld.gov.au. Which is why we treat every built-in-under from before 1990 as containing asbestos until a test says otherwise. <a href="../what-asbestos-removal-means-for-a-knockdown-rebuild/">What that means for a rebuild is here.</a></cite>
      </blockquote>

      <h2 class="h2" id="brick">The brick house on a slab: what can and can't change?</h2>
      <p>From the 1970s the Bayside got the brick veneer house: a timber frame with a single skin of brick outside, on a concrete slab, tile roof, aluminium windows. Solid, low maintenance, and the first Bayside house type that can't be picked up and moved.</p>
      <p>That last point decides everything. A timber house on stumps can be raised, shifted on the block, or opened up underneath. A brick house on a slab is where it is, at the height it is. Changing the layout means cutting brick and re-supporting the roof. Adding a storey means engineering the slab and the walls for a load they weren't designed for.</p>
      <p>It can be done. Whether it should be is a cost question, and the honest answer is different on every block.</p>

      <h2 class="h2" id="salt">What does the bay do to all of them?</h2>
      <p>Salt, wind and the tide, every day, for decades.</p>
      <ul class="pts">
        <li><strong>Steel rusts faster.</strong> Roofing screws, gutters, the reinforcing in old concrete stumps and slabs, aluminium window fittings.</li>
        <li><strong>Paint doesn't last.</strong> The western face of a Bayside house takes the afternoon sun; the eastern face takes the salt.</li>
        <li><strong>Timber moves.</strong> Humidity swells it, the dry westerlies shrink it. Old joints open. Doors stick in summer and rattle in winter.</li>
      </ul>
      <p>None of this is a reason to knock a house down. It's the reason a builder looks at the frame and the stumps before anyone talks about the kitchen.</p>

      <h2 class="h2" id="what-next">Which ones get changed, and which get replaced?</h2>
      <p>There's no rule, but there's a pattern, and it comes straight from the materials.</p>
      <div class="tablewrap">
        <table>
          <thead><tr><th>House</th><th>Made of</th><th>What usually happens</th></tr></thead>
          <tbody>
            <tr><td>Pre-1947 timber</td><td>Hardwood on stumps, VJ walls, tin</td><td>Raised, restored, extended. Often can't be demolished if the street is in the overlay</td></tr>
            <tr><td>Post-war cottage</td><td>Light timber or fibro, lowset</td><td>The house is small and the block is good. This is the classic knockdown rebuild</td></tr>
            <tr><td>1960s&ndash;70s highset</td><td>Chamferboard or brick over a slab, fibro underneath</td><td>Depends on the built-in-under. Legal height and asbestos decide whether it's a renovation or a rebuild</td></tr>
            <tr><td>1970s+ brick veneer</td><td>Brick skin, timber frame, slab</td><td>Kitchens and bathrooms for decades; then a hard choice between a big renovation and starting again</td></tr>
          </tbody>
        </table>
      </div>
      <p>The families who come to us have almost always outgrown the house and not the street. Knowing what the house is made of is the first step to knowing whether it can grow with you, or whether the block is the thing worth keeping. <a href="../why-are-so-many-bayside-houses-being-knocked-down/">Why so many families on the Bayside end up choosing the second option is here.</a></p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Four house types, four eras, and you can date them from the footpath.</b> Pre-war timber, post-war cottage, the highset, brick on a slab.</li>
          <li><b>Timber on stumps can move; brick on a slab can't.</b> That one fact decides most renovation-or-rebuild conversations.</li>
          <li><b>The built-in-under is where the problems are:</b> head height, fibro, ground-level floors.</li>
          <li><b>Anything clad before 1990 gets treated as asbestos</b> until a test says otherwise.</li>
          <li><b>The bay wears everything.</b> Check the frame and the stumps before the kitchen.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">How do I tell what year my house is from?</p>
          <p>The footpath test above gets you close. For the actual year, Brisbane City Archives hold building records back to 1904, and the step-by-step is in <a href="../check-if-your-street-is-in-the-character-overlay/">the overlay check</a>.</p>
        </div>
        <div>
          <p class="q">Is a timber house worth less than a brick one?</p>
          <p>Not to a builder. A sound hardwood frame on good stumps is easier to work with than most brick veneer. What matters is the condition of the frame and the stumps, and that's a look, not a material.</p>
        </div>
        <div>
          <p class="q">Our downstairs rooms are lovely. Are you saying they don't count?</p>
          <p>They count to you. On paper, if the ceiling is below legal habitable height, they may not be bedrooms or living rooms, and that affects an approval, a valuation and a sale. Worth knowing before you plan around them.</p>
        </div>
        <div>
          <p class="q">Can you tell us what our house is made of without opening it up?</p>
          <p>Mostly, yes. Stumps, cladding, windows and roofline tell a builder a lot in thirty seconds. The things that need a test &mdash; asbestos, termite damage, the state of the slab &mdash; we'll tell you about at the walk-through.</p>
        </div>
      </div>

      <p class="small sources">Sources: State Library of Queensland, <a href="https://www.slq.qld.gov.au/blog/housing-growing-state" rel="noopener"><em>Housing a growing state</em></a>, 30 September 2014; Queensland Government, asbestos.qld.gov.au, <em>What is asbestos?</em> and <em>How was asbestos used?</em>; Brisbane City Council, Brisbane City Plan 2014. House descriptions are a builder's general guide to common Brisbane types, not a survey of any particular house. Read 17 September 2026. Not planning, engineering or health advice.</p>
''')

# ---------------------------------------------------------------- R33 · why so many get knocked down
POSTS["r33-why"] = dict(
    slug="why-are-so-many-bayside-houses-being-knocked-down",
    title="Why are so many Bayside houses being knocked down?",
    h1="Why are so many Bayside houses<br>being knocked down?",
    description="Post-war houses hitting the end of their working life, fibro from the asbestos era, small houses on the best blocks near the water, and families who want the street more than the house.",
    lede="Drive Wynnum or Manly on a weekday and you'll pass a fence with a demolition sign on it. Then another. It isn't a fashion. It's four things arriving at once, and most of them are about the block, not the house.",
    date="2026-09-17", category="Living on the Bayside", image="blog/why-are-so-many-bayside-houses-being-knocked-down.jpg",
    image_alt="A small post-war cottage behind temporary fencing with an excavator, a new two-storey home next door",
    image_caption="Illustration in the style of Sabre's story frames. Not a real job.",
    card_title="Why are so many Bayside houses being knocked down?",
    card_blurb="Four things arriving at once: the post-war houses are seventy years old, the fibro era is ending, the blocks are the best in Brisbane, and families want the street more than the house.",
    about=["Knockdown rebuild", "Brisbane Bayside", "Post-war housing", "Wynnum", "Manly"],
    related=["what-are-bayside-houses-made-of", "can-we-knock-down-our-house", "what-is-a-knockdown-rebuild-package"],
    cta="If you're at the fork between moving and staying, he'll walk the house with you and tell you honestly which side of it your block is on.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Four things, arriving together.</p>
        <p>The post-war houses that fill the Bayside were built fast, small and light during a national housing shortage, and they're now seventy years old. A great many of them are clad in fibro from the asbestos era, which makes a big renovation an asbestos job before it's anything else. The blocks they sit on are some of the best in Brisbane &mdash; flat, near the water, near the train and the schools. And the families in them have outgrown the house without outgrowing the street.</p>
        <p>Put those together and the maths of the block changes. When the house is worth little and the land is worth a lot, and the family wants to stay, starting again on the same block becomes the honest option. Not always. But often enough that you'll see the signs.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#age">Reason one: the houses are at the end of their working life</a></li>
          <li><a href="#fibro">Reason two: the fibro era is ending</a></li>
          <li><a href="#blocks">Reason three: the blocks were always the point</a></li>
          <li><a href="#family">Reason four: the family wants the street, not the house</a></li>
          <li><a href="#not-all">Which houses don't get knocked down?</a></li>
          <li><a href="#is-it-you">Is this you?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="age">Reason one: the houses are at the end of their working life</h2>
      <p>Most of the Bayside's housing went up in a hurry after the war.</p>

      <blockquote class="proof">
        <p><b>&ldquo;In 1946, Brisbane architect Robert Cummings estimated that there was a shortfall of 300,000 houses nationwide.&rdquo;</b> Brisbane's suburbs &ldquo;became populated with low-set timber houses on quarter acre blocks.&rdquo;</p>
        <cite>State Library of Queensland, <em>Housing a growing state</em>, 2014. Houses built to end a shortage were built for the shortage, not for the family of 2026.</cite>
      </blockquote>

      <p>A house from that era is now sixty to seventy-five years old. Light frames, small rooms, one bathroom, stumps that have been replaced at least once, wiring and plumbing that have been added to rather than redone. None of that is a fault. It's what seventy years does.</p>
      <p>The question every owner eventually hits is whether the next round of work &mdash; restumping, rewiring, a new roof, a second bathroom &mdash; is money into a house that will still be small and old when it's finished.</p>

      <h2 class="h2" id="fibro">Reason two: the fibro era is ending</h2>
      <p>A lot of Bayside houses, and most of the built-in-under rooms beneath the highsets, are clad in asbestos cement sheeting.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Asbestos cement sheeting was commonly used in building materials from 1940s to the late 1980s in both domestic residences and other structures.&rdquo;</b></p>
        <cite>Queensland Government, asbestos.qld.gov.au, <em>How was asbestos used?</em> On a house from that era, a big renovation starts as a licensed asbestos removal job before a single new wall goes up.</cite>
      </blockquote>

      <p>That changes the renovation sums. If the walls are coming off to be replaced anyway, and the removal is licensed work either way, the gap between &ldquo;renovate heavily&rdquo; and &ldquo;start again&rdquo; gets narrower than people expect. <a href="../what-asbestos-removal-means-for-a-knockdown-rebuild/">What asbestos removal means for a rebuild is here.</a></p>

      <h2 class="h2" id="blocks">Reason three: the blocks were always the point</h2>
      <p>When these houses were built, the Bayside was a long way from anywhere. The blocks were big and cheap and flat, and the house was whatever could be put on them.</p>
      <p>Now they're some of the best residential land in Brisbane: near the water, near the train, near schools, on ground that doesn't need retaining walls. The land carries the value. The house, in many cases, doesn't.</p>
      <p>When that's true, every dollar spent on the old house is a dollar that doesn't move the block's value much. A new house designed for the block does. That's the maths behind a lot of the signs on a lot of the fences, and it's not sentimental. It's arithmetic.</p>

      <h2 class="h2" id="family">Reason four: the family wants the street, not the house</h2>
      <p>This is the one we hear most, and it's the reason we're in this business.</p>
      <p>The kids are in the school. The neighbours are friends. The walk to the water is the walk you moved here for. The house has two bedrooms and one bathroom and nowhere to work from home, and the alternative is a bigger house in a suburb you don't want to live in.</p>
      <p>So the family stays and the house goes. The decision is about the street. The demolition is just what it costs to keep it.</p>

      <h2 class="h2" id="not-all">Which houses don't get knocked down?</h2>
      <p>Plenty, and for good reasons.</p>
      <ul class="pts">
        <li><strong>Pre-1947 houses in the character overlay.</strong> Council decides those, and the answer is often no. <a href="../can-we-knock-down-our-house/">The rules are here.</a></li>
        <li><strong>Sound hardwood houses on good stumps.</strong> A pre-war timber house in good order can be raised, opened up and extended, and often should be.</li>
        <li><strong>Houses where the family fits.</strong> If the house works and the problem is a tired kitchen, that's a renovation.</li>
        <li><strong>Blocks where the numbers don't work.</strong> Awkward access, a steep fall, an overlay that pushes the design somewhere expensive. Sometimes the honest answer is stay, or sell.</li>
      </ul>
      <p>Anyone who tells you every old house should come down is selling something. So is anyone who tells you none of them should.</p>

      <h2 class="h2" id="is-it-you">Is this you?</h2>
      <p>You don't need to decide from an article. You need three facts about your own place:</p>
      <ol>
        <li><strong>The year and the overlay.</strong> <a href="../check-if-your-street-is-in-the-character-overlay/">Fifteen minutes, two free checks.</a></li>
        <li><strong>What the house is made of</strong>, and whether the frame and stumps are sound. <a href="../what-are-bayside-houses-made-of/">The field guide is here.</a></li>
        <li><strong>What you actually want from the next ten years</strong> in this street.</li>
      </ol>
      <p>The first two a builder can tell you in a walk-through. The third is yours.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>The post-war houses are seventy years old</b> and were built for a shortage, not for the family living in them now.</li>
          <li><b>Fibro from before 1990 turns a big renovation into an asbestos job first.</b> That narrows the gap between renovating and rebuilding.</li>
          <li><b>The land carries the value.</b> On a good Bayside block the house often doesn't.</li>
          <li><b>Families stay for the street.</b> The rebuild is what it costs to keep it.</li>
          <li><b>Not every house should come down.</b> Overlay, condition, fit and block all argue the other way sometimes.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Isn't it wasteful to knock down a house that still stands?</p>
          <p>Sometimes. A sound house that fits the family should be kept. A small, tired house on a block that could carry the home a family needs for the next thirty years is a different case, and the honest comparison is the life of the new house against the money the old one would keep absorbing.</p>
        </div>
        <div>
          <p class="q">Are the character rules stopping it?</p>
          <p>In the streets they cover, yes, deliberately. The Traditional building character overlay exists to keep the pre-1947 streetscape, and demolishing a pre-1947 house inside it needs council's approval. Most post-war houses aren't covered.</p>
        </div>
        <div>
          <p class="q">How do I know if my house is worth renovating instead?</p>
          <p>Get someone to look at the frame, the stumps and what's behind the cladding, and be honest about whether the layout can ever be the house you need. A builder who does both renovations and rebuilds will tell you which yours is. We do both.</p>
        </div>
        <div>
          <p class="q">What happens to the old house?</p>
          <p>Asbestos comes out first, by a licensed removalist. Then the demolition. Salvageable hardwood, windows and fittings are sometimes worth taking; the honest answer is usually that very little of an old house goes into the new one.</p>
        </div>
      </div>

      <p class="small sources">Sources: State Library of Queensland, <a href="https://www.slq.qld.gov.au/blog/housing-growing-state" rel="noopener"><em>Housing a growing state</em></a>, 30 September 2014; Queensland Government, asbestos.qld.gov.au, <em>How was asbestos used?</em>; Brisbane City Council, Heritage and character properties, Brisbane City Plan 2014. The reasons above are a builder's observations from working on the Bayside, not a survey. Read 17 September 2026. Not planning or financial advice.</p>
''')

# ---------------------------------------------------------------- S12 · the QBCC
POSTS["s12-qbcc"] = dict(
    slug="what-is-the-qbcc-and-what-to-check-on-a-builders-licence",
    title="What is the QBCC, and what should you check on a builder's licence?",
    h1="What is the QBCC, and what should you<br>check on a builder's licence?",
    description="The Queensland Building and Construction Commission licenses builders, runs the public register, and runs the Home Warranty Scheme. How to look a builder up in five minutes, and what the register does and doesn't tell you.",
    lede="Before you sign anything with a builder in Queensland, you can look them up. It takes five minutes, it's free, and it tells you things a brochure never will. Here's what the QBCC is, what the register shows, and what to do with it.",
    date="2026-09-17", category="Dealing with a builder", image="blog/what-is-the-qbcc-and-what-to-check-on-a-builders-licence.jpg",
    image_alt="A verandah table with a building contract, a hard hat and a laptop open at a blank licence search",
    image_caption="Illustration.",
    card_title="What is the QBCC, and what should you check on a builder's licence?",
    card_blurb="The regulator, the public register and the Home Warranty Scheme, in plain words. How to look any builder up in five minutes &mdash; including us.",
    about=["QBCC", "Builder licence", "Queensland Home Warranty Scheme", "Choosing a builder"],
    related=["who-are-the-small-independent-builders-on-brisbanes-bayside", "what-is-a-knockdown-rebuild-package", "rebuilding-in-wynnum-or-manly"],
    cta="Look us up first &mdash; licence 15486557 &mdash; then come and meet the people behind the number.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>The QBCC is the Queensland Building and Construction Commission, the state body that regulates the building industry. It licenses builders and tradespeople, keeps a public register of every licence, handles complaints about defective work, and runs the Queensland Home Warranty Scheme that insures your build.</p>
        <p>Before you sign with any builder, search the QBCC licensee register for their licence number. Check three things: that the licence is current, that its class covers the work you're asking for, and that the name on it is the entity you're contracting with. The register also shows the licensee's history, including any disciplinary action.</p>
        <p>Then ask about home warranty insurance. It's compulsory on residential work over $3,300, the premium is part of your contract price, and it's what protects you if the builder doesn't finish or doesn't fix defects. Sabre's licence is 15486557. Go and look.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-is-it">What is the QBCC?</a></li>
          <li><a href="#how-to-search">How do you look a builder up?</a></li>
          <li><a href="#what-to-check">What should you check on the licence?</a></li>
          <li><a href="#what-it-doesnt-show">What doesn't the register tell you?</a></li>
          <li><a href="#warranty">What is the Home Warranty Scheme, and what does it cover?</a></li>
          <li><a href="#fixed-vs-cost-plus">Why does the type of contract matter to the insurance?</a></li>
          <li><a href="#sabre">Where does Sabre sit in all this?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-is-it">What is the QBCC?</h2>
      <p>It's the regulator. Every builder, and most trades, in Queensland needs a licence from it to do the work legally.</p>

      <blockquote class="proof">
        <p><b>&ldquo;The QBCC is a statutory body &hellip; established under the Queensland Building and Construction Commission Act 1991 (QBCC Act) to regulate the building industry.&rdquo;</b> It &ldquo;helps to ensure maintenance of proper building standards and remedies for defective building work.&rdquo;</p>
        <cite>Queensland Building and Construction Commission, <em>About us</em>. In plain words: it decides who can build, keeps the list, and is who you go to when something's wrong.</cite>
      </blockquote>

      <p>Four jobs matter to you as a homeowner:</p>
      <ul class="pts">
        <li><strong>Licensing.</strong> A builder without a current QBCC licence can't lawfully contract for your build.</li>
        <li><strong>The register.</strong> Every licence is public, with its history.</li>
        <li><strong>Complaints and disputes.</strong> Defective work, non-completion, and the process for both.</li>
        <li><strong>The Queensland Home Warranty Scheme.</strong> The insurance behind residential building work.</li>
      </ul>

      <h2 class="h2" id="how-to-search">How do you look a builder up?</h2>
      <ol>
        <li>Ask the builder for their <strong>QBCC licence number</strong>. Any builder will give it to you without a pause. Ours is on every page of this site.</li>
        <li>Go to the QBCC website and choose <strong>Search a QBCC register</strong>, then the <strong>licensee register</strong>.</li>
        <li>Search by the licence number, or by name if you don't have it. Searching by number avoids a builder with a similar name.</li>
        <li>Open the record.</li>
      </ol>
      <p>If you'd rather talk to a person, the QBCC's number is 139 333.</p>

      <h2 class="h2" id="what-to-check">What should you check on the licence?</h2>

      <blockquote class="proof">
        <p><b>&ldquo;Search the QBCC licensee register to check the history of your builder before you sign the contract on your next repair, renovation or build.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Our lists and registers</em>. Their words, not ours. Do it before the deposit, not after.</cite>
      </blockquote>

      <p>Three things, in this order:</p>
      <ol>
        <li><strong>Is it current?</strong> The status should be active. Not suspended, not cancelled, not expired.</li>
        <li><strong>Does the class cover the work?</strong> Licence classes say what a licensee may do. A new house or a knockdown rebuild needs a builder's licence that covers that scope, not a trade licence.</li>
        <li><strong>Is it the same entity?</strong> The name and ABN on the licence should match the name on your quote and your contract. A licence held by a person doesn't cover a company they've since set up, and the other way round.</li>
      </ol>
      <p>Then read the history. The register records disciplinary matters against a licensee, including demerit points and directions to rectify, for a period after they occur. A clean history isn't a guarantee. A messy one is information.</p>

      <h2 class="h2" id="what-it-doesnt-show">What doesn't the register tell you?</h2>
      <p>Whether they're any good.</p>
      <p>A licence says a builder met the requirements to hold one. It doesn't say they answer the phone in month four, or that their last three families would build with them again. For that you want their Google reviews, all of them, and a phone number for a recent client. <a href="../rebuilding-in-wynnum-or-manly/">Point five here is how we'd read a builder's reviews.</a></p>
      <p>The register also may not show everything about a licensee's financial position or civil disputes. It's one check, not the only one.</p>

      <h2 class="h2" id="warranty">What is the Home Warranty Scheme, and what does it cover?</h2>
      <p>It's the insurance behind your build, and the builder arranges it, not you.</p>
      <p>In the QBCC's own words, the premium is &ldquo;collected from you and paid to us by the contractor&rdquo;, is &ldquo;included as part of your contract&rdquo;, and is &ldquo;compulsory for all residential construction work valued at more than $3,300 (including cost of materials, labour and GST).&rdquo; The cover lasts for six years and six months.</p>
      <p>It protects you in two situations:</p>
      <ul class="pts">
        <li><strong>Non-completion</strong> &mdash; the builder doesn't, or can't, finish the work you contracted for.</li>
        <li><strong>Defective work</strong> &mdash; the builder doesn't fix defects.</li>
      </ul>
      <p>The scheme covers a maximum of $200,000 for each category of loss, or $300,000 if optional additional cover was taken out within the time limits. It is not home and contents insurance, and it can't be transferred from one contractor to another.</p>
      <p>The practical check: <strong>ask your builder how the home warranty premium appears in your contract.</strong> If it doesn't, ask why.</p>

      <h2 class="h2" id="fixed-vs-cost-plus">Why does the type of contract matter to the insurance?</h2>
      <p>Because the scheme treats the two common contract types differently, and most people don't find out until it matters.</p>
      <p>The QBCC says fixed-price residential contracts can be covered for both non-completion and defective work claims. Cost-plus contracts are covered for defective work only. Their reasoning: to settle a non-completion claim they need to know what you agreed to pay to finish, and a cost-plus contract has no fixed final price.</p>
      <p>That's not an argument against cost-plus in every case. It's a thing to know before you choose, and it's one of the questions worth putting to any builder, including us.</p>

      <h2 class="h2" id="sabre">Where does Sabre sit in all this?</h2>
      <p>QBCC licence <strong>15486557</strong>. Master Builders Queensland member <strong>00352</strong>. Both numbers are in the footer of every page on this site.</p>
      <p>We put them there so you don't have to ask. Look us up, read the history, then read the reviews. We'd rather you did all three before you rang.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>The QBCC licenses builders, keeps the public register and runs the warranty scheme.</b> It's the regulator.</li>
          <li><b>Search the licensee register by number before you sign.</b> Current, right class, same entity, then the history.</li>
          <li><b>A licence says they may build. It doesn't say they're good.</b> Reviews and a recent client's phone number do that.</li>
          <li><b>Home warranty insurance is compulsory over $3,300, paid through your contract, and lasts 6 years 6 months.</b> Ask where it is in yours.</li>
          <li><b>Fixed-price and cost-plus contracts are insured differently.</b> Cost-plus is covered for defects only.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Does the search cost anything?</p>
          <p>No. The QBCC licensee register is public and free to search online.</p>
        </div>
        <div>
          <p class="q">The builder says the insurance is &ldquo;included.&rdquo; Is that enough?</p>
          <p>Ask to see where. The premium forms part of your contract price, and the QBCC issues the policy for your work. You should be able to see the cover attached to your property.</p>
        </div>
        <div>
          <p class="q">What if we're buying a house that was recently built or renovated?</p>
          <p>The QBCC says a buyer or their legal agent can search whether any home warranty insurance is attached to the property. Worth doing before settlement on any recently built Bayside home.</p>
        </div>
        <div>
          <p class="q">What's the difference between the QBCC and Master Builders?</p>
          <p>The QBCC is the government regulator; every builder must hold its licence. Master Builders Queensland is an industry association a builder chooses to join. Both numbers are worth checking, and they're different things.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission &mdash; <em>About us</em>; <em>Our lists and registers</em>; <em>Queensland Home Warranty Scheme: What is home warranty insurance</em> and <em>Maximum amounts covered</em>; <em>Demerit points</em>. Read 17 September 2026. Cover amounts, thresholds and register rules change; check the QBCC's current pages before you rely on any figure here. This is a plain-English guide, not legal or financial advice.</p>
''')

# ---------------------------------------------------------------- R16 · small independent builders
POSTS["r16-independent"] = dict(
    slug="who-are-the-small-independent-builders-on-brisbanes-bayside",
    title="Who are the small independent builders on Brisbane's Bayside?",
    h1="Who are the small independent builders<br>on Brisbane's Bayside?",
    description="What 'small' and 'independent' actually mean when you're choosing a builder, how to find the ones near Wynnum, Manly and the Redlands, what to check, and where Sabre fits.",
    lede="People search for a small, independent builder because they've worked out what they don't want: a display centre, a sales consultant, and a site supervisor running twenty jobs. Here's what the words mean, how to find one on the Bayside, and how to check them.",
    date="2026-09-17", category="Dealing with a builder", image="blog/who-are-the-small-independent-builders-on-brisbanes-bayside.jpg",
    image_alt="A small builder's frame-stage job on a Bayside street, a builder talking with a couple on the footpath",
    image_caption="Illustration in the style of Sabre's story frames. Not a real job or client.",
    card_title="Who are the small independent builders on Brisbane's Bayside?",
    card_blurb="What the words actually mean, how to find the builders near Wynnum and Manly who fit them, the checks that work on any of us, and where Sabre sits.",
    about=["Independent builder", "Small builder", "Brisbane Bayside", "Wynnum", "Manly", "Choosing a builder"],
    related=["what-is-the-qbcc-and-what-to-check-on-a-builders-licence", "what-is-a-knockdown-rebuild-package", "rebuilding-in-wynnum-or-manly"],
    cta="Meet the people who'd build it. Nathan walks your house; Stewart, Frank and the crew build the next one. Same family, same phone number, since 1990.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>A small independent builder on the Bayside is a locally owned building business, usually a family or a couple of partners, that designs and builds a handful of homes at a time in and around Wynnum, Manly, Lota, Capalaba and the Redlands. Independent means not a franchise of a national brand. Small means the person you meet is the person who builds.</p>
        <p>There are more of them than the display villages suggest. To find them: search the QBCC licensee register by suburb, look at the Google map results for &ldquo;builders&rdquo; plus your suburb, and look at who is actually on the fences in your street.</p>
        <p>Then run the same checks on all of them: the licence, the reviews, a recent client's number, and the question of who's on the phone in month four. Sabre is one of them, family-owned in Ransome since 1990, and we'd rather you compared us than took our word.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-it-means">What do &ldquo;small&rdquo; and &ldquo;independent&rdquo; actually mean?</a></li>
          <li><a href="#why-people-want-one">Why do families go looking for one?</a></li>
          <li><a href="#how-to-find">How do you find the ones near you?</a></li>
          <li><a href="#what-to-check">What should you check on any of them?</a></li>
          <li><a href="#trade-offs">What's the honest trade-off?</a></li>
          <li><a href="#sabre">Where does Sabre fit?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-it-means">What do &ldquo;small&rdquo; and &ldquo;independent&rdquo; actually mean?</h2>
      <p>They're the words families use. Builders don't, much. So here's what they mean in practice.</p>
      <p><strong>Independent</strong> means the business is owned by the people running it, not operating under a national brand's name and systems. There's no head office deciding the range, the specification or the price list. The builder decides, with you.</p>
      <p><strong>Small</strong> means the number of jobs running at once is small enough that the owner is on all of them. The builder who quoted your house is the builder who turns up. There isn't a sales layer between you and the person with the hammer.</p>
      <p>Neither word says anything about quality by itself. There are excellent big builders and poor small ones. What the words point at is the <em>shape</em> of the relationship, and that's what people are really searching for.</p>

      <h2 class="h2" id="why-people-want-one">Why do families go looking for one?</h2>
      <p>Usually after a bad experience, or after hearing about one. The pattern is the same:</p>
      <ul class="pts">
        <li><strong>They want the block designed to, not a plan fitted to it.</strong> On a Bayside block with a slope, an aspect and a flood level, that matters. <a href="../what-is-a-knockdown-rebuild-package/">Packages and where they stop suiting people are here.</a></li>
        <li><strong>They want one phone number.</strong> Not a sales consultant, then a contracts person, then a supervisor they've never met.</li>
        <li><strong>They want the person who said it to be the person who does it.</strong></li>
        <li><strong>They want a builder who knows the suburb</strong> &mdash; the overlay, the salt, the storm-tide levels, which streets flood in a king tide.</li>
      </ul>

      <blockquote class="proof">
        <p>&ldquo;Nathan and the gang were excellent during the build. Always around to help or offer suggestions. Would definitely recommend them.&rdquo;</p>
        <cite>Jason Turner &middot; Google review of Sabre Constructions &middot; June 2025. That's the shape people are looking for, described by someone who had it.</cite>
      </blockquote>

      <h2 class="h2" id="how-to-find">How do you find the ones near you?</h2>
      <p>The display villages are on the arterial roads. The small builders are on the fences. Four ways to find them:</p>
      <ol>
        <li><strong>The QBCC licensee register.</strong> Every licensed builder in Queensland is on it, searchable by name and location. It's the only complete list there is.</li>
        <li><strong>Google's map results.</strong> Search &ldquo;builders&rdquo; and your suburb. The map box shows businesses with a Google profile near you, with their reviews. Read all the reviews, not the rating.</li>
        <li><strong>The fences.</strong> Walk the streets you'd want to build in. The builder's sign on a job in your suburb is a builder who already works on your kind of block.</li>
        <li><strong>The neighbours.</strong> A family two streets over who rebuilt three years ago knows more about their builder than any website does. Ask them who they'd use again.</li>
      </ol>

      <h2 class="h2" id="what-to-check">What should you check on any of them?</h2>
      <p>The same things, whether the builder has two jobs or two hundred.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Search the QBCC licensee register to check the history of your builder before you sign the contract on your next repair, renovation or build.&rdquo;</b> Home warranty insurance is compulsory for residential work over $3,300, and the premium forms part of your contract price.</p>
        <cite>Queensland Building and Construction Commission. A small builder is held to exactly the same licence and the same insurance as a national one. Check both, every time. <a href="../what-is-the-qbcc-and-what-to-check-on-a-builders-licence/">How to do it in five minutes is here.</a></cite>
      </blockquote>

      <ol>
        <li><strong>The licence.</strong> Current, right class, same entity as the quote.</li>
        <li><strong>The insurance.</strong> Ask how the home warranty premium appears in the contract.</li>
        <li><strong>The reviews, all of them.</strong> Look for whether people name a person. On Sabre's listing, families name Stewart, Nathan and Frank, and the rating sits at 4.5 from 12 with the one-star review included.</li>
        <li><strong>A recent client's phone number.</strong> Not a testimonial. A number.</li>
        <li><strong>Who's on the phone in month four.</strong> Ask for the name, and how many jobs that person is running.</li>
        <li><strong>How they handle the price after the soil test.</strong> Every builder has an answer. Hear it before you sign.</li>
      </ol>

      <h2 class="h2" id="trade-offs">What's the honest trade-off?</h2>
      <p>There is one, and a fair page says so.</p>
      <p>A small builder builds fewer houses a year, so there may be a wait, and the design stage takes longer than picking a plan from a range. There's no display home to walk through &mdash; you walk through a house they built for someone else, or through your own with a builder who's imagining the next one. And a small business is a small business: it's worth checking the licence history and the insurance, as it is with anyone.</p>
      <p>What you get for that is the thing the search was for. The person who walked your house builds it. The design starts with your block. And the phone number in month four is the same one you rang in month one.</p>

      <h2 class="h2" id="sabre">Where does Sabre fit?</h2>
      <p>We're one of the small independent builders on the Bayside. Family owned and family run since 1990, based at Ransome, building across Wynnum, Manly, Lota, Wakerley, Capalaba, Birkdale, Wellington Point and the Redlands. Stewart founded it, Nathan came through his apprenticeship here and is on site through the build, Frank has supervised jobs here for seventeen years.</p>
      <p>We design to the block, we don't sell packages, and we'd rather you ran every check above on us before you rang. QBCC 15486557. Master Builders Queensland 00352. The reviews are on Google.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>&ldquo;Independent&rdquo; means locally owned, not a franchise. &ldquo;Small&rdquo; means the owner is on every job.</b> Neither word means good by itself.</li>
          <li><b>Find them on the QBCC register, the Google map box, the fences and the neighbours.</b> Not on the arterial roads.</li>
          <li><b>Run the same six checks on every builder,</b> whatever their size: licence, insurance, reviews, a client's number, month four, the soil test.</li>
          <li><b>The trade-off is real:</b> fewer jobs, a wait, no display home. What you get is the person who quoted it building it.</li>
          <li><b>Sabre is one of them.</b> Look us up before you ring.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Is a small builder cheaper than a big one?</p>
          <p>Not necessarily, and anyone who tells you they always are is guessing. A small builder has less overhead in some places and less buying power in others. Compare what's in each quote, line by line, and what moves after the soil test.</p>
        </div>
        <div>
          <p class="q">Is my deposit safe with a small builder?</p>
          <p>The Queensland Home Warranty Scheme covers residential building work over $3,300 regardless of the builder's size, including refunding a deposit if work hasn't started. Check the licence and ask how the premium appears in your contract, as you would with anyone.</p>
        </div>
        <div>
          <p class="q">Do small builders do knockdown rebuilds, or just renovations?</p>
          <p>Both, usually. Ask to see a rebuild they've done in your suburb, and ask who managed the demolition and the asbestos removal on it.</p>
        </div>
        <div>
          <p class="q">How many jobs is &ldquo;small&rdquo;?</p>
          <p>There's no rule. The useful question is whether the owner is on every job, and how many the person supervising yours is running at once. Ask for the number.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission &mdash; <em>Our lists and registers</em> and <em>Queensland Home Warranty Scheme</em>; Sabre Constructions' public Google listing, read 5 September 2026 (4.5 stars from 12 reviews); Sabre's Meet the Team page. This page names no other builder, deliberately &mdash; run the checks on all of us. Read 17 September 2026. Not legal or financial advice.</p>
''')
