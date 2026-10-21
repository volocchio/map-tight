# MapTight border context pack

Version: 2026-10-19

Curated short-form context for UI import. Keep copy neutral: borders are historical/political artifacts, not destiny.

## Implementation notes

- CPI values use Transparency International CPI 2025 where available; non-sovereign states/regions and microstates not covered reliably are null.
- Entries are intentionally short for app UI; sources are included for later expansion and QA.

- Load `border_context_pack.json` as external data later instead of embedding in `index.html`.
- Match entries by stable `id` values already used in app data/presets where possible.
- In UI, show 3–5 `border_history` bullets plus tags; keep sources collapsed behind a “sources” link.
- `corruption_context` is null for regions, U.S. states, and entities without reliable CPI coverage.
- Treat this as v1: source-check before adding casualty numbers, contested-boundary claims, or sensitive map labels.

## France (`france`)

**Type:** country

**Border history**
- 843 Treaty of Verdun split Charlemagne’s empire; western Francia became the long ancestor of France, not a neat modern nation-state.
- 1648 Peace of Westphalia and 1659 Treaty of the Pyrenees helped fix eastern/southern frontiers through dynastic war and diplomacy.
- 1871–1945 Alsace-Lorraine shifted between France and Germany after wars; the border there carries memories of annexation, occupation, and return.
- Post-1945 European integration softened many hard borders via the EU and Schengen, while overseas territories keep France globally dispersed.

**Human-cost tags:** empire, treaty, war, annexation, colonialism

**Government context:** Unitary semi-presidential republic; president and parliament share power, with strong central state traditions.

**Languages:** French is official; regional languages include Breton, Occitan, Basque, Corsican, Alsatian/Germanic varieties, Catalan, and overseas creoles.

**Corruption context:** 66/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/France
- https://history.state.gov/countries/france
- https://www.elysee.fr/en/french-presidency/the-institutions-of-the-fifth-republic
- https://www.transparency.org/en/cpi/2025

## Germany (`germany`)

**Type:** country

**Border history**
- 1871 German unification joined many states under Prussian leadership after wars with Denmark, Austria, and France.
- 1919 Treaty of Versailles redrew borders after World War I, transferring territories and creating lasting grievances exploited by extremists.
- 1945 defeat of Nazi Germany led to occupation zones; 1949 created two German states, divided by Cold War frontiers.
- 1990 reunification settled postwar borders, including recognition of the Oder–Neisse line with Poland.

**Human-cost tags:** war, treaty, partition, ethnic cleansing, empire

**Government context:** Federal parliamentary republic; chancellor leads government, president is largely ceremonial, Länder retain major powers.

**Languages:** German is official; recognized minority languages include Danish, Sorbian, Frisian, Romani, plus regional dialect continua such as Low German and Bavarian.

**Corruption context:** 77/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Germany
- https://history.state.gov/countries/germany
- https://www.bundesregierung.de/breg-en/federal-government
- https://www.transparency.org/en/cpi/2025

## Luxembourg (`luxembourg`)

**Type:** country

**Border history**
- 1839 Treaty of London split Luxembourg, ceding western Luxembourg to Belgium and leaving a smaller grand duchy.
- 1867 Treaty of London confirmed Luxembourg’s neutrality and independence after a crisis between France and Prussia.
- World Wars I and II brought occupation despite neutrality, shaping a strong postwar pro-European identity.
- Modern borders are small but deeply cross-border: daily commuting ties Luxembourg to Belgium, France, and Germany.

**Human-cost tags:** treaty, occupation, great-power diplomacy, microstate

**Government context:** Constitutional monarchy and parliamentary democracy; grand duke is head of state, elected government exercises executive power.

**Languages:** Luxembourgish is national language; French and German are administrative/judicial languages; multilingualism is normal in public life.

**Corruption context:** 78/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Luxembourg
- https://history.state.gov/countries/luxembourg
- https://gouvernement.lu/en/systeme-politique.html
- https://www.transparency.org/en/cpi/2025

## South Africa (`south-africa`)

**Type:** country

**Border history**
- 1652 Dutch settlement at the Cape began settler expansion onto Khoekhoe, San, and later other African lands.
- 1806 British control of the Cape and 19th-century frontier wars reshaped landholding through conquest and dispossession.
- 1910 Union of South Africa joined British colonies and former Boer republics, excluding most Black South Africans from power.
- 1948–1994 apartheid hardened internal boundaries through Bantustans, pass laws, and forced removals rather than changing external borders.

**Human-cost tags:** colonialism, indigenous displacement, apartheid, conquest, settler colonialism

**Government context:** Constitutional parliamentary republic; president is elected by the National Assembly; provinces have devolved powers.

**Languages:** 12 official languages including Zulu, Xhosa, Afrikaans, English, Sepedi, Setswana, Sesotho, Xitsonga, siSwati, Tshivenda, Ndebele, and South African Sign Language.

**Corruption context:** 41/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/South-Africa
- https://www.gov.za/about-sa/history
- https://www.gov.za/about-sa/south-africas-people
- https://www.transparency.org/en/cpi/2025

## United States (`united-states`)

**Type:** country

**Border history**
- 1776–1783 independence from Britain created a republic on Atlantic seaboard lands already inhabited by Native nations.
- 1803 Louisiana Purchase and later treaties/purchases vastly expanded U.S. claims, often ahead of actual control.
- 1846–1848 U.S.–Mexico War and Treaty of Guadalupe Hidalgo transferred huge western territories to the United States.
- 19th-century removal, reservations, allotment, and military campaigns displaced Indigenous peoples while survey lines made state borders look deceptively clean.

**Human-cost tags:** indigenous displacement, treaty, conquest, settler colonialism, survey line

**Government context:** Federal presidential constitutional republic; powers split among federal branches and states.

**Languages:** No federal official language; English dominates nationally, Spanish is widely spoken, and many Indigenous and immigrant languages remain important.

**Corruption context:** 64/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/United-States
- https://history.state.gov/milestones/1830-1860/indian-treaties
- https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo
- https://www.transparency.org/en/cpi/2025

## United Kingdom (`united-kingdom`)

**Type:** country

**Border history**
- 1536–1543 Laws in Wales Acts incorporated Wales into the English legal state.
- 1707 Acts of Union joined England/Wales and Scotland into Great Britain through parliamentary union, not conquest alone.
- 1801 union with Ireland created the United Kingdom; 1921 partition left Northern Ireland in the UK and most of Ireland outside it.
- Late-20th-century devolution gave Scotland, Wales, and Northern Ireland elected institutions without dissolving the UK state.

**Human-cost tags:** union, partition, empire, devolution, treaty

**Government context:** Constitutional monarchy with parliamentary government; devolved administrations in Scotland, Wales, and Northern Ireland.

**Languages:** English dominates; Welsh has strong official status in Wales; Scottish Gaelic, Scots, Irish, Ulster Scots, and Cornish have varying recognition.

**Corruption context:** 70/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/United-Kingdom
- https://www.parliament.uk/about/living-heritage/evolutionofparliament/legislativescrutiny/acts-of-union-1707/
- https://www.gov.uk/government/organisations/northern-ireland-office
- https://www.transparency.org/en/cpi/2025

## India (`india`)

**Type:** country

**Border history**
- 1757–1858 East India Company rule expanded through war, alliance, and annexation before direct British Crown rule.
- 1947 Partition created India and Pakistan along hurried lines, causing mass displacement and communal violence.
- 1962 Sino-Indian War left disputed Himalayan borders unresolved in areas such as Aksai Chin and Arunachal Pradesh.
- 1971 Bangladesh’s independence changed India’s eastern neighborhood; the 2015 India–Bangladesh land-boundary agreement cleaned up enclaves peacefully.

**Human-cost tags:** colonialism, partition, border dispute, war, treaty

**Government context:** Federal parliamentary republic; prime minister leads government, president is constitutional head of state.

**Languages:** Hindi and English serve Union-level functions; constitution recognizes 22 scheduled languages, with many state and regional languages.

**Corruption context:** 39/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/India
- https://history.state.gov/milestones/1945-1952/india-pakistan
- https://www.mea.gov.in/bilateral-documents.htm?dtl/25160/IndiaBangladesh+Land+Boundary+Agreement
- https://www.transparency.org/en/cpi/2025

## Bangladesh (`bangladesh`)

**Type:** country

**Border history**
- 1947 Partition made East Bengal/East Pakistan part of Pakistan despite being separated from West Pakistan by India.
- 1952 Language Movement made Bengali identity politically central and is remembered as a foundational struggle.
- 1971 Bangladesh Liberation War created an independent state after severe violence and mass displacement.
- 2015 India–Bangladesh land-boundary agreement exchanged enclaves and simplified one of the world’s strangest border patchworks.

**Human-cost tags:** partition, language movement, civil war, mass displacement, treaty

**Government context:** Parliamentary republic; prime minister heads government, president is largely ceremonial; politics has been marked by intense party rivalry.

**Languages:** Bengali/Bangla is official and central to national identity; Indigenous and minority languages are spoken in the Chittagong Hill Tracts and elsewhere.

**Corruption context:** 24/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Bangladesh
- https://history.state.gov/milestones/1969-1976/south-asia
- https://www.unesco.org/en/days/mother-language
- https://www.transparency.org/en/cpi/2025

## Wyoming (`wyoming`)

**Type:** state

**Border history**
- 1868 Wyoming Territory was carved from parts of Dakota, Idaho, and Utah territories with straight survey-line borders.
- 1868 Fort Laramie Treaty recognized Lakota-related lands nearby, but U.S. expansion and later policy steadily constrained Native land bases.
- 1869 Wyoming granted women suffrage while still a territory, shaping its political identity before statehood.
- 1890 Wyoming became the 44th U.S. state with borders largely inherited from federal territorial surveying.

**Human-cost tags:** survey line, indigenous displacement, treaty, territorial administration

**Government context:** U.S. state with elected governor, bicameral legislature, and judiciary under the U.S. federal system.

