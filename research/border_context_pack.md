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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

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

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo
- https://jic.nv.gov/About/History_of_Nevada/
- https://www.leg.state.nv.us/Const/NVAdmActs.html
- https://nsla.nv.gov/utah-nevada-territory/home

## Utah (`utah`)

**Type:** us-state

**Border history**
- Utah’s state borders overlay Indigenous homelands including Ute, Paiute, Goshute, Shoshone, and Diné/Navajo peoples, whose governance and movement predate U.S. territorial lines.
- The 1848 Treaty of Guadalupe Hidalgo transferred the region from Mexico to the United States; Mormon migration and settlement quickly made the area a distinct U.S. territorial question.
- Congress created Utah Territory in 1850 as part of the Compromise of 1850, originally far larger than the modern state before later territorial reductions created neighboring jurisdictions.
- Utah became a state in 1896 after repeated statehood efforts, with the modern border reflecting federal territorial carving, mining/frontier politics, and religious-political conflict over governance.

**Human-cost tags:** indigenous dispossession, treaty, religious settlement, territorial government, statehood

**Government context:** U.S. state with a governor, bicameral legislature, and constitution; counties, municipalities, tribal nations, and extensive federal lands shape governance.

**Languages:** English dominates state government; Spanish and Indigenous languages including Ute, Paiute, Goshute/Shoshone, and Diné/Navajo are part of the state context.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo
- https://historytogo.utah.gov/utah-territory/
- https://www.senate.gov/states/UT/timeline.htm
- https://www.uen.org/utah_history_encyclopedia/s/STATEHOOD.shtml

## Oregon (`oregon`)

**Type:** us-state

**Border history**
- Indigenous nations including Chinook, Kalapuya, Klamath, Nez Perce, Umatilla, and many others lived across the region long before U.S. state lines.
- The 1846 Oregon Treaty set the U.S.–British boundary at the 49th parallel, separating Oregon Country from what became British/Canadian territory.
- Oregon Territory was organized in 1848 after settler migration and the provisional government period; later territorial splits created Washington, Idaho-linked, and other boundaries.
- Oregon became a state in 1859; its early constitution included exclusionary racial clauses, a reminder that clean map borders often hid violent and discriminatory settlement politics.

**Human-cost tags:** indigenous displacement, treaty, settler colonialism, territorial split, exclusion law

**Government context:** U.S. state with a governor, bicameral legislature, and judiciary; state government is organized across executive, legislative, and judicial branches.

**Languages:** English is dominant in state government and public life; Spanish and many Indigenous, immigrant, and refugee-community languages are also part of Oregon's language landscape.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://sos.oregon.gov/blue-book/explore/Pages/chronology-1851-1900.aspx
- https://sos.oregon.gov/blue-book/government/Pages/state-constitution.aspx
- https://www.oregon.gov/Pages/government.aspx
- https://www.britannica.com/place/Oregon-state

## Colorado (`colorado`)

**Type:** us-state

**Border history**
- Colorado's rectangular outline overlays homelands of Ute, Cheyenne, Arapaho, Pueblo, Apache, Comanche, and other Native peoples rather than reflecting older cultural boundaries.
- U.S. claims came through overlapping acquisitions and treaties including the Louisiana Purchase, the Adams-Onís Treaty, Texas annexation claims, and the Treaty of Guadalupe Hidalgo.
- The 1861 Colorado Territory gathered pieces from Kansas, Nebraska, New Mexico, and Utah territories during the mining boom and Civil War-era federal organization.
- Colorado entered the Union in 1876; surveyed meridians and parallels make the border look simple, while land loss, reservations, mining, and water compacts made control far more contested.

**Human-cost tags:** indigenous displacement, treaty, mining frontier, survey line, territorial split

**Government context:** U.S. state with an elected governor, bicameral General Assembly, judiciary, and a state constitution that also supports citizen initiatives and referendums.

**Languages:** English is Colorado's official language under the state constitution; Spanish and Indigenous, immigrant, and regional community languages remain important in daily life.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://www.colorado.gov/history-colorado
- https://www.leg.colorado.gov/laws/colorado-constitution
- https://www.leg.colorado.gov/agencies/office-legislative-legal-services/colorado-constitution
- https://www.britannica.com/place/Colorado-state

## Washington (`washington`)

**Type:** us-state

**Border history**
- Washington's state borders overlay Coast Salish, Yakama, Spokane, Nez Perce, Colville, Makah, Chinook, and many other Native homelands that long predate U.S. and Canadian lines.
- The 1846 Oregon Treaty set the 49th parallel as the U.S.-British boundary west to the Strait of Georgia, splitting older Indigenous and trade geographies across what became the U.S.-Canada border.
- Washington Territory was separated from Oregon Territory in 1853, with later adjustments as Idaho and other territorial lines were organized.
- Washington became a state in 1889; its Pacific, Columbia River, and surveyed inland borders hide histories of treaty coercion, settler migration, resource extraction, and cross-border Native ties.

**Human-cost tags:** indigenous displacement, treaty, settler colonialism, territorial split, survey line

**Government context:** U.S. state with an elected governor, bicameral legislature, judiciary, counties, municipalities, and federally recognized tribal governments that exercise sovereignty within the state context.

**Languages:** English dominates state government; Spanish, Lushootseed, Sahaptin/Yakama, Salishan languages, Makah, and many immigrant-community languages are part of Washington's language landscape.

**Corruption context:** Not applicable/reliably comparable for U.S. states in this pack.

**Sources**
- https://history.state.gov/milestones/1830-1860/oregon-territory
- https://www.senate.gov/states/WA/timeline.htm
- https://www.britannica.com/place/Washington-state
- https://goia.wa.gov/tribal-directory/federally-recognized-indian-tribes

## New Mexico (`new-mexico`)

**Type:** us-state

**Border history**
- New Mexico's borders overlay Pueblo, Diné/Navajo, Apache, Comanche, Ute, and other Indigenous homelands whose political geographies predate Spanish, Mexican, and U.S. rule.
- Spanish colonization from the late 1500s made the region part of New Spain; the 1680 Pueblo Revolt showed that imperial control was contested and never simply a line on a map.
- The 1848 Treaty of Guadalupe Hidalgo transferred much of the region from Mexico to the United States, and the 1853 Gadsden Purchase fixed the southern border area.
- New Mexico Territory was organized in 1850 and statehood came in 1912 after long debates over language, race, land grants, and federal control in the borderlands.

**Human-cost tags:** indigenous displacement, colonialism, treaty, borderland, statehood

**Government context:** U.S. state with an elected governor, bicameral legislature, judiciary, counties, municipalities, pueblos, tribal nations, and major federal/tribal land governance layers.

**Languages:** English and Spanish are central to public life; Diné/Navajo, Pueblo languages, Apache languages, and other Indigenous and immigrant-community languages are also important.

**Corruption context:** Not applicable/reliably comparable for U.S. states in this pack.

**Sources**
- https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo
- https://www.senate.gov/states/NM/timeline.htm
- https://www.britannica.com/place/New-Mexico
- https://www.nmlegis.gov/Publications/New_Mexico_Statehood.pdf

## Montana (`montana`)

**Type:** state

**Border history**
- Indigenous nations, including Blackfeet, Crow, Northern Cheyenne, Salish, Kootenai, Pend d’Oreille, Assiniboine, Sioux, and others, shaped the region long before U.S. territorial lines.
- The 1846 Oregon Treaty fixed the 49th parallel as the U.S.–British North America boundary west of the Rockies, forming Montana’s future northern international border.
- Congress created Montana Territory in 1864 out of areas previously attached to Idaho and Dakota territories, reflecting mining rushes and federal territorial administration.
- Montana became a state in 1889; its later political borders remained mostly stable, while tribal reservations and federal lands continued to shape jurisdiction on the ground.

**Human-cost tags:** indigenous dispossession, treaty, territory, settler colonialism, resource extraction

**Government context:** U.S. state with a constitutionally separated executive, legislative, and judicial government; local governments operate under state law.

