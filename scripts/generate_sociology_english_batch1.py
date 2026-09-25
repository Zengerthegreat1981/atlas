#!/usr/bin/env python3
"""
Generate Sociology Phase 1 English Batch 1: Schools (40 nodes)
Properly formatted YAML with bilingual metadata
"""

import os
import json
from datetime import datetime
from pathlib import Path
import yaml

CONTENT_DIR = Path("/Users/mina/Desktop/Atlas/content/en/schools")
CONTENT_DIR.mkdir(parents=True, exist_ok=True)

# Batch 1: 40 Classical and Foundational Sociology Schools
SCHOOLS_DATA = [
    {
        "slug": "sch-comtean-positivism-english",
        "id": "SOC-14000",
        "title": "الوضعية السوسيولوجية الكلاسيكية",
        "en": "Comtean Positivism",
        "crumb": "علم الاجتماع ← الوضعية الكلاسيكية",
        "dates": "France · 1830-1857",
        "active_start": 1830,
        "tradition": "positivist",
        "paradigm": "macro",
        "description": "Auguste Comte's foundational positivist approach establishing sociology as the 'science of society' with systematic laws of social organization and development. Comte argued that just as natural phenomena follow discoverable laws, social phenomena also follow discoverable laws that can be studied scientifically.",
        "sources": [
            "Comte, Auguste. Cours de Philosophie Positive. 1830-1842.",
            "Pickering, Mary. Auguste Comte: An Intellectual Biography. Cambridge University Press, 1993.",
        ]
    },
    {
        "slug": "sch-spencerian-evolutionism-english",
        "id": "SOC-14001",
        "title": "التطورية الاجتماعية والعضوية",
        "en": "Spencerian Social Evolutionism",
        "crumb": "علم الاجتماع ← التطورية الاجتماعية",
        "dates": "Britain · 1850-1903",
        "active_start": 1850,
        "tradition": "evolutionary",
        "paradigm": "macro",
        "description": "Herbert Spencer's evolutionary sociology viewing society as an evolving organism. Spencer applied Darwinian principles to society, arguing that societies evolve from simple to complex forms through natural selection, competition, and survival of the fittest.",
        "sources": [
            "Spencer, Herbert. The Principles of Sociology. Williams & Norgate, 1876-1896.",
            "Peel, J.D.Y. Spencer and the Liberal Temper. Routledge, 1971.",
        ]
    },
    {
        "slug": "sch-marxist-classical-sociology-english",
        "id": "SOC-14002",
        "title": "المادية التاريخية السوسيولوجية",
        "en": "Marxist Classical Sociology",
        "crumb": "علم الاجتماع ← الماركسية والصراع",
        "dates": "Germany/International · 1848-present",
        "active_start": 1848,
        "tradition": "marxian",
        "paradigm": "macro",
        "description": "Sociological readings of Marx's historical materialism and class conflict as foundational structural theory. This tradition analyzes modes of production, social relations, class struggle, and alienation as core sociological concepts.",
        "sources": [
            "Marx, Karl & Engels, Friedrich. The German Ideology. 1845.",
            "Miliband, Ralph. The State in Capitalist Society. Weidenfeld & Nicolson, 1969.",
        ]
    },
    {
        "slug": "sch-durkheimian-functionalism-english",
        "id": "SOC-14003",
        "title": "البنائية الوظيفية الدوركهايمية",
        "en": "Durkheimian Structural Functionalism",
        "crumb": "علم الاجتماع ← الوظيفية البنائية",
        "dates": "France · 1893-1917",
        "active_start": 1893,
        "tradition": "functionalist",
        "paradigm": "macro",
        "description": "Émile Durkheim's foundational functionalist paradigm treating society as an integrated system where social institutions serve essential functions for social cohesion and solidarity. Durkheim pioneered empirical sociological research and analysis of social facts.",
        "sources": [
            "Durkheim, Émile. The Division of Labor in Society. Free Press, 1893.",
            "Giddens, Anthony (ed.). Durkheim and Modern Sociology. Stanford University Press, 1986.",
        ]
    },
    {
        "slug": "sch-weberian-verstehen-english",
        "id": "SOC-14004",
        "title": "السوسيولوجيا الفهمية الفيبرية",
        "en": "Weberian Interpretive Sociology",
        "crumb": "علم الاجتماع ← الفهمية والتفسير",
        "dates": "Germany · 1905-1920",
        "active_start": 1905,
        "tradition": "interpretive",
        "paradigm": "micro-macro",
        "description": "Max Weber's interpretive sociology emphasizing verstehen (understanding) of subjective meanings and intentional action. Weber developed ideal types as analytical tools and analyzed rationalization, authority types, and religious ethics as sociological phenomena.",
        "sources": [
            "Weber, Max. The Protestant Ethic and the Spirit of Capitalism. Penguin, 1905.",
            "Kalberg, Stephen. Max Weber's Comparative-Historical Sociology. University of Chicago Press, 1994.",
        ]
    },
    {
        "slug": "sch-simmelian-formal-english",
        "id": "SOC-14005",
        "title": "السوسيولوجيا الصورية الزيملية",
        "en": "Simmelian Formal Sociology",
        "crumb": "علم الاجتماع ← الصورية والأشكال الاجتماعية",
        "dates": "Germany · 1890-1918",
        "active_start": 1890,
        "tradition": "formal",
        "paradigm": "micro",
        "description": "Georg Simmel's formal sociology analyzing abstract social forms and structures. Simmel examined dyads, triads, networks, and other geometric properties of social relations independent of their content, pioneering microsociology.",
        "sources": [
            "Simmel, Georg. The Sociology of Georg Simmel. Free Press, 1908.",
            "Frisby, David. Georg Simmel: Critical Assessments. Routledge, 1994.",
        ]
    },
    {
        "slug": "sch-chicago-urban-ecology-english",
        "id": "SOC-14006",
        "title": "مدرسة شيكاغو الإيكولوجية",
        "en": "Chicago School Urban Ecology",
        "crumb": "علم الاجتماع ← الإيكولوجيا الحضرية",
        "dates": "USA · 1920-1940",
        "active_start": 1920,
        "tradition": "ecological",
        "paradigm": "macro",
        "description": "The Chicago School's ecological approach to studying urban communities, neighborhoods, and zones. This approach emphasized empirical fieldwork, participant observation, and understanding urban social organization through ecological metaphors.",
        "sources": [
            "Park, Robert E., Burgess, Ernest W., & McKenzie, Roderick D. The City. University of Chicago Press, 1925.",
            "Fine, Gary Alan. The Sociology of the Chicago School. University of Chicago Press, 1995.",
        ]
    },
    {
        "slug": "sch-symbolic-interactionism-english",
        "id": "SOC-14007",
        "title": "التفاعلية الرمزية",
        "en": "Symbolic Interactionism",
        "crumb": "علم الاجتماع ← التفاعلية والرموز",
        "dates": "USA · 1930-present",
        "active_start": 1930,
        "tradition": "interactionist",
        "paradigm": "micro",
        "description": "Symbolic interactionism examining social interaction through shared symbols, meanings, and interpretive processes. This tradition studies how people construct reality through interaction and how selves emerge through social process.",
        "sources": [
            "Blumer, Herbert. Symbolic Interactionism: Perspective and Method. Prentice Hall, 1969.",
            "Fine, Gary Alan. Meaningful Worlds. University of Chicago Press, 2012.",
        ]
    },
    {
        "slug": "sch-goffmanian-dramaturgical-english",
        "id": "SOC-14008",
        "title": "النظرية الدراماتورجية الغوفمانية",
        "en": "Goffmanian Dramaturgical Sociology",
        "crumb": "علم الاجتماع ← الدراماتورجيا والأداء",
        "dates": "USA/Canada · 1959-1983",
        "active_start": 1959,
        "tradition": "interactionist",
        "paradigm": "micro",
        "description": "Erving Goffman's dramaturgical perspective analyzing social life as theatrical performance with front/back stages, impression management, and interaction rituals. Goffman examined stigma, total institutions, and everyday interaction order.",
        "sources": [
            "Goffman, Erving. The Presentation of Self in Everyday Life. Doubleday, 1959.",
            "Manning, Philip & Smith, Gregory W.H. (eds.). The Goffman Reader. Wiley-Blackwell, 2010.",
        ]
    },
    {
        "slug": "sch-parsonian-agil-english",
        "id": "SOC-14009",
        "title": "الوظيفية البنائية عند بارسونز",
        "en": "Parsonian Structural Functionalism",
        "crumb": "علم الاجتماع ← الوظيفية والأنساق",
        "dates": "USA · 1951-1979",
        "active_start": 1951,
        "tradition": "functionalist",
        "paradigm": "macro",
        "description": "Talcott Parsons' elaboration of functionalist theory with action theory and the AGIL model (Adaptation, Goal-attainment, Integration, Latency). Parsons developed pattern variables and systems theory as frameworks for understanding social systems.",
        "sources": [
            "Parsons, Talcott. The Social System. Free Press, 1951.",
            "Buxton, William. Talcott Parsons and the Capitalist Nation-State. University of Toronto Press, 1985.",
        ]
    },
]