**Languages:** English dominates; Native languages with regional ties include Arapaho and Shoshone, alongside Spanish and other community languages.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.britannica.com/place/Wyoming-state
- https://www.wyohistory.org/encyclopedia/wyoming-territory
- https://www.archives.gov/milestone-documents/fort-laramie-treaty
- https://www.census.gov/quickfacts/WY

## Tennessee (`tennessee`)

**Type:** state

**Border history**
- 1796 Tennessee became the 16th U.S. state from the Southwest Territory, on lands long inhabited by Cherokee, Chickasaw, and other peoples.
- 1818 Jackson Purchase extended western Tennessee claims after Chickasaw cession under U.S. pressure.
- 1830s Indian Removal forced many Cherokee and other Native people from the region toward Indian Territory.
- 1861–1865 Civil War split Tennessee politically and militarily; it was a major borderland between Union and Confederacy.

**Human-cost tags:** indigenous displacement, treaty, civil war, settler colonialism

**Government context:** U.S. state with elected governor, bicameral General Assembly, and judiciary under the U.S. federal system.

**Languages:** English dominates; Appalachian and Southern dialects are culturally important; Spanish and Indigenous heritage languages are present.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.britannica.com/place/Tennessee
- https://tennesseeencyclopedia.net/entries/jackson-purchase/
- https://www.nps.gov/trte/index.htm
- https://www.census.gov/quickfacts/TN

## Africa (`africa`)

**Type:** region

**Border history**
- Precolonial Africa included empires, kingdoms, city-states, pastoral ranges, and trade zones rather than one border logic.
- 1884–1885 Berlin Conference symbolized European partition claims, mostly without African consent.
- 1950s–1970s decolonization kept many colonial borders under the Organization of African Unity principle of inherited frontiers to avoid wider wars.
- Several borders remain politically sensitive where colonial lines cut through ethnic, linguistic, pastoral, or ecological regions.

**Human-cost tags:** colonialism, partition, empire, indigenous sovereignty, arbitrary borders

**Government context:** Continental region, not a single government; the African Union coordinates among sovereign states.

**Languages:** Extremely multilingual: Niger-Congo, Afro-Asiatic, Nilo-Saharan, Khoisan families, Arabic, Swahili, Hausa, Amharic, and colonial languages such as English, French, Portuguese.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.britannica.com/place/Africa
- https://au.int/en/overview
- https://history.state.gov/milestones/1880-1914/berlin-conference
- https://www.un.org/africarenewal/magazine/may-2020/silencing-guns-africa

## Europe (`europe`)

**Type:** region

**Border history**
- 1648 Peace of Westphalia is often treated as a milestone in state sovereignty, though Europe’s borders kept shifting violently.
- 1815 Congress of Vienna redrew post-Napoleonic Europe around balance-of-power politics.
- 1919–1923 post-World War I settlements created or restored states while planting minority and border disputes.
- Post-1945 and post-1989 integration, decolonization, and state breakups made Europe both border-softening and border-making.

**Human-cost tags:** war, treaty, empire, partition, integration

**Government context:** Region, not a single state; the European Union is a supranational polity for many, but not all, European countries.

**Languages:** Indo-European languages dominate, with Uralic, Turkic, Basque, Maltese, Romani, and many minority/regional languages.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.britannica.com/place/Europe
- https://european-union.europa.eu/principles-countries-history/history-eu_en
- https://history.state.gov/milestones/1784-1800/congress-of-vienna
- https://www.coe.int/en/web/minorities

## Asia (`asia`)

**Type:** region

**Border history**
- Asian borders reflect ancient empires and trade zones, plus modern imperial, colonial, and Cold War lines.
- 19th–20th-century Russian, British, French, Dutch, Japanese, Qing/Republican/PRC, Ottoman, and other imperial projects left layered claims.
- 1945–1975 decolonization and Cold War wars created new states and divided states, including Korea, Vietnam for a time, India/Pakistan, and others.
- Some of the world’s most militarized borders remain in Asia, including the Korean DMZ and parts of the India–Pakistan and India–China frontiers.

**Human-cost tags:** empire, colonialism, partition, cold war, border dispute

**Government context:** Region, not a single government; includes republics, monarchies, one-party states, federations, and contested polities.

**Languages:** World’s largest linguistic diversity: Sino-Tibetan, Indo-European, Austronesian, Dravidian, Turkic, Japonic, Koreanic, Semitic, Tai-Kadai and many others.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.britannica.com/place/Asia
- https://www.unescap.org/about/member-states
- https://history.state.gov/milestones/1945-1952/asia-and-africa
- https://www.cia.gov/the-world-factbook/

## North America (`north-america`)

**Type:** region

**Border history**
- Indigenous nations and trade networks long predated European empires and modern borders.
- 1492 onward Spanish, French, British, Dutch, and later U.S. expansion layered colonial claims over Native sovereignty.
- 1783, 1818, 1848, and 1853 treaties helped fix U.S. borders with Britain/Canada and Mexico after war, purchase, and diplomacy.
- Caribbean and Central American borders often reflect colonization, plantation economies, intervention, and independence movements.

