import json
import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path
repo_dir = Path(__file__).parent.parent.absolute()

remote_datasets = repo_dir / "datasets_to_add.json"


def read_datasets():
    if remote_datasets.exists():
        with open(remote_datasets) as fn:
            ds_ids = json.load(fn)
    else:
        ds_ids = {}
    return ds_ids


def write_datasets(ds_ids):
    json_str = json.dumps(ds_ids, indent=4)
    with open(remote_datasets, "w") as f:
        f.write(json_str)


def add_voto_og1():
    df = pd.read_csv("https://erddap.observations.voiceoftheocean.org/erddap/search/index.csv?searchFor=OG-1.0")
    df = df.dropna(subset=['tabledap'])
    ds_ids = read_datasets()
    for i, row in df.iterrows():
        ds_ids[f"VOTO_{row['Dataset ID']}"] = row['tabledap']
    write_datasets(ds_ids)


def add_bodc_og1():
    df = pd.read_csv("https://linkedsystems.uk/erddap/search/index.csv?searchFor=OG-1.0")
    df = df.dropna(subset=['tabledap'])
    ds_ids = read_datasets()
    for i, row in df.iterrows():
        ds_ids[f"BODC_{row['Dataset ID']}"] = row['tabledap']
    write_datasets(ds_ids)


def make_datasets_xml():
    # Read in datasets_base_xml for the header settings (no datasets)
    xml_file = repo_dir / 'erddap' / 'content' / 'datasets_base.xml'
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # remove any datasets entered into the base xml
    for child in root.findall('dataset'):
        root.remove(child)
    # loop through input datasets and add them to the xml
    ds_ids = read_datasets()
    for ds_id, ds_url in ds_ids.items():
        item = ET.SubElement(root, "dataset")
        item.attrib["type"] = "EDDTableFromErddap"
        item.attrib["datasetID"] = ds_id
        item.attrib["active"] = "true"
        source_item = ET.SubElement(item, "sourceUrl")
        source_item.text = ds_url
    # Write this out to datasets.xml
    ET.indent(tree, '  ')
    out = repo_dir / 'erddap' / 'content' / 'datasets.xml'
    tree.write(out, encoding="utf-8", xml_declaration=True)


if __name__ == '__main__':
    add_voto_og1()
    add_bodc_og1()
    make_datasets_xml()