import csv
import xml.etree.ElementTree as ET

def create_xml_annotation_file(data):
    root = ET.Element("annotation")
    ET.SubElement(root, "filename").text = data['id'] + '.xml'
    annotations = ET.SubElement(root, "annotations")

    for annotation in data['annotations']:
        annotation_type = annotation['type']
        coordinates = annotation['coordinates']

        annotation_element = ET.SubElement(annotations, "annotation")
        ET.SubElement(annotation_element, "type").text = annotation_type

        for coordinate in coordinates:
            point_element = ET.SubElement(annotation_element, "point")
            x, y = coordinate[0], coordinate[1]
            ET.SubElement(point_element, "x").text = str(x)
            ET.SubElement(point_element, "y").text = str(y)

    tree = ET.ElementTree(root)
    tree.write(data['id'] + '.xml')

def process_csv_file(csv_filename):
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = {
                'id': row['id'],
                'annotations': eval(row['annotations'])
            }
            create_xml_annotation_file(data)

if __name__ == "__main__":
    csv_file = "annotations.csv"
    process_csv_file(csv_file)
