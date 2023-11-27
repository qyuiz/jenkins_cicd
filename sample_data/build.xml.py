data = {
    'actions': {
        'hudson.model.CauseAction': {
            'causeBag': {
                'entry': {
                    'com.sonyericsson.hudson.plugins.gerrit.trigger.hudsontrigger.GerritCause': {
                        'tEvent': {
                            'account': {
                                'name': 'Administrator',
                                'email': 'admin@example.com',
                                'username': 'admin'
                            },
                            'provider': {
                                'name': 'local-gerrit',
                                'host': '172.18.0.1',
                                'port': '29418',
                                'scheme': 'ssh',
                                'url': 'http://localhost:8080/',
                                'version': '3.7.5'
                            },
                            'receivedOn': '1700834642134',
                            'eventCreatedOn': '2023-11-24 14:04:02.0 UTC',
                            'change': {
                                'project': 'Test-Repo',
                                'branch': 'master',
                                'hashtags': None,
                                'id': 'I7b5de57db72422fa6f43cbf48060ab4ac37978ee',
                                'number': '22',
                                'subject': 'update2',
                                'commitMessage': 'update2\n\nChange-Id: I7b5de57db72422fa6f43cbf48060ab4ac37978ee\n',
                                'owner': {
                                    'name': 'Administrator',
                                    'email': 'admin@example.com',
                                    'username': 'admin'
                                },
                                'url': 'http://localhost:8080/c/Test-Repo/+/22',
                                'createdOn': '2023-11-24 13:57:46.0 UTC',
                                'status': 'NEW',
                                'wip': 'false',
                                '__private': 'false'
                            },
                            'patchSet': {
                                'number': '1',
                                'revision': 'c479b592ed4b6efda92f1a510d7089c43644fcc3',
                                'ref': 'refs/changes/22/22/1',
                                'draft': 'false',
                                'kind': 'REWORK',
                                'uploader': {
                                    'name': 'Administrator',
                                    'email': 'admin@example.com',
                                    'username': 'admin'
                                },
                                'author': {
                                    'name': 'qyuiz',
                                    'email': 'maibatikun929@gmail.com',
                                    'username': None
                                },
                                'parents': {
                                    'string': 'ab26d661345b74e4b2b9bc2fc2fda80ce4385996'
                                },
                                'createdOn': '2023-11-24 13:57:46.0 UTC'
                            },
                            'comment': 'Patch Set 1:\n\nこんにちは\nこれはテストです\nどうなるかな？',
                            'approvals': {
                                'com.sonyericsson.hudson.plugins.gerrit.gerritevents.dto.attr.Approval': {
                                    'type': 'Code-Review',
                                    'value': '2',
                                    'oldValue': '0'
                                }
                            }
                        },
                        'silentMode': 'false',
                        'context': {
                            'event': None,
                            'thisBuild': {
                                'buildNumber': '4',
                                'projectId': 'gerrit'
                            }
                        },
                        'url': 'http://localhost:8080/c/Test-Repo/+/22'
                    }
                },
                'int': '1'
            }
        },
        'hudson.triggers.SCMTrigger_-BuildAction': None,
        'com.sonyericsson.hudson.plugins.gerrit.trigger.hudsontrigger.BadgeAction': {
            'tEvent': None
        },
        'com.sonyericsson.hudson.plugins.gerrit.trigger.hudsontrigger.actions.RetriggerAction': {
            'context': None
        },
        'com.sonyericsson.hudson.plugins.gerrit.trigger.hudsontrigger.actions.RetriggerAllAction': {
            'context': None
        },
        'hudson.model.ParametersAction': {
            'safeParameters': {
                'string': ['GERRIT_BRANCH']  # (Truncated for brevity, complete the list as needed)
            },
            'parameters': {
                'hudson.model.StringParameterValue': [
                    {'name': 'GERRIT_EVENT_TYPE', 'description': None, 'value': 'comment-added'},
                    # (Truncated for brevity, complete the list as needed)
                ],
                'com.sonyericsson.hudson.plugins.gerrit.trigger.hudsontrigger.parameters.Base64EncodedStringParameterValue': [
                    {'name': 'GERRIT_CHANGE_COMMIT_MESSAGE', 'description': None, 'value': 'dXBkYXRlMgoKQ2hhbmdlLUlkOiBJN2I1ZGU1N2RiNzI0MjJmYTZmNDNjYmY0ODA2MGFiNGFjMzc5NzhlZQo='},
                    # (Truncated for brevity, complete the list as needed)
                ]
            },
            'parameterDefinitionNames': None
        },
        'hudson.plugins.git.util.BuildData': {
            'buildsByBranchName': {
                'entry': {
                    'string': 'refs/remotes/origin/master',
                    'hudson.plugins.git.util.Build': {
                        'marked': {
                            'sha1': 'ab26d661345b74e4b2b9bc2fc2fda80ce4385996',
                            'branches': {
                                'hudson.plugins.git.Branch': {
                                    'sha1': None,
                                    'name': 'refs/remotes/origin/master'
                                }
                            }
                        },
                        'revision': None,
                        'hudsonBuildNumber': '4'
                    }
                }
            },
            'lastBuild': None,
            'remoteUrls': {'string': 'ssh://admin@localhost:29418/Test-Repo'}
        },
        'hudson.scm.SCMRevisionState_-None': None
    },
    'queueId': '4',
    'timestamp': '1700834648459',
    'startTime': '1700834648468',
    'result': 'SUCCESS',
    'duration': '311',
    'charset': 'UTF-8',
    'keepLog': 'false',
    'builtOn': None,
    'workspace': '/var/jenkins_home/workspace/gerrit',
    'hudsonVersion': '2.426.1',
    'scm': {
        'authorOrCommitter': 'false',
        'showEntireCommitSummaryInChanges': 'true'
    },
    'culprits': {'c': {'string': 'maibatikun929'}}
}