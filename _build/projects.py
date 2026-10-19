# Beyond Branding — portfolio content.
# Edit this file, then run:  python3 _build/build.py
# Every project gets its own page at /work/<slug>.html and a card on portfolio.html.
#
# Fields
#   slug        url name (lowercase, hyphens)
#   client      display name
#   industry    short sector label
#   location    optional
#   images      list of (file in /assets, alt text) — first one is the cover
#   filters     which hub filters it appears under (keys of FILTERS below)
#   packages    which pricing categories to pitch on the page (keys of PACKAGES below)
#   services    the services line
#   hook        one-line headline (bold, sales-led)
#   summary     1–2 sentences under the hook
#   result      one line shown on the hub card
#   featured    True = shown as a large case study at the top of the hub
#   story       list of (label, text) sections for the case-study page

WHATSAPP = "19108301588"
SITE = "https://beyondbranding.media"

FILTERS = [
    ("identity",   "Brand Identity"),
    ("packaging",  "Packaging & Product"),
    ("web",        "Websites & E-commerce"),
    ("campaigns",  "Campaigns & Social"),
    ("events",     "Exhibitions & Events"),
    ("signage",    "Retail & Signage"),
    ("collateral", "Brochures & Collateral"),
]

# Mirrors /packages-global — 'id' is the anchor on that page.
PACKAGES = {
    "identity":   dict(id="identity",   name="Brand Identity & Logo",          start="$500",  incl="Logo, type system, colour and guidelines"),
    "packaging":  dict(id="packaging",  name="Packaging Design",               start="$400",  incl="Single SKU to full ranges, print-ready"),
    "collateral": dict(id="collateral", name="Brochure & Sales Collateral",    start="$400",  incl="Catalogues, brochures and sales decks"),
    "events":     dict(id="events",     name="Event & Exhibition Branding",    start="$800",  incl="Booth graphics, stage and conference systems"),
    "signage":    dict(id="signage",    name="Retail & Environmental Signage", start="$500",  incl="Store signage, wayfinding, counter branding"),
    "campaigns":  dict(id="campaigns",  name="Print & Digital Ad Campaigns",   start="$150",  incl="Single creatives to full campaign sets"),
    "social":     dict(id="social",     name="Social Media Content Systems",   start="$400",  incl="Template systems and monthly retainers"),
    "web":        dict(id="web",        name="Digital & Web Design",           start="$800",  incl="Landing pages, full websites, e-commerce"),
}