**Languages:** English is the official language for state and local government; Indigenous languages and Spanish are among communities’ important living languages.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://montana.gov/discover/brief_history
- https://courts.mt.gov/External/library/guides/guide.pdf
- https://mca.legmt.gov/bills/MCA/title_0010/chapter_0010/part_0050/section_0100/0010-0010-0050-0100.html

## North Dakota (`north-dakota`)

**Type:** state

**Border history**
- The Mandan, Hidatsa, Arikara, Dakota/Lakota, Ojibwe, and other Indigenous peoples lived with trade, river, and kinship geographies that predated U.S. survey lines.
- Dakota Territory was organized in 1861 and its boundaries changed multiple times before the northern plains were divided into states.
- North Dakota’s eastern edge follows the Red River, but its other borders are congressional political boundaries rather than natural divisions.
- In 1889 Congress admitted North Dakota and South Dakota separately, fixing the state’s core outline while reservation, county, and federal land jurisdictions remained consequential.

**Human-cost tags:** indigenous dispossession, territory, treaty, partition, settler colonialism

**Government context:** U.S. state with elected executive officials, a bicameral Legislative Assembly, and a state judiciary under the North Dakota Constitution.

**Languages:** English is the main government language; Dakota/Lakota, Ojibwe, Hidatsa, Mandan, Arikara, Norwegian heritage, German heritage, Spanish, and newer immigrant languages are part of the state’s language landscape.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://www.history.nd.gov/archives/stateagencies/dtrecords.html
- https://www.ndstudies.gov/gr8/node/65
- https://www.dmr.nd.gov/ndgs/ndnotes/Boundaries/Boundaries.asp

## South Dakota (`south-dakota`)

**Type:** state

**Border history**
- Present-day South Dakota was part of the Louisiana Purchase, a paper transfer of imperial claims over lands already governed and used by Native nations.
- 1861 Dakota Territory organized a large northern-plains territory; later territorial changes and settlement pressure separated Dakota from Nebraska, Wyoming, Montana, and Idaho-era claims.
- 1868 Fort Laramie Treaty recognized the Great Sioux Reservation west of the Missouri River, but later U.S. actions and agreements broke that land base into smaller reservations.
- 1889 Enabling Act split Dakota Territory into North Dakota and South Dakota, turning a survey line and federal admission politics into a state boundary.

**Human-cost tags:** indigenous displacement, treaty, reservation, settler colonialism, survey line

**Government context:** U.S. state government with executive, legislative, and judicial branches; governor leads the executive branch and the legislature is bicameral.

**Languages:** English is the state’s common language; the language of the O'ceti Sakowin/Great Sioux Nation—Dakota, Lakota, and Nakota—is recognized as the official indigenous language.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://sdsos.gov/general-information/about-state-south-dakota/
- https://www.justice.gov/usao-sd/indian-country
- https://sdlegislature.gov/Statutes/1-27-20
- https://sdlegislature.gov/Constitution/2-0

## Nebraska (`nebraska`)

**Type:** state

**Border history**
- Present-day Nebraska sits within the Louisiana Purchase region, where U.S. claims overlaid Native homelands and treaty relationships.
- 1854 Kansas-Nebraska Act created Nebraska Territory and tied its organization to the national conflict over slavery through popular sovereignty.
- Nebraska Territory was later reduced as new territories and states were carved from the plains and Rockies, leaving a more compact state along the Missouri River and 40th parallel.
- 1867 statehood fixed Nebraska’s state frame during Reconstruction-era disputes over suffrage and admission conditions.

**Human-cost tags:** indigenous displacement, treaty, slavery politics, territorial carving, survey line

**Government context:** U.S. state government with executive, judicial, and a distinctive unicameral, officially nonpartisan legislature—the only one-house state legislature in the United States.

**Languages:** English is the state’s official language; Native, immigrant, and refugee languages remain part of Nebraska’s communities even without statewide official status.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://www.archives.gov/milestone-documents/kansas-nebraska-act
- https://history.nebraska.gov/the-kansas-nebraska-act-and-the-organization-of-nebraska-territory/
- https://history.nebraska.gov/nebraska-statehood-launched-in-troubled-times/
- https://www.nebraskalegislature.gov/about/ou_facts.php
- https://www.nebraskalegislature.gov/laws/articles.php?article=I-27&print=true