**Human-cost tags:** indigenous displacement, colonialism, treaty, conquest, plantation slavery

**Government context:** Region, not a single government; includes sovereign states, territories, federations, monarchies, and dependencies.

**Languages:** English, Spanish, and French are dominant state languages; Indigenous, creole, and immigrant languages remain central in many communities.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.britannica.com/place/North-America
- https://www.britannica.com/event/Louisiana-Purchase
- https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo
- https://www.oas.org/en/member_states/default.asp

## South America (`south-america`)

**Type:** region

**Border history**
- 1494 Treaty of Tordesillas framed Iberian claims, later producing broad Portuguese Brazil vs Spanish America patterns.
- 1810s–1820s independence wars broke Spanish and Portuguese imperial rule but did not restore Indigenous sovereignty.
- 19th-century wars such as the War of the Pacific and Paraguayan War reshaped borders with major human costs.
- Amazonian and Andean borders often followed colonial claims, river surveys, rubber/frontier economies, and later arbitration.

**Human-cost tags:** colonialism, empire, war, indigenous displacement, arbitration

**Government context:** Region, not a single government; most states are presidential republics, with varied federal/unitary systems.

**Languages:** Spanish and Portuguese dominate state life; Quechua, Aymara, Guarani and many Amazonian/Indigenous languages remain important.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.britannica.com/place/South-America
- https://www.britannica.com/event/Treaty-of-Tordesillas
- https://www.britannica.com/event/War-of-the-Pacific
- https://www.oas.org/en/member_states/default.asp

## Antarctica (`antarctica`)

**Type:** region

**Border history**
- 1820s sightings and landings opened an era of exploration rather than Indigenous displacement; Antarctica had no native human population.
- 1908–1940s several states announced sector claims, many overlapping or unrecognized.
- 1959 Antarctic Treaty froze sovereignty disputes and reserved the continent for peaceful scientific cooperation.
- 1991 Madrid Protocol banned mineral resource activity except scientific research, reinforcing Antarctica as a governed commons rather than normal territory.

**Human-cost tags:** sovereignty claims, treaty, scientific commons, resource governance

**Government context:** No sovereign government; Antarctic Treaty System governs activities and freezes territorial-claim disputes.

**Languages:** No native language community; station languages follow national programs, especially English, Spanish, Russian, French, Chinese, and others.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.ats.aq/e/antarctictreaty.html
- https://www.ats.aq/e/protocol.html
- https://www.britannica.com/place/Antarctica
- https://www.nsf.gov/geo/opp/antarct/anttrty.jsp

## Middle East (`middle-east`)

**Type:** region

**Border history**
- Ottoman imperial administration shaped much of the region before World War I, but borders were often provincial and flexible.
- 1916 Sykes–Picot and postwar mandates helped carve British and French zones, shaping Iraq, Syria, Lebanon, Jordan, and Palestine/Israel contexts.
- 1948 creation of Israel and the Arab–Israeli war produced armistice lines, refugee crises, and unresolved sovereignty disputes.
- Oil concessions, dynastic states, wars, and external intervention have repeatedly hardened or contested borders, especially in the Gulf and Levant.

**Human-cost tags:** empire, mandate, partition, refugees, war

**Government context:** Region, not a single government; includes monarchies, republics, occupied/disputed territories, and fragile states.

**Languages:** Arabic is most widespread; Persian, Turkish, Hebrew, Kurdish, Armenian, Aramaic/Syriac varieties and many minority languages are significant.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.britannica.com/place/Middle-East
- https://history.state.gov/milestones/1914-1920/mandate-system
- https://www.un.org/unispal/history/
- https://www.cia.gov/the-world-factbook/

## Brazil (`brazil`)

**Type:** country

**Border history**
- 1494 Treaty of Tordesillas nominally split Iberian claims; Portuguese Brazil later expanded far west beyond that line.
- Colonial bandeirante expeditions, missions, slavery, and frontier wars pushed Portuguese control into Indigenous territories.
- 1822 independence kept Brazil territorially unified under a monarchy, unlike Spanish America’s fragmentation.
- 1903 Treaty of Petrópolis transferred Acre from Bolivia to Brazil after conflict tied to rubber-frontier settlement.

**Human-cost tags:** colonialism, indigenous displacement, slavery, treaty, frontier war

**Government context:** Federal presidential republic with states and municipalities under a 1988 constitution.

**Languages:** Portuguese is official; many Indigenous languages and immigrant-community languages survive, though under pressure.

**Corruption context:** 35/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Brazil
- https://history.state.gov/countries/brazil
- https://www.gov.br/planalto/en/follow-the-government/constitution
- https://www.transparency.org/en/cpi/2025

## Nigeria (`nigeria`)

**Type:** country

**Border history**
- Precolonial region included Hausa city-states, Kanem-Bornu links, Yoruba states, Igbo communities, Benin, Sokoto Caliphate, and many others.
- 1914 British amalgamation joined Northern and Southern Nigeria for colonial administration, creating a large state with deep regional diversity.
- 1960 independence kept colonial borders; federalism became a tool for managing ethnic, regional, and religious complexity.
- 1967–1970 Biafra war followed attempted secession and caused catastrophic civilian suffering, especially through famine.