PROJECTS = [
    dict(
        slug="dubai-media-office", client="Dubai Media Office", industry="Government", location="Dubai, UAE",
        images=[("dubai-media-office-stage.webp", "Dubai Government Media Office annual forum stage branding"),
                ("dubai-media-office-instagram.webp", "Dubai Media Office Instagram content")],
        filters=["events", "campaigns"], packages=["events", "social"],
        services="Social Content · Stage Branding · Design Collaterals",
        hook="Designing for millions means designing responsibly.",
        summary="When communication represents a government institution, clarity becomes more important than creativity.",
        result="Bilingual campaign, stage and social systems that held together across dozens of touchpoints.",
        featured=True,
        story=[
            ("The Challenge", "Every announcement, campaign and event asset needed to communicate instantly across different languages, audiences and platforms—while staying consistent with an identity that was already established, not ours to reinvent."),
            ("The Thinking", "The temptation with public-sector work is to make it interesting. We resisted that. The real work was asking what a viewer needed to understand in the two seconds they'd actually give it."),
            ("The Solution", "Bilingual campaign systems, stage branding and social templates built around a strict hierarchy—one idea per frame, repeated until it felt familiar rather than novel."),
            ("The Outcome", "Materials that held together across dozens of touchpoints and multiple teams, without a single style guide meeting."),
            ("What I Learned", "Good public communication isn't remembered because it's beautiful. It's remembered because people never had to think twice."),
        ],
    ),
    dict(
        slug="marriott-indore", client="Marriott Indore", industry="Hospitality", location="Indore, India",
        images=[("marriott-indore-hamper.webp", "Marriott Indore festive hamper packaging")],
        filters=["packaging", "campaigns"], packages=["packaging", "campaigns"],
        services="Packaging · Campaign Design · Guest Collateral",
        hook="Hospitality doesn't end at the hotel entrance.",
        summary="During the pandemic, the guest experience had to travel home with them.",
        result="Takeaway and festive packaging that carried the in-hotel Marriott experience home.",
        featured=True,
        story=[
            ("The Challenge", "Luxury hotels needed to deliver the same level of care through takeaway packaging, festive hampers and communication that guests would normally only experience inside the property."),
            ("The Thinking", "The challenge wasn't designing packaging. It was preserving the feeling of Marriott outside the hotel—a much harder brief than it sounds."),
            ("The Solution", "Every detail, from materials to typography, was considered so the experience remained recognisably Marriott the moment it left the building."),
            ("The Outcome", "Packaging and collateral that guests associated with the same quality as the in-hotel experience, delivered through a fraction of the usual touchpoints."),
            ("What I Learned", "Premium brands don't become memorable because they look expensive. They become memorable because every touchpoint feels intentional."),
        ],
    ),
    dict(
        slug="valdaria", client="Valdaria", industry="Luxury Retail",
        images=[("valdaria-exhibition-booth.webp", "Valdaria premium suiting trade exhibition booth")],
        filters=["identity", "events"], packages=["identity", "events"],
        services="Brand Identity · Exhibition Design · Event Graphics",
        hook="Building a brand before building awareness.",
        summary="Valdaria wasn't looking for another logo. It needed an identity that could stand beside established luxury suiting brands.",
        result="A new suiting brand that read as established from day one.",
        featured=True,
        story=[
            ("The Challenge", "A brand with no market awareness, entering a category where competitors had decades of trust already built in."),
            ("The Thinking", "Building a brand before building awareness meant every asset had to do the work a reputation usually does."),
            ("The Solution", "The work extended far beyond visual identity—exhibition spaces, printed material and fabric presentation, all designed to create confidence before the first conversation began."),
            ("The Outcome", "A presence that read as established from day one, in a category that punishes anything that looks new."),
            ("What I Learned", "Luxury isn't decoration. Luxury is restraint."),
        ],
    ),
    dict(
        slug="doubletree-by-hilton", client="DoubleTree by Hilton", industry="Hospitality",
        images=[("doubletree-hilton-signage.webp", "DoubleTree by Hilton signage")],
        filters=["signage"], packages=["signage"],
        services="Signage Design · Production Artwork",
        hook="A global standard, executed locally.",
        summary="Property signage designed to sit precisely inside DoubleTree by Hilton's brand standards while working for the space it lives in.",
        result="Signage that reads as unmistakably DoubleTree, built to global brand standards.",
        story=[
            ("The Challenge", "Global hotel brands come with strict standards. The signage had to feel considered for this property while staying exactly inside the system guests already recognise."),
            ("The Approach", "We worked from the brand's own rules outward—typography, spacing, colour, materials and placement—so every sign felt native to the brand, not adapted from it."),
            ("Delivered", "Signage designs and production-ready artwork for the property."),
        ],
    ),
    dict(
        slug="manek", client="Manek", industry="Luxury Retail",
        images=[("manek-brochure-bag.webp", "Manek luxury shirting brand collateral")],
        filters=["identity", "packaging", "collateral"], packages=["identity", "collateral"],
        services="Brand Identity · Packaging · Sales Collateral",
        hook="Trust begins before the fabric is touched.",
        summary="When customers invest in premium shirting, their first impression often happens long before they experience the product itself.",
        result="One continuous brand experience from shelf to store to sale.",
        featured=True,
        story=[
            ("The Challenge", "Trust needed to begin before the product was in anyone's hands—through packaging, catalogues and sales collateral alone."),
            ("The Thinking", "Branding doesn't begin with the product. It begins with expectation. We designed for the moment before the sale, not the moment of it."),
            ("The Solution", "Packaging, catalogues, sales collateral and exhibition material became part of one continuous experience, rather than separate deliverables handled in isolation."),
            ("The Outcome", "A retail presence that carried the same confidence at every stage, from shelf to store to sale."),
            ("What I Learned", "The first impression is rarely the product itself. It's everything that surrounds it."),
        ],
    ),
    dict(
        slug="aeroengines-america", client="Aeroengines America", industry="Aviation", location="USA",
        images=[("aeroengines-america-booth.webp", "Aeroengines America exhibition booth")],
        filters=["events"], packages=["events"],
        services="Booth Graphics · Exhibition Design",
        hook="Technical credibility, readable from across the hall.",
        summary="Trade-show booth graphics for an aviation engine business, built to be understood by a specialist audience in seconds.",
        result="A booth that signals capability from a distance, before anyone steps in.",
        story=[
            ("The Challenge", "Aviation buyers walk trade floors full of near-identical booths. This one needed to signal capability and trust from a distance, before anyone stepped inside."),
            ("The Approach", "A restrained, high-contrast system: one clear message at eye level, technical detail saved for closer range, and brand colour used with discipline."),
            ("Delivered", "Booth graphics and exhibition artwork, ready for the fabrication partner."),
        ],
    ),
    dict(
        slug="indian-kawfee-co", client="Indian Kawfee Co.", industry="Food & Beverage",
        images=[("indian-kawfee-jar.webp", "Indian Kawfee Company premium coffee packaging")],
        filters=["identity", "packaging"], packages=["identity", "packaging"],
        services="Brand Identity · Packaging Design",
        hook="Packaging should tell a story before the first sip.",
        summary="Coffee isn't only judged by taste. It's judged on the shelf, in the seconds before anyone tastes anything.",
        result="Shelf packaging that stands out without shouting—and feels authentically Indian.",
        featured=True,
        story=[
            ("The Challenge", "Celebrate Indian coffee culture without leaning on the clichés the category usually reaches for."),
            ("The Thinking", "The objective wasn't louder packaging. It was packaging people wanted to pick up—a quieter, harder goal to design for."),
            ("The Solution", "Every visual decision balanced authenticity with contemporary retail appeal, so the identity felt rooted without feeling dated."),
            ("The Outcome", "Packaging that stood out on shelf without shouting, and that customers described as feeling authentically Indian."),
            ("What I Learned", "Story sells before flavour does. Give people something to believe before they taste anything."),
        ],
    ),
    dict(
        slug="xess", client="XESS", industry="Energy Storage",
        images=[("xess-conference-stage.webp", "XESS energy storage conference presentation")],
        filters=["events"], packages=["events"],
        services="Stage Design · Presentation Design · Event Graphics",
        hook="Making energy storage easy to follow from the back row.",
        summary="Conference stage and presentation design for XESS, an energy storage company.",
        result="Stage visuals that let a technical story land with a mixed audience.",
        story=[
            ("The Challenge", "Energy storage is technical by nature. On stage, complex ideas had to land with a mixed room of investors, partners and engineers."),
            ("The Approach", "Stage and presentation visuals built around one idea per screen, large type and clear data, so the speaker carried the story and the design supported it."),
            ("Delivered", "Stage backdrop, presentation design and supporting event graphics."),
        ],
    ),
    dict(
        slug="dhanraj-jain-jewellers", client="Dhanraj Jain Jewellers", industry="Jewellery",
        images=[("dhanraj-jain-jewellers-counter.webp", "Dhanraj Jain Jewellers store counter branding")],
        filters=["signage", "identity"], packages=["signage", "identity"],
        services="Retail Branding · Counter Design · In-store Graphics",
        hook="Where trust is built across the counter.",
        summary="In-store branding for a jewellery house, designed around the moment customers decide.",
        result="A counter that communicates heritage as clearly as the pieces in the case.",
        story=[
            ("The Challenge", "In jewellery, the store is part of the promise. The counter had to communicate heritage and craftsmanship as clearly as the pieces on display."),
            ("The Approach", "Counter branding and in-store graphics in a refined palette with careful material choices—premium, without ever competing with the jewellery."),
            ("Delivered", "Counter branding, in-store graphics and production artwork."),
        ],
    ),
    dict(
        slug="colorado-windows-direct", client="Colorado Windows Direct", industry="Home Improvement", location="USA",
        images=[("colorado-windows-newspaper-ad.webp", "Colorado Windows Direct print advertising campaign")],
        filters=["campaigns"], packages=["campaigns"],
        services="Print Advertising · Campaign Design",
        hook="Print that earns attention on a crowded page.",
        summary="Newspaper advertising for a home windows company, designed to be noticed and acted on.",
        result="A headline-first ad that makes the offer obvious and the call easy.",
        story=[
            ("The Challenge", "Newspaper readers skim. The ad had to stop them, make the offer obvious and make picking up the phone feel easy—all inside a fixed space."),
            ("The Approach", "A headline-first layout, one clear offer and a prominent call to action, with supporting detail kept deliberately quiet."),
            ("Delivered", "Print advertising artwork, ready for publication."),
        ],
    ),
    dict(
        slug="aiolec", client="Aiolec", industry="Technology", location="London, UK",
        images=[("aiolec-brochure-laptop.webp", "Aiolec London brochure design")],
        filters=["collateral"], packages=["collateral", "web"],
        services="Brochure Design · Sales Collateral",
        hook="A brochure that sells before the meeting starts.",
        summary="Brochure design for Aiolec in London, built to explain the offer clearly and look as premium as the product.",
        result="A brochure where every spread answers one buyer question.",
        story=[
            ("The Challenge", "Technical products often get brochures written only for engineers. This one had to work just as well for the people signing off the budget."),
            ("The Approach", "A clear page-by-page structure, generous space and confident product imagery, so each spread answered one question and moved the reader to the next."),
            ("Delivered", "Brochure design in print and digital formats."),
        ],
    ),
    dict(
        slug="overcmr", client="Overcmr", industry="Sports Equipment", location="India",
        images=[("overcmr-paddles-display.webp", "OverCMR pickleball paddle product launch display")],
        filters=["packaging"], packages=["packaging"],
        services="Product Graphics · Range Design · Launch Display",
        hook="Paddles designed to be picked up first.",
        summary="Pickleball paddle graphics and launch display for Overcmr, a fitness gear brand.",
        result="A paddle range that reads as distinct on the rack and on court.",
        story=[
            ("The Challenge", "Pickleball is crowded with paddles that look the same. Overcmr needed a range that stood apart on the rack and on court."),
            ("The Approach", "Each paddle—Invictus, Vanguard and Augustus—got its own character within one family, tied together by a consistent structure and finish, then shown on a launch display built for retail."),
            ("Delivered", "Paddle graphics for the range and launch display design."),
        ],
    ),
    dict(
        slug="stanfords-real-estate", client="Stanford's Real Estate", industry="Real Estate",
        images=[("stanfords-real-estate-poolside.webp", "Stanford's Real Estate poolside campaign")],
        filters=["campaigns"], packages=["campaigns", "social"],
        services="Campaign Design · Property Advertising",
        hook="Selling the lifestyle, not the square footage.",
        summary="A campaign for Stanford's Real Estate that leads with how a home feels to live in.",
        result="A lifestyle-led campaign buyers remember after the listings blur together.",
        story=[
            ("The Challenge", "Property ads tend to look interchangeable—specs, floor plans, price. The campaign needed an emotional hook buyers would remember."),
            ("The Approach", "Lifestyle-led imagery anchored on the poolside moment, with concise copy and a clean layout that let the setting do the selling."),
            ("Delivered", "Campaign creative for print and digital placements."),
        ],
    ),
    dict(
        slug="pride-of-cows", client="Pride of Cows", industry="Premium Dairy",
        images=[("pride-of-cows-retail-signage.webp", "Pride of Cows retail signage")],
        filters=["signage"], packages=["signage"],
        services="Retail Signage · Point of Sale",
        hook="Premium dairy deserves premium shelf presence.",
        summary="Retail signage for Pride of Cows, designed to stand out at the point of purchase.",
        result="Point-of-sale signage that communicates quality and freshness at a glance.",
        story=[
            ("The Challenge", "In-store, a premium brand has seconds to justify its price. The signage had to communicate quality and freshness at a glance."),
            ("The Approach", "Clean signage built on the brand's existing identity, with a single clear message for each placement."),
            ("Delivered", "Retail signage and point-of-sale artwork."),
        ],
    ),
    dict(
        slug="gowardhan-ghee", client="Gowardhan Ghee", industry="FMCG · E-commerce",
        images=[("gowardhan-ghee-amazon.webp", "Gowardhan Ghee Amazon listing design")],
        filters=["web", "campaigns"], packages=["web", "campaigns"],
        services="Amazon Listing Design · E-commerce Creative",
        hook="The shelf is now a product page.",
        summary="Amazon listing design for Gowardhan Ghee, built to turn scrollers into buyers.",
        result="Listing images that answer buyer questions in the order they ask them.",
        story=[
            ("The Challenge", "On Amazon, shoppers compare products in seconds with nothing but images to go on. The listing had to do the job of a salesperson."),
            ("The Approach", "A listing image set that answers buyer questions in order—what it is, why it's better, how it's made, what's inside—with consistent brand styling throughout."),
            ("Delivered", "Amazon listing image set and e-commerce creative."),
        ],
    ),
    dict(
        slug="myaccessiblehome", client="MyAccessibleHome", industry="Home Accessibility",
        images=[("myaccessiblehome-website.webp", "MyAccessibleHome website design")],
        filters=["web"], packages=["web"],
        services="Website Design · UX",
        hook="A website that practises what it preaches.",
        summary="Website design for MyAccessibleHome, a home accessibility business.",
        result="A site where clarity and legibility were requirements, not extras.",
        story=[
            ("The Challenge", "A brand about accessibility can't have a website that's hard to use. Clarity and legibility were requirements, not nice-to-haves."),
            ("The Approach", "Clear structure, readable type, strong contrast and simple navigation, so every visitor could find what they needed quickly."),
            ("Delivered", "Website design across key pages, desktop and mobile."),
        ],
    ),
]