## Kansas (`kansas`)

**Type:** us-state

**Border history**
- 1803 Louisiana Purchase brought the area claimed by France under U.S. control, while Native nations retained homelands and treaty rights that settlers and federal policy increasingly constrained.
- 1854 Kansas-Nebraska Act organized Kansas Territory and used popular sovereignty for slavery, turning the Missouri border region into the violent Bleeding Kansas conflict.
- 1861 Kansas entered the Union as a free state shortly before the Civil War, fixing its statehood against the backdrop of sectional conflict.
- Modern Kansas borders follow survey lines and river segments, but the state still reflects older Indigenous removals, railroad settlement, and border-war memory.

**Human-cost tags:** indigenous displacement, slavery conflict, settler colonialism, civil war, survey borders

**Government context:** U.S. state with an elected governor and bicameral legislature; counties and municipalities handle many local services under state law.

**Languages:** English is the dominant official/public language; Spanish, Vietnamese, German heritage varieties, and Native languages including Kanza/Kaw revitalization contexts are part of the wider language landscape.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://www.kansashistory.gov/
- https://home.nps.gov/articles/bleeding-kansas.htm
- https://sos.ks.gov/Pubs/Publications/KTAN.pdf

## Oklahoma (`oklahoma`)

**Type:** us-state

**Border history**
- Indian Territory grew from U.S. removal policy that forced many Native nations west of the Mississippi, layering sovereign tribal histories into the future state.
- 1887 Dawes Act allotment and later land openings broke up collectively held tribal lands and accelerated non-Native settlement in and around Oklahoma Territory.
- 1906 Oklahoma Enabling Act and 1907 statehood merged Oklahoma Territory and Indian Territory into one state instead of separate or Sequoyah-style Indigenous-led statehood.
- Today Oklahoma's map coexists with federally recognized tribal nations and jurisdictional debates shaped by treaties, allotment, and court rulings.

**Human-cost tags:** indigenous displacement, treaty rights, allotment, settler colonialism, statehood

**Government context:** U.S. state with an elected governor and bicameral legislature; tribal governments also exercise sovereign powers within treaty and federal-law frameworks.

**Languages:** English dominates public life; many Native languages including Cherokee, Choctaw, Chickasaw, Muscogee, Seminole, Osage, Comanche, Kiowa, and others have community and revitalization roles; Spanish is also widely used.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://www.archives.gov/legislative/features/oklahoma
- https://www.okhistory.org/publications/enc/entry.php?entryname=STATEHOOD+MOVEMENT
- https://www.okhistory.org/learn/government5

## Arkansas (`arkansas`)

**Type:** us-state

**Border history**
- 1803 Louisiana Purchase transferred French-claimed land to the United States, accelerating U.S. control over the lower Mississippi borderlands.
- 1819 Arkansas Territory was separated from Missouri Territory; its western line was later adjusted as Indian Territory and U.S. settlement policy evolved.
- 1830s Indian Removal reshaped Arkansas by forcing Native peoples out of ancestral lands and routing removed eastern nations through or beyond the state.
- 1836 statehood and later Civil War/Reconstruction politics fixed Arkansas as a slave-state borderland whose Mississippi River edge tied it to regional trade and conflict.

**Human-cost tags:** indigenous displacement, slavery, territorial partition, civil war, river borders

**Government context:** U.S. state with an elected governor and bicameral legislature; county governments remain important for local administration.

**Languages:** English dominates public life; Spanish, Marshallese, Vietnamese, and Native language heritage contexts are part of the broader language landscape.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://encyclopediaofarkansas.net/entries/Louisiana-Purchase-2383/
- https://encyclopediaofarkansas.net/entries/Indian-Removal-2595/
- https://encyclopediaofarkansas.net/entries/louisiana-purchase-through-early-statehood-1803-through-1860-398/

## Missouri (`missouri`)

**Type:** us-state