**Human-cost tags:** colonialism, amalgamation, civil war, federalism, resource politics

**Government context:** Federal presidential republic; 36 states plus Federal Capital Territory.

**Languages:** English is official; Hausa, Yoruba, Igbo, Fulfulde, Kanuri, Tiv, Ibibio and hundreds of other languages are spoken.

**Corruption context:** 26/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Nigeria
- https://history.state.gov/countries/nigeria
- https://www.britannica.com/event/Nigerian-civil-war
- https://www.transparency.org/en/cpi/2025

## Japan (`japan`)

**Type:** country

**Border history**
- 1868 Meiji Restoration centralized state power and accelerated modern border-making from a feudal order.
- 1895 Treaty of Shimonoseki after war with Qing China gave Japan Taiwan and influence over Korea, beginning major overseas empire.
- 1905–1910 Japan expanded into Korea and southern Sakhalin; empire-building was tied to coercion and war.
- 1945 defeat ended the empire; postwar borders left disputes over the Kuril/Northern Territories, Takeshima/Dokdo, and Senkaku/Diaoyu.

**Human-cost tags:** empire, war, annexation, occupation, border dispute

**Government context:** Constitutional monarchy with parliamentary cabinet government; emperor is symbolic head of state.

**Languages:** Japanese is dominant; Ryukyuan and Ainu languages have cultural recognition and revitalization efforts.

**Corruption context:** 71/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Japan
- https://history.state.gov/countries/japan
- https://japan.kantei.go.jp/constitution_and_government_of_japan/constitution_e.html
- https://www.transparency.org/en/cpi/2025

## Singapore (`singapore`)

**Type:** country

**Border history**
- 1819 Stamford Raffles established a British trading post on an island already connected to Malay-world trade and settlement.
- 1824 treaties placed Singapore firmly under British control as part of imperial trade strategy.
- 1942–1945 Japanese occupation during World War II was brutal and central to modern memory.
- 1963 Singapore joined Malaysia; 1965 separation made it an independent city-state with tiny land borders but major maritime stakes.

**Human-cost tags:** colonialism, occupation, separation, city-state, maritime border

**Government context:** Parliamentary republic; People’s Action Party has dominated government since self-rule/independence era.

**Languages:** English, Malay, Mandarin, and Tamil are official; Malay is national language, while multilingual everyday use is common.

**Corruption context:** 84/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Singapore
- https://www.nlb.gov.sg/main/article-detail?cmsuuid=33c12da6-9d6b-4d3f-9e55-7df5e7abceef
- https://www.gov.sg/article/government-system
- https://www.transparency.org/en/cpi/2025

## Monaco (`monaco`)

**Type:** country

**Border history**
- 1297 Grimaldi seizure of the fortress began the ruling dynasty’s long association with Monaco.
- 1861 Franco-Monegasque treaty recognized Monaco’s sovereignty while ceding Menton and Roquebrune to France.
- 1918 treaty with France tied Monaco’s external position closely to French interests while preserving separate statehood.
- Modern Monaco’s land border is entirely with France; its sovereignty is microstate survival through diplomacy, finance, and legal specificity.

**Human-cost tags:** microstate, treaty, dynastic rule, protectorate influence

**Government context:** Constitutional hereditary monarchy; prince is head of state with elected National Council and minister of state.

**Languages:** French is official; Monégasque/Ligurian heritage language, Italian, and English are also used.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.britannica.com/place/Monaco
- https://en.gouv.mc/Government-Institutions/Institutions/Political-system
- https://www.gouv.mc/Action-Gouvernementale/Monaco-a-l-International/Monaco-et-l-Union-Europeenne/Relations-bilaterales-avec-la-France
- https://www.cia.gov/the-world-factbook/countries/monaco/

## Vatican City (`vatican-city`)

**Type:** country

**Border history**
- 1870 Italian capture of Rome ended the Papal States, leaving the pope without temporal territory.
- 1929 Lateran Treaty between Italy and the Holy See created Vatican City as a tiny sovereign state.
- The border is less ethnic or geographic than institutional: a territorial guarantee for the Holy See’s independence.
- Modern Vatican sovereignty is tied to diplomacy, religion, and extraterritorial properties rather than normal national territory.

**Human-cost tags:** treaty, microstate, religious sovereignty, state succession

**Government context:** Ecclesiastical elective monarchy; pope is sovereign, with governance delegated through Vatican institutions.

**Languages:** Italian is everyday administrative language; Latin is important in church law and ritual; many world languages are used by the Holy See.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.britannica.com/place/Vatican-City
- https://www.vaticanstate.va/en/state-government/general-informations/history.html
- https://www.vatican.va/content/holysee/en.html
- https://www.cia.gov/the-world-factbook/countries/holy-see-vatican-city/

## Canada (`canada`)

**Type:** country