def create_sociology_node(data):
    """Create a properly formatted sociology node file"""

    frontmatter = {
        "slug": data["slug"],
        "id": data["id"],
        "type": "مدرسة",
        "part": "sociology",
        "sociological_tradition": data["tradition"],
        "sociological_paradigm": data["paradigm"],
        "level": "متوسط",
        "title": data["title"],
        "en": data["en"],
        "crumb": data["crumb"],
        "dates": data["dates"],
        "active_start": data["active_start"],
        "active_end": "مستمر",
        "edges": [],
        "related": [],
        "gaps": [
            "English version created 2026-09-25 from Arabic base",
            "Full translation and sociological contextualization pending",
            "Additional scholarly sources and critical perspectives needed"
        ]
    }

    # Format YAML properly
    yaml_str = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False)
    yaml_str = yaml_str.rstrip()

    content_body = f"""
# {data["en"]}

{data["description"]}

## Historical Development

[Expansion of school history and evolution pending full development]

## Key Theoretical Contributions

[Key contributions and theoretical innovations pending]

## Contemporary Applications

[Contemporary applications and influence pending]

## Sources

"""

    for source in data["sources"]:
        content_body += f"- {source}\n"

    # Combine everything
    full_content = f"---\n{yaml_str}\n---{content_body}\n"

    return full_content

def main():
    print("Generating Sociology Phase 1 Batch 1: Schools (10/40)")

    count = 0
    for school_data in SCHOOLS_DATA:
        filepath = CONTENT_DIR / f"{school_data['slug']}.md"
        content = create_sociology_node(school_data)
        filepath.write_text(content, encoding='utf-8')
        count += 1
        print(f"  {count}. {filepath.name}")

    print(f"\nCreated {count} school nodes in {CONTENT_DIR}")
    print("Note: Remaining 30 nodes (11-40) with generic structures")
    print("Next: Add remaining schools with full content, then validate")

if __name__ == "__main__":
    main()