**Border history**
- Present-day Missouri was within the Louisiana Purchase, where U.S. claims overlaid Indigenous nations’ lands, trade routes, and treaty relationships.
- 1812 Missouri Territory was organized from the former Louisiana Territory, then later reduced as Arkansas and other western lands were separated.
- 1820 Missouri Compromise tied Missouri’s admission as a slave state to Maine’s admission as a free state and a slavery restriction north of 36°30′ in much of the Louisiana Purchase.
- 1821 statehood fixed Missouri’s basic outline, while the Missouri River, Mississippi River, and later border-war politics kept the state tied to both western expansion and Civil War conflict.

**Human-cost tags:** indigenous displacement, slavery politics, territorial partition, settler colonialism, civil war

**Government context:** U.S. state with an elected governor, bicameral General Assembly, and state judiciary; counties and municipalities exercise powers under state law.

**Languages:** English is the dominant language of public life; Spanish, Bosnian, German heritage varieties, and Native language heritage contexts are part of Missouri’s wider language landscape.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://www.sos.mo.gov/Archives/Bicentennial/Summary
- https://www.loc.gov/item/today-in-history/august-10/
- https://www.senate.gov/states/MO/timeline.shtml

## Iowa (`iowa`)

**Type:** us-state

**Border history**
- Present-day Iowa was part of the Louisiana Purchase, but Native nations’ homelands and treaty relationships predated and outlasted U.S. paper claims.
- 1832 Black Hawk War and subsequent land cessions opened large areas west of the Mississippi to U.S. settlement under coercive conditions.
- 1838 Congress created Iowa Territory from Wisconsin Territory; early proposals and voter debates over boundaries shaped the eventual state outline.
- 1846 statehood made Iowa the 29th state after boundary compromises; its Missouri and Mississippi river edges contrast with surveyed northern and western lines.

**Human-cost tags:** indigenous displacement, treaty, territorial partition, settler colonialism, survey borders

**Government context:** U.S. state with executive, legislative, and judicial departments under the Iowa Constitution; local governments operate within state constitutional and statutory frameworks.

**Languages:** English is Iowa’s official language for state government; Spanish, Arabic, Bosnian, Vietnamese, Native language heritage contexts, and other community languages are also present.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://history.iowa.gov/learn/k-12-education/professional-learning/iowa-history-course/unit-3-iowa-statehood
- https://www.iowacourts.gov/for-the-public/educational-resources-and-services/iowa-courts-history
- https://www.legis.iowa.gov/law/statutory/constitution
- https://www.legis.iowa.gov/docs/code/2014/Vol1.pdf

## Louisiana (`louisiana`)

**Type:** us-state

**Border history**
- French and Spanish colonial claims around the lower Mississippi overlaid Native nations’ lands and long-running Indigenous, African, and European borderland histories.
- 1803 Louisiana Purchase transferred French imperial claims to the United States, with New Orleans and Mississippi River access central to U.S. strategy.
- The Territory of Orleans was governed separately from the larger District/Territory of Louisiana before admission as the state of Louisiana in 1812.
- Louisiana’s borders and identity were shaped by river commerce, plantation slavery, Creole/Cajun cultures, Civil War occupation, and later coastal change along the Gulf.

**Human-cost tags:** colonialism, indigenous displacement, slavery, river borders, coastal change

**Government context:** U.S. state with an elected governor, bicameral legislature, and judiciary; Louisiana’s civil-law tradition distinguishes parts of its legal system from other U.S. states.

**Languages:** English is dominant in state government; Louisiana French, Louisiana Creole/Kouri-Vini, Spanish, Vietnamese, and Native language heritage contexts remain culturally important.

**Corruption context:** Not applicable/reliably comparable for this entry in this pack.

**Sources**
- https://www.archives.gov/legislative/features/louisiana-statehood
- https://history.state.gov/milestones/1801-1829/louisiana-purchase
- https://louisianastatemuseum.org/louisiana-history-louisiana-purchase
- https://www.sos.la.gov/HistoricalResources/PublishedDocuments/LouisianaFactsBooklet.pdf