**Border history**
- Indigenous nations and Inuit, Métis, and First Nations homelands long predate European imperial borders across northern North America.
- 1763 Treaty of Paris shifted New France to Britain, while later British North America boundaries evolved through imperial administration and settlement.
- 1818 convention and later treaties fixed much of the Canada–United States boundary, including the 49th parallel westward, while Alaska boundaries were settled separately.
- 1867 Confederation joined colonies into the Dominion of Canada; later provinces and territories expanded the federation across the continent.

**Human-cost tags:** colonialism, indigenous dispossession, treaty, federalism, settler expansion

**Government context:** Federal parliamentary democracy and constitutional monarchy; provinces and territories share powers with the federal government.

**Languages:** English and French are official at the federal level; many Indigenous languages remain central to communities and revitalization efforts.

**Corruption context:** 75/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Canada
- https://history.state.gov/countries/canada
- https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/how-canadians-govern-themselves.html
- https://laws-lois.justice.gc.ca/eng/acts/o-3.01/page-1.html
- https://www.transparency.org/en/cpi/2025

## Mexico (`mexico`)

**Type:** country

**Border history**
- Indigenous polities including Mexica, Maya, Mixtec, Zapotec, Purépecha, and many others shaped regions long before Spanish colonial borders.
- 1821 independence from Spain inherited a vast northern frontier whose borders were contested by settler migration, regional autonomy, and foreign pressure.
- 1848 Treaty of Guadalupe Hidalgo ended the Mexican–American War and ceded large northern territories to the United States, fixing much of today’s border.
- 1853 Gadsden Purchase adjusted the border again; later boundary management mixed diplomacy, migration, policing, trade, and shared river systems.

**Human-cost tags:** colonialism, war, territorial cession, indigenous dispossession, border enforcement

**Government context:** Federal presidential republic under the Constitution of the United Mexican States; states and Mexico City have constitutional roles within the federation.

**Languages:** Spanish is the dominant national language; Indigenous languages are recognized as national languages with linguistic rights protections.

**Corruption context:** 27/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Mexico
- https://history.state.gov/countries/mexico
- https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo
- https://www.gob.mx/sesnsp/documentos/constitucion-normateca-del-sesnsp
- https://site.inali.gob.mx/Micrositios/LGDLPI/
- https://www.transparency.org/en/cpi/2025

## Idaho (`idaho`)

**Type:** state

**Border history**
- 1846 Oregon Treaty fixed the U.S.–British boundary at the 49th parallel, placing the future Idaho panhandle inside U.S. claims.
- 1859–1863 the area shifted from Oregon Territory to Washington Territory and then Idaho Territory as Congress reorganized western lands.
- 1864–1868 Montana and Wyoming were carved away, leaving Idaho’s narrow panhandle and southern block shape.
- 1890 statehood locked survey lines, mining/frontier politics, and older Indigenous homelands into a U.S. state border.

**Human-cost tags:** indigenous dispossession, treaty, mining frontier, survey line, territorial carving

**Government context:** U.S. state with a governor-led executive, bicameral legislature, and powers reserved under the federal system.

**Languages:** English dominates public life; Indigenous languages tied to Nez Perce, Shoshone-Bannock, Coeur d’Alene, Kootenai, and other communities remain culturally important.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://history.state.gov/milestones/1830-1860/oregon-territory
- https://history.idaho.gov/wp-content/uploads/0264_The-Creation-of-the-Territory-of-Idaho.pdf
- https://history.idaho.gov/wp-content/uploads/0482_Idaho-Indian-Treaty-Lands.pdf
- https://www.britannica.com/place/Idaho

## Texas (`texas`)

**Type:** state

**Border history**
- 1819 Adams–Onís Treaty set the Sabine River boundary between Spanish Texas and the United States, shaping Texas’s eastern edge.
- 1836 Republic of Texas claimed the Rio Grande as its southern and western boundary, a claim Mexico disputed and Texas did not fully control.
- 1848 Treaty of Guadalupe Hidalgo confirmed the Rio Grande as the international boundary after the Mexican–American War.
- 1850 Compromise fixed Texas’s north and west boundaries after Texas relinquished large western claims for federal debt relief.

**Human-cost tags:** war, annexation, slavery politics, indigenous dispossession, border conflict

**Government context:** U.S. state with a governor-led executive, bicameral legislature, and powers reserved under the federal system.

**Languages:** English dominates statewide; Spanish is deeply rooted and widely spoken; Indigenous and immigrant languages remain part of the state’s cultural landscape.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://www.tsl.texas.gov/exhibits/annexation/aftermath/question10.html
- https://www.tsl.texas.gov/treasures/earlystate/boundary.html
- https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo
- https://www.archives.gov/milestone-documents/compromise-of-1850
- https://www.tshaonline.org/handbook/entries/boundaries

## Alaska (`alaska`)

**Type:** state

**Border history**
- 1825 Anglo-Russian convention described a boundary between Russian America and British possessions, leaving later ambiguities around the coastal strip and mountain line.
- 1867 Treaty of Cession transferred Alaska from Russia to the United States, carrying those inherited boundary questions into U.S.–British/Canadian diplomacy.
- 1897 Klondike gold rush increased pressure to settle access and sovereignty disputes around the Alaska–Canada border.
- 1903 Alaska Boundary Tribunal resolved the main southeastern Alaska boundary dispute largely in favor of the United States; Alaska became a U.S. state in 1959.

**Human-cost tags:** colonialism, treaty, resource frontier, indigenous sovereignty, boundary arbitration

**Government context:** U.S. state with a governor-led executive, bicameral legislature, and powers reserved under the federal system; Alaska Native corporations and tribal governments are major political and land-rights actors.

**Languages:** English dominates state administration; Alaska Native languages across Eskimo-Aleut and Na-Dene families remain culturally central, with revitalization and official-recognition efforts.

**Corruption context:** n/a / not reliably covered by CPI.

**Sources**
- https://history.state.gov/historicaldocuments/frus1903/d479
- https://avalon.law.yale.edu/19th_century/treatywi.asp
- https://www.govinfo.gov/app/details/SERIALSET-04600_00_00-001-0162-0000/
- https://history.state.gov/milestones/1866-1898/alaska-purchase
- https://gov.alaska.gov/admin-orders/administrative-order-no-300/

## Spain (`spain`)

**Type:** country

**Border history**
- 1469 marriage of Ferdinand of Aragon and Isabella of Castile linked two crowns; later conquest of Granada and Navarre helped form the territorial core of Spain.
- 1713 Treaty of Utrecht ended the War of the Spanish Succession settlement; Spain ceded Gibraltar and other European possessions, while Bourbon centralization reshaped internal autonomy.
- 19th-century loss of most American colonies and the 1898 Spanish-American War reduced Spain from empire to a mostly European state with remaining North African enclaves.
- Post-1978 democracy recognizes autonomous communities, so modern territorial politics include Catalonia, the Basque Country, and debates over Gibraltar, Ceuta, and Melilla.

**Human-cost tags:** empire, conquest, colonialism, war, regional autonomy

**Government context:** Parliamentary constitutional monarchy; the monarch is head of state, while the prime minister leads government through the Cortes Generales.

**Languages:** Castilian Spanish is official nationwide; Catalan/Valencian, Galician, Basque, and other languages have official or protected regional roles.

**Corruption context:** 55/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Spain
- https://history.state.gov/countries/spain
- https://www.lamoncloa.gob.es/lang/en/espana/historyandculture/constitutionalorganisation/Paginas/index.aspx
- https://www.transparency.org/en/cpi/2025
- https://mptmd.gob.es/en/portal/politica-territorial/autonomica/lenguas-cooficiales

## Italy (`italy`)

**Type:** country

**Border history**
- 1861 Kingdom of Italy unified many pre-existing states, though Rome and Venetia joined only after later wars and diplomacy.
- 1919–1920 post-World War I settlements brought South Tyrol/Alto Adige and other borderlands into Italy, creating lasting minority-language questions.
- 1947 peace treaty after World War II adjusted Italy’s borders, including losses around Istria and the complex Free Territory of Trieste settlement.
- Postwar European integration softened Alpine and Adriatic borders, while regional autonomy remains important in places such as South Tyrol, Sicily, and Sardinia.

**Human-cost tags:** unification, war, treaty, minority rights, borderland displacement

**Government context:** Parliamentary republic; the president is head of state and the prime minister leads government with parliamentary confidence.

**Languages:** Italian is official; protected minority languages include German, French, Slovene, Ladin, Sardinian, Friulian, and others under national and regional laws.

**Corruption context:** 53/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Italy
- https://history.state.gov/countries/italy
- https://www.quirinale.it/page/costituzione?lingua=en
- https://www.transparency.org/en/cpi/2025
- https://libertaciviliimmigrazione.dlci.interno.gov.it/minoranze-linguistiche-storiche

## Belgium (`belgium`)

**Type:** country

**Border history**
- 1830 Belgian Revolution separated the southern provinces from the Netherlands; the 1839 Treaty of London recognized Belgium and fixed key borders.
- World Wars I and II brought German invasions and occupation despite Belgium’s small size and strategic position between larger powers.
- Postwar state reforms gradually federalized Belgium around language communities and regions rather than moving the external border.
- Today borders are highly integrated through the EU and Schengen, while internal language borders shape politics, education, and public administration.

**Human-cost tags:** treaty, occupation, great-power diplomacy, federalism, language politics

**Government context:** Federal parliamentary constitutional monarchy with powers divided among federal, regional, and community institutions.

**Languages:** Dutch, French, and German are official; language communities and the Brussels-Capital bilingual region are central to public life.

**Corruption context:** 69/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Belgium
- https://history.state.gov/countries/belgium
- https://www.belgium.be/en/about_belgium/government/federale_staat
- https://www.transparency.org/en/cpi/2025

## Netherlands (`netherlands`)

**Type:** country

