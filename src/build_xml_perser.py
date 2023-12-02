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
    
    def get_gerrit_trigger_patchset_id(self):
        """
        パッチセットIDを返します
        """
        # revisionから先頭7文字を抜き出す
        return self.get_gerrit_trigger_parameter("GERRIT_PATCHSET_REVISION")[:7]
    
    def get_gerrit_trigger_repo_name(self):
        """
        リポジトリ名称を返します
        """
        return self.get_gerrit_trigger_parameter("GERRIT_PROJECT")
    
    def get_gerrit_trigger_branch_name(self):
        """
        ブランチ名称を返します
        """
        return self.get_gerrit_trigger_parameter("GERRIT_BRANCH")
    
    def get_gerrit_trigger_review_url(self):
        """
        レビューURLを返します
        """
        return self.get_gerrit_trigger_parameter("GERRIT_CHANGE_URL")
    
    def get_gerrit_trigger_parameter(self, parameter_name):
        """
        指定されたパラメータ名の値を返します
        """
        parameter_list = (self.xml_dict["actions"]["hudson.model.ParametersAction"]
                            ["parameters"]["hudson.model.StringParameterValue"])
        for parameter_dict in parameter_list:
            if parameter_dict["name"] == parameter_name:
                return parameter_dict["value"]
        return ""
    
    def get_gerrit_trriger_commit_user_info(self):
        """
        ユーザー情報を返します

        return:
            'name': 'Administrator',
            'email': 'admin@example.com',
            'username': 'admin'
        """
        user_info = (self.xml_dict["actions"]["hudson.model.CauseAction"]["causeBag"]
                ["entry"]["com.sonyericsson.hudson.plugins.gerrit.trigger.hudsontrigger.GerritCause"]
                ["tEvent"]["account"])
        return user_info



# 以下開発確認用
xml_file_path = "sample_data/build.xml"
build_xml = BuildXmlPerser(xml_path=xml_file_path)
print("comment:", build_xml.get_gerrit_trigger_review_comment())
print("patchSetID:", build_xml.get_gerrit_trigger_patchset_id())
print("repoName:", build_xml.get_gerrit_trigger_repo_name())
print("reviewURL:", build_xml.get_gerrit_trigger_review_url())
userInfo = build_xml.get_gerrit_trriger_commit_user_info()
print("userInfo:", userInfo)
print("name:", userInfo["name"])
print("email:", userInfo["email"])
print("username:", userInfo["username"])
