import xml.etree.ElementTree as ET

class BuildXmlPerser:
    def __init__(self, xml_path) -> None:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        self.xml_dict = self.xml_to_dict(root)
        pass

    def xml_to_dict(self, elemet):
        """
        xmlをperseしてdictに格納します
        """
        result = {}
        for child in elemet:
            if child.tag in result:
                if type(result[child.tag]) is list:
                    result[child.tag].append(self.xml_to_dict(child))
                else:
                    result[child.tag] = [result[child.tag], self.xml_to_dict(child)]
            else:
                result[child.tag] = self.xml_to_dict(child) if len(child) > 0 else child.text
        return result
    
    def get_gerrit_trigger_review_comment(self):
        """
        triggerとなったgerritのレビューコメントを返します
        """
        return (self.xml_dict["actions"]["hudson.model.CauseAction"]["causeBag"]
                ["entry"]["com.sonyericsson.hudson.plugins.gerrit.trigger.hudsontrigger.GerritCause"]
                ["tEvent"]["comment"])


# 以下開発確認用
xml_file_path = "sample_data/build.xml"
build_xml = BuildXmlPerser(xml_path=xml_file_path)
print("comment:", build_xml.get_gerrit_trigger_review_comment())
print(build_xml.xml_dict)