**Border history**
- 1579 Union of Utrecht joined rebellious northern provinces during the Dutch Revolt; 1648 Peace of Münster recognized the Dutch Republic’s independence from Spain.
- 1815 Congress of Vienna created the Kingdom of the Netherlands by joining the northern Netherlands with the southern provinces as a buffer after Napoleonic wars.
- 1830 Belgian Revolution and the 1839 Treaty of London separated Belgium from the Netherlands, fixing much of the modern southern frontier.
- Post-1945 European integration and Benelux/EU cooperation softened borders with Belgium and Germany, while Caribbean parts of the kingdom keep Dutch sovereignty transatlantic.

**Human-cost tags:** revolt, treaty, partition, empire, European integration

**Government context:** Constitutional monarchy and parliamentary democracy; ministers are politically responsible for government, and the monarch’s role is constitutional.

**Languages:** Dutch is official; Frisian is official in Fryslân/Friesland, while Low Saxon and Limburgish are recognized regional languages under the European language charter.

**Corruption context:** 78/100, Transparency International CPI 2025 (2025).

**Sources**
- https://www.britannica.com/place/Netherlands
- https://history.state.gov/countries/netherlands
- https://www.government.nl/themes/government-and-democracy/constitution
- https://www.rijksoverheid.nl/documenten/vraag-en-antwoord/erkende-talen/erkende-talen-nederland
- https://www.transparency.org/en/cpi/2025

## California (`california`)

**Type:** us-state

**Border history**
- Long before state lines, California contained many Indigenous homelands; Spanish missions, Mexican land grants, and later U.S. rule layered new jurisdictions over them.
- The 1848 Treaty of Guadalupe Hidalgo transferred Alta California from Mexico to the United States after the Mexican-American War.
- California entered the Union in 1850 under the Compromise of 1850; its admission as a free state was tied to national conflict over slavery.
- California’s eastern boundary was surveyed and disputed in stages, with practical border fixing continuing after statehood.

**Human-cost tags:** indigenous dispossession, war, treaty, statehood, slavery politics

**Government context:** U.S. state with a governor, bicameral legislature, and constitution; local governments retain important land-use and service powers.

**Languages:** English is the dominant government language; Spanish, Chinese, Tagalog, Vietnamese, Korean, Armenian, and many Indigenous languages are part of the state’s linguistic landscape.

**Corruption context:** Not applicable/reliably comparable for U.S. states in this pack.

**Sources**
- https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo
- https://www.archives.gov/milestone-documents/compromise-of-1850
- https://www.parks.ca.gov/?lang=en&page_id=23856
- https://www.senate.gov/states/CA/timeline.shtml

## Arizona (`arizona`)

**Type:** us-state

**Border history**
- Present-day Arizona includes many Indigenous homelands whose borders and governance long predate Spanish, Mexican, and U.S. jurisdiction.
- Much of northern Arizona came under U.S. control through the 1848 Treaty of Guadalupe Hidalgo; southern Arizona was added through the 1853 Gadsden Purchase.
- Congress created Arizona Territory in 1863, separating it from New Mexico Territory during the Civil War era.
- Arizona became a state in 1912, after an enabling act and constitution-writing process shaped its modern state government.

**Human-cost tags:** indigenous dispossession, war, treaty, purchase, territorial government

**Government context:** U.S. state with elected executive offices, a bicameral legislature, and county/municipal governments; tribal nations exercise sovereignty within the state.

**Languages:** English is the dominant government language; Spanish and Indigenous languages including Diné/Navajo, Apache, O’odham, Hopi, and Yuman languages are historically important.

**Corruption context:** Not applicable/reliably comparable for U.S. states in this pack.

**Sources**
- https://history.state.gov/milestones/1830-1860/gadsden-purchase
- https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo
- https://www.senate.gov/states/AZ/timeline.htm
- https://azcapitolmuseum.gov/pdfs/azcm-introduction-packet.pdf

## Nevada (`nevada`)

**Type:** us-state

**Border history**
- Nevada’s modern borders overlay Indigenous homelands including Paiute, Shoshone, and Washoe peoples, later claimed by Spain, Mexico, and the United States.
- The 1848 Treaty of Guadalupe Hidalgo placed the region under U.S. control; the Comstock silver boom helped push separate territorial organization.
- Congress created Nevada Territory from western Utah Territory in 1861, then admitted Nevada as a state in 1864 during the Civil War.
- Nevada’s shape expanded east and south after statehood, including later additions from Utah Territory and Arizona Territory.

**Human-cost tags:** indigenous dispossession, mining boom, war, territorial government, statehood

**Government context:** U.S. state with a governor, bicameral legislature, and constitution; counties and cities handle many local services across large federal-land areas.

**Languages:** English is the dominant government language; Spanish, Tagalog, Chinese languages, and Indigenous languages including Northern Paiute, Shoshone, and Washoe are part of the state context.

**Corruption context:** Not applicable/reliably comparable for U.S. states in this pack.

**Sources**
- https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo
- https://jic.nv.gov/About/History_of_Nevada/
- https://www.leg.state.nv.us/Const/NVAdmActs.html
- https://nsla.nv.gov/utah-nevada-territory/home
