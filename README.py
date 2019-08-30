<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:flowable="http://flowable.org/bpmn" xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC" xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI" xmlns:sasbpmn="http://www.sas.com/xml/schema/bpmn" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" expressionLanguage="http://www.w3.org/1999/XPath" targetNamespace="http://www.flowable.org/Test" typeLanguage="http://www.w3.org/2001/XMLSchema">
    <process id="WFA37BEF26-296E-4E9D-A0DC-C940FEA355D6" isExecutable="true" name="ModelManagerDemoWorkflowEn">
        <extensionElements>
            <sasbpmn:defaultLocale country="US" language="en" variant=""/>
            <flowable:localization locale="en_US" name="ModelManagerDemoWorkflowEn"/>
            <sasbpmn:prompt dataObjectRef="WFCBD62144-E486-46DE-94AC-A4DEEBBBBD57" id="WF446DB86E-FD23-491D-8456-FF0052E36D17" name="Is the model quality good enough?"/>
            <sasbpmn:prompt dataObjectRef="WFCBD62144-E486-46DE-94AC-A4DEEBBBBD57" id="WF4B8FD138-1C0C-4386-BA41-2EA07BB29476" name="Is the model quality good enough ?"/>
            <sasbpmn:prompt dataObjectRef="WFCED7215C-C534-4AE4-9C96-0DB302146669" id="WF4E3A9345-AD93-4DD1-832B-D18467C55378" name="Select threshold for retrain condition:"/>
            <sasbpmn:prompt dataObjectRef="WF99097AFA-0B8F-452F-B927-451D60D84B4F" id="WFF6D701B1-3F61-4892-8453-5005F77FD6F1" name="Insert github token if needed"/>
            <sasbpmn:promptValue id="WF4A830ECA-BCE0-49F3-89EE-84770772FE00" name="0.01" type="xsd:double" value="0.01"/>
            <sasbpmn:promptValue id="WFA255A265-2715-45E4-8811-CE08A5C58670" name="0.02" type="xsd:double" value="0.02"/>
            <sasbpmn:promptValue id="WF74FB7E81-D679-4298-AFDE-7BEA2BA57A5B" name="0.03" type="xsd:double" value="0.03"/>
            <sasbpmn:promptValue id="WF202E2E2B-3C23-40F0-8410-12B3478B7BFE" name="Yes" type="xsd:boolean" value="true"/>
            <sasbpmn:promptValue id="WF344B51E2-735E-490A-9CAC-FFAADDBC7DAF" name="No" type="xsd:boolean" value="false"/>
        </extensionElements>
        <dataObject id="WFCBD62144-E486-46DE-94AC-A4DEEBBBBD57" itemSubjectRef="xsd:boolean" name="performanceManualOk"/>
        <dataObject id="WFAB174E7D-7FE7-4E14-A032-7C4B43213AE0" itemSubjectRef="xsd:boolean" name="modelIsLoaded"/>
        <dataObject id="WFCED7215C-C534-4AE4-9C96-0DB302146669" itemSubjectRef="xsd:double" name="perfQuality">
            <extensionElements>
                <flowable:value>0.02</flowable:value>
            </extensionElements>
        </dataObject>
        <dataObject id="WF16EA3F78-88D4-496C-9E36-EE5F66F0D6E2" itemSubjectRef="xsd:boolean" name="performanceAutoOk"/>
        <dataObject id="WF5BEEF7DF-DD9C-4BA6-A08A-ECF88473B5A1" itemSubjectRef="xsd:string" name="testMonth">
            <extensionElements>
                <flowable:value>01dec2014</flowable:value>
            </extensionElements>
        </dataObject>
        <dataObject id="WF2E231E3C-6207-4C6E-99E3-EEDDBC95077F" itemSubjectRef="xsd:string" name="projectId">
            <extensionElements>
                <flowable:value/>
            </extensionElements>
        </dataObject>
        <dataObject id="WFD9544935-442A-49D7-8E76-7EE2522B22B7" itemSubjectRef="xsd:string" name="validationMonth">
            <extensionElements>
                <flowable:value>01dec2014</flowable:value>
            </extensionElements>
        </dataObject>
        <dataObject id="WF31517679-21F1-437D-97C9-EA6A0E3F03E8" itemSubjectRef="xsd:string" name="UUID">
            <extensionElements>
                <flowable:value/>
            </extensionElements>
        </dataObject>
        <dataObject id="WF684B1C58-4078-4EB6-ADAA-5CB0EA9A9325" itemSubjectRef="xsd:string" name="taskNewMonthPath">
            <extensionElements>
                <flowable:value>/My Folder/Demo/WFnewMonth</flowable:value>
            </extensionElements>
        </dataObject>
        <dataObject id="WF978C37C9-462F-4E82-ABAC-14645C9A585A" itemSubjectRef="xsd:string" name="taskPerfRep">
            <extensionElements>
                <flowable:value>/My Folder/Demo/WFperfRep</flowable:value>
            </extensionElements>
        </dataObject>
        <dataObject id="WF6B67D1F8-4571-4500-A927-B55BE3D27B28" itemSubjectRef="xsd:string" name="taskAsses">
            <extensionElements>
                <flowable:value>/My Folder/Demo/WFpyAssess</flowable:value>
            </extensionElements>
        </dataObject>
        <dataObject id="WFCAABB3B0-601C-4291-9751-CC71219A65B6" itemSubjectRef="xsd:string" name="taskScore">
            <extensionElements>
                <flowable:value>/My Folder/Demo/WFpyScore</flowable:value>
            </extensionElements>
        </dataObject>
        <dataObject id="WF93A6B357-9696-44D7-B493-949475E35670" itemSubjectRef="xsd:string" name="taskTrain">
            <extensionElements>
                <flowable:value>/My Folder/Demo/WFpyTrain</flowable:value>
            </extensionElements>
        </dataObject>
        <dataObject id="WF8173DD10-4E9D-4ADE-BB54-27DF522136E9" itemSubjectRef="xsd:double" name="processCount"/>
        <dataObject id="WF412D670A-9B47-409F-BA18-DB17864ED796" itemSubjectRef="xsd:string" name="modelId">
            <extensionElements>
                <flowable:value/>
            </extensionElements>
        </dataObject>
        <dataObject id="WFF12A547E-1EFA-4141-8A80-2D0D67F91025" itemSubjectRef="xsd:string" name="taskGetProjectID">
            <extensionElements>
                <flowable:value>/My Folder/Demo/WFgetProjectId</flowable:value>
            </extensionElements>
        </dataObject>
        <dataObject id="WFE814A708-8C3F-4D1A-B4BC-D953BE65C35E" itemSubjectRef="xsd:string" name="procId">
            <extensionElements>
                <flowable:value/>
            </extensionElements>
        </dataObject>
        <dataObject id="WF99097AFA-0B8F-452F-B927-451D60D84B4F" itemSubjectRef="xsd:string" name="githubToken">
            <extensionElements>
                <flowable:value/>
            </extensionElements>
        </dataObject>
        <sequenceFlow id="WF4A6C1D79-A9EA-4B22-8322-FF3B40F0E99D" sourceRef="WFEEBE76D6-F895-4276-9CE2-D62A8D92F2D1" targetRef="WF2F1C8B89-A541-4A88-A7FA-FE4DAAF9832F"/>
        <sequenceFlow id="WF75139DF1-5396-44A5-B757-0EE8BCAB2312" sourceRef="WFD6347A29-23C0-4A56-927F-3DF26687C18A" targetRef="WFBE97D411-85A5-42CB-870D-4DE51100502E"/>
        <sequenceFlow id="WF757A1923-D2E1-4D82-AA21-766A7EEE463D" sourceRef="WF235470E9-4A52-4465-A034-BCB9F4755E48" targetRef="WFEEBE76D6-F895-4276-9CE2-D62A8D92F2D1"/>
        <sequenceFlow id="WF955B744F-54B1-490A-8ECA-897914EF4FE8" name="variables PerformanceManualOk or PerformanceAutoOk==True" sourceRef="WF2F1C8B89-A541-4A88-A7FA-FE4DAAF9832F" targetRef="WFD6347A29-23C0-4A56-927F-3DF26687C18A">
            <conditionExpression xsi:type="tFormalExpression"><![CDATA[${performanceManualOk=='True' || performanceAutoOk=='True' }]]></conditionExpression>
        </sequenceFlow>
        <sequenceFlow id="WFE271E85C-38F0-4C77-B1E8-D1AF85BB540B" sourceRef="WF8E522432-FF68-4C78-B589-9145B332CBBA" targetRef="WFD6347A29-23C0-4A56-927F-3DF26687C18A"/>
        <sequenceFlow id="WFD9A6C766-AB8A-44B9-B9D3-3D78253BB920" name="variables PerformanceAutoOk or  PerformanceManualOk == False" sourceRef="WF2F1C8B89-A541-4A88-A7FA-FE4DAAF9832F" targetRef="WF8E522432-FF68-4C78-B589-9145B332CBBA"/>
        <sequenceFlow id="WFC4341DC2-90AE-49E0-B015-4656D30C4DF1" sourceRef="WF85599C35-6ECB-4D78-A105-9524AE04A12A" targetRef="WF4AD1DFF5-9A1D-4B5D-95D1-5ECC6D056B91"/>
        <sequenceFlow id="WF40960770-5656-4DDF-9CBD-18D8355DDEA9" sourceRef="WF62779719-FF2A-4276-8312-21AC2EF6F37E" targetRef="WF85599C35-6ECB-4D78-A105-9524AE04A12A"/>
        <sequenceFlow id="WF20594082-59CE-477E-93E9-D2ADC6C9B750" sourceRef="WFBE97D411-85A5-42CB-870D-4DE51100502E" targetRef="WF60F1C3F3-3A8B-4AC6-9F20-0BCEF38F3C6C"/>
        <sequenceFlow id="WF1CC97FFE-1B9D-4412-ACC5-C8C471376269" sourceRef="WF60F1C3F3-3A8B-4AC6-9F20-0BCEF38F3C6C" targetRef="WF235470E9-4A52-4465-A034-BCB9F4755E48"/>
        <sequenceFlow id="WF52EBB0BE-9BA1-4049-B204-7EDCD6B6C7A3" sourceRef="WF377688DB-CB5B-4CA0-9F8C-BC76EBC7351C" targetRef="WFBE97D411-85A5-42CB-870D-4DE51100502E"/>
        <sequenceFlow id="WF3AE1A97E-F45E-4BA4-A3E9-4F4021DCF5B8" sourceRef="WF4AD1DFF5-9A1D-4B5D-95D1-5ECC6D056B91" targetRef="WF377688DB-CB5B-4CA0-9F8C-BC76EBC7351C"/>
        <startEvent id="WF62779719-FF2A-4276-8312-21AC2EF6F37E" name="Start"/>
        <userTask flowable:dueDate="P1D" id="WF85599C35-6ECB-4D78-A105-9524AE04A12A" name="Process start confirmation">
            <extensionElements>
                <flowable:localization locale="en_US" name="Process start confirmation"/>
                <sasbpmn:promptDefinition promptRef="WFF6D701B1-3F61-4892-8453-5005F77FD6F1" required="false"/>
            </extensionElements>
            <potentialOwner>
                <resourceAssignmentExpression>
                    <formalExpression>user(sasdemo)</formalExpression>
                </resourceAssignmentExpression>
            </potentialOwner>
        </userTask>
        <intermediateCatchEvent id="WFD6347A29-23C0-4A56-927F-3DF26687C18A" name="Intermediate Timer">
            <timerEventDefinition>
                <timeDuration>PT1M</timeDuration>
            </timerEventDefinition>
        </intermediateCatchEvent>
        <exclusiveGateway default="WFD9A6C766-AB8A-44B9-B9D3-3D78253BB920" id="WF2F1C8B89-A541-4A88-A7FA-FE4DAAF9832F" name="Exclusive Gateway"/>
        <subProcess id="WFEEBE76D6-F895-4276-9CE2-D62A8D92F2D1" name="Quality assesment">
            <sequenceFlow id="WF2450B62D-59E0-4B0A-BE42-C8892E1C973C" sourceRef="WF3E978DE1-90ED-4ADD-93FE-FF64FAA00EB2" targetRef="WFB9025C1F-2043-44F0-B77B-FD820ACA8084"/>
            <sequenceFlow id="WF23FCCC51-6517-45A9-81B9-9603A2AA5B22" sourceRef="WF16988003-2F53-437C-925A-78BABED0A074" targetRef="WF2048BFDF-7826-42AA-93B1-6ACD012B4064"/>
            <sequenceFlow id="WF0A32074A-36DA-46BD-B019-D5BA4764E47E" sourceRef="WF1159045C-1444-4ED8-A350-67330CE0FF66" targetRef="WF2048BFDF-7826-42AA-93B1-6ACD012B4064"/>
            <sequenceFlow id="WFF263F8B3-2E69-488D-AC68-6E1559380F72" sourceRef="WF3ABCA81F-C6F0-4A10-9376-86F0EAEB6944" targetRef="WF16988003-2F53-437C-925A-78BABED0A074"/>
            <sequenceFlow id="WF853A76CA-FAFE-4445-A4D4-28FFC66F7ED9" sourceRef="WF18E5A25A-71D7-4A92-BEE1-5187C06151BB" targetRef="WF3ABCA81F-C6F0-4A10-9376-86F0EAEB6944"/>
            <sequenceFlow id="WF86A072FC-3729-4820-8A74-5991A75BED9F" sourceRef="WF1DA2CF58-95DC-4011-886E-C3582D26D705" targetRef="WF18E5A25A-71D7-4A92-BEE1-5187C06151BB"/>
            <sequenceFlow id="WF6A962F26-6E3E-46AD-84C8-A126CA68D704" sourceRef="WFE9276C88-5D19-4524-AED7-58546932BF71" targetRef="WF2048BFDF-7826-42AA-93B1-6ACD012B4064"/>
            <sequenceFlow id="WFAF97833C-E8E9-4211-A2C8-0F49CBD239EF" sourceRef="WF6D3B4E1E-4C1C-4825-8A71-669E5F38A061" targetRef="WF1159045C-1444-4ED8-A350-67330CE0FF66"/>
            <sequenceFlow id="WFE803870D-952B-4FB5-9BA6-F00B1581007F" sourceRef="WFB9025C1F-2043-44F0-B77B-FD820ACA8084" targetRef="WF18E5A25A-71D7-4A92-BEE1-5187C06151BB"/>
            <sequenceFlow id="WFB716AA7D-EAC9-4FBE-BBCE-B0F349BF3528" sourceRef="WFFDB1CD8B-E8E5-4696-99A2-6FE9813336B2" targetRef="WFE9276C88-5D19-4524-AED7-58546932BF71"/>
            <sequenceFlow id="WF81B2E128-7FD8-4802-B80A-291F24E3D72B" sourceRef="WFC0B417EB-4F6E-4FF9-B87D-695648AB0643" targetRef="WF6D3B4E1E-4C1C-4825-8A71-669E5F38A061"/>
            <startEvent id="WF3E978DE1-90ED-4ADD-93FE-FF64FAA00EB2" name="Start"/>
            <boundaryEvent attachedToRef="WFB9025C1F-2043-44F0-B77B-FD820ACA8084" cancelActivity="true" id="WF1DA2CF58-95DC-4011-886E-C3582D26D705" name="Boundary Timer">
                <timerEventDefinition>
                    <timeDuration>P1D</timeDuration>
                </timerEventDefinition>
            </boundaryEvent>
            <userTask id="WFB9025C1F-2043-44F0-B77B-FD820ACA8084" name="Select threshold for QA">
                <extensionElements>
                    <flowable:localization locale="en_US" name="Select threshold for QA"/>
                    <sasbpmn:promptDefinition promptRef="WF4E3A9345-AD93-4DD1-832B-D18467C55378" required="false">
                        <sasbpmn:promptValueDefinition promptValueRef="WF4A830ECA-BCE0-49F3-89EE-84770772FE00"/>
                        <sasbpmn:promptValueDefinition promptValueRef="WFA255A265-2715-45E4-8811-CE08A5C58670"/>
                        <sasbpmn:promptValueDefinition promptValueRef="WF74FB7E81-D679-4298-AFDE-7BEA2BA57A5B"/>
                    </sasbpmn:promptDefinition>
                </extensionElements>
                <potentialOwner>
                    <resourceAssignmentExpression>
                        <formalExpression>user(sasdemo), user(sasdemo01)</formalExpression>
                    </resourceAssignmentExpression>
                </potentialOwner>
            </userTask>
            <serviceTask flowable:delegateExpression="${notificationTask}" id="WF3ABCA81F-C6F0-4A10-9376-86F0EAEB6944" name="Send report review notification">
                <extensionElements>
                    <flowable:field name="userIds">
                        <flowable:string><![CDATA[sasdemo]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="level">
                        <flowable:string><![CDATA[info]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="templateName">
                        <flowable:string><![CDATA[MMnotifyTemplate]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="mail">
                        <flowable:string><![CDATA[false]]></flowable:string>
                    </flowable:field>
                    <flowable:localization locale="en_US" name="Send report review notification"/>
                </extensionElements>
            </serviceTask>
            <endEvent id="WF2048BFDF-7826-42AA-93B1-6ACD012B4064" name="End"/>
            <boundaryEvent attachedToRef="WF16988003-2F53-437C-925A-78BABED0A074" cancelActivity="true" id="WFC0B417EB-4F6E-4FF9-B87D-695648AB0643" name="Boundary Timer">
                <timerEventDefinition>
                    <timeDuration>PT5M</timeDuration>
                </timerEventDefinition>
            </boundaryEvent>
            <userTask id="WF16988003-2F53-437C-925A-78BABED0A074" name="Report analysis - analyst">
                <extensionElements>
                    <flowable:localization locale="en_US" name="Report analysis - analyst"/>
                    <sasbpmn:promptDefinition promptRef="WF446DB86E-FD23-491D-8456-FF0052E36D17" required="true">
                        <sasbpmn:promptValueDefinition promptValueRef="WF202E2E2B-3C23-40F0-8410-12B3478B7BFE"/>
                        <sasbpmn:promptValueDefinition promptValueRef="WF344B51E2-735E-490A-9CAC-FFAADDBC7DAF"/>
                    </sasbpmn:promptDefinition>
                </extensionElements>
                <potentialOwner>
                    <resourceAssignmentExpression>
                        <formalExpression>user(sasdemo)</formalExpression>
                    </resourceAssignmentExpression>
                </potentialOwner>
            </userTask>
            <boundaryEvent attachedToRef="WF1159045C-1444-4ED8-A350-67330CE0FF66" cancelActivity="true" id="WFFDB1CD8B-E8E5-4696-99A2-6FE9813336B2" name="Boundary Timer">
                <timerEventDefinition>
                    <timeDuration>PT5M</timeDuration>
                </timerEventDefinition>
            </boundaryEvent>
            <userTask id="WF1159045C-1444-4ED8-A350-67330CE0FF66" name="Report analysis - analyst, sr. analyst">
                <extensionElements>
                    <flowable:localization locale="en_US" name="Report analysis - analyst, sr. analyst"/>
                    <sasbpmn:promptDefinition promptRef="WF4B8FD138-1C0C-4386-BA41-2EA07BB29476" required="true">
                        <sasbpmn:promptValueDefinition promptValueRef="WF202E2E2B-3C23-40F0-8410-12B3478B7BFE"/>
                        <sasbpmn:promptValueDefinition promptValueRef="WF344B51E2-735E-490A-9CAC-FFAADDBC7DAF"/>
                    </sasbpmn:promptDefinition>
                </extensionElements>
                <potentialOwner>
                    <resourceAssignmentExpression>
                        <formalExpression>user(sasdemo), user(sasdemo01)</formalExpression>
                    </resourceAssignmentExpression>
                </potentialOwner>
            </userTask>
            <serviceTask flowable:delegateExpression="${restTask}" id="WF18E5A25A-71D7-4A92-BEE1-5187C06151BB" name="Prepare report">
                <extensionElements>
                    <flowable:field name="url">
                        <flowable:expression><![CDATA[/SASJobExecution/?_program=${taskPerfRep}]]></flowable:expression>
                    </flowable:field>
                    <flowable:field name="method">
                        <flowable:string><![CDATA[GET]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="bodyType">
                        <flowable:string><![CDATA[EMPTY]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="statusCode">
                        <flowable:string><![CDATA[200]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="headers">
                        <flowable:string><![CDATA[{}]]></flowable:string>
                    </flowable:field>
                    <flowable:localization locale="en_US" name="Prepare report"/>
                </extensionElements>
            </serviceTask>
            <serviceTask flowable:delegateExpression="${restTask}" id="WFE9276C88-5D19-4524-AED7-58546932BF71" name="Automatic model quality assurance">
                <extensionElements>
                    <flowable:field name="url">
                        <flowable:expression><![CDATA[/SASJobExecution/?_program=${taskAsses}&procid=${procId}]]></flowable:expression>
                    </flowable:field>
                    <flowable:field name="method">
                        <flowable:string><![CDATA[GET]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="bodyType">
                        <flowable:string><![CDATA[EMPTY]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="statusCode">
                        <flowable:string><![CDATA[200]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="headers">
                        <flowable:string><![CDATA[{}]]></flowable:string>
                    </flowable:field>
                    <flowable:localization locale="en_US" name="Automatic model quality assurance"/>
                </extensionElements>
            </serviceTask>
            <serviceTask flowable:delegateExpression="${notificationTask}" id="WF6D3B4E1E-4C1C-4825-8A71-669E5F38A061" name="Send report review notifications">
                <extensionElements>
                    <flowable:field name="userIds">
                        <flowable:string><![CDATA[sasdemo,sasdemo01]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="level">
                        <flowable:string><![CDATA[info]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="templateName">
                        <flowable:string><![CDATA[MMnotifyTemplate]]></flowable:string>
                    </flowable:field>
                    <flowable:field name="mail">
                        <flowable:string><![CDATA[false]]></flowable:string>
                    </flowable:field>
                    <flowable:localization locale="en_US" name="Send report review notifications"/>
                </extensionElements>
            </serviceTask>
            <textAnnotation id="WFC861788C-90EC-4572-AD2E-EE5A5E83B617">
                <text>User can set threshold for automatic model retrain</text>
            </textAnnotation>
            <textAnnotation id="WFBF981D97-52A4-4C7F-B79D-A9680EB86CED">
                <text>Prepare model quality report in Visual Analytics

</text>
            </textAnnotation>
            <textAnnotation id="WF7584834A-E440-4A3E-9C25-075E285D6AB6">
                <text>User receives a notification, 1 day is given to analyse the report</text>
            </textAnnotation>
            <textAnnotation id="WFDD408AAE-33C3-4033-98D6-5DD8E7B630FF">
                <text>Get value of PerformanceManualOk variable (analyst and sr analyst)</text>
            </textAnnotation>
            <textAnnotation id="WF9F5B6597-ACCA-4967-82A3-3903F839E76F">
                <text>Get value of PerformanceManualOk variable (analyst and sr analyst)</text>
            </textAnnotation>
            <textAnnotation id="WF2C332DF2-48D8-4217-B776-EBF0B9E16238">
                <text>Get value of 
PerformanceAutoOk 
</text>
            </textAnnotation>
            <textAnnotation id="WF2556B52E-E489-4F6A-BA26-DFB2BD121D24">
                <text>If user haven't completed the task in 1 day then go tuther</text>
            </textAnnotation>
            <textAnnotation id="WF9523F8FA-B259-497E-8A3B-5BE1869BAA6E">
                <text>Users receive a notification, 1 day is given to analyse the report</text>
            </textAnnotation>
        </subProcess>
        <serviceTask flowable:delegateExpression="${restTask}" id="WFBE97D411-85A5-42CB-870D-4DE51100502E" name="Load new data">
            <extensionElements>
                <flowable:field name="url">
                    <flowable:expression><![CDATA[/SASJobExecution/?_program=${taskNewMonthPath}&procid=${procId}]]></flowable:expression>
                </flowable:field>
                <flowable:field name="method">
                    <flowable:string><![CDATA[GET]]></flowable:string>
                </flowable:field>
                <flowable:field name="bodyType">
                    <flowable:string><![CDATA[EMPTY]]></flowable:string>
                </flowable:field>
                <flowable:field name="statusCode">
                    <flowable:string><![CDATA[200]]></flowable:string>
                </flowable:field>
                <flowable:field name="headers">
                    <flowable:string><![CDATA[{}]]></flowable:string>
                </flowable:field>
                <flowable:localization locale="en_US" name="Load new data"/>
            </extensionElements>
        </serviceTask>
        <serviceTask flowable:delegateExpression="${restTask}" id="WF235470E9-4A52-4465-A034-BCB9F4755E48" name="Score new data">
            <extensionElements>
                <flowable:field name="url">
                    <flowable:expression><![CDATA[/SASJobExecution/?_program=${taskScore}&procid=${procId}]]></flowable:expression>
                </flowable:field>
                <flowable:field name="method">
                    <flowable:string><![CDATA[GET]]></flowable:string>
                </flowable:field>
                <flowable:field name="bodyType">
                    <flowable:string><![CDATA[EMPTY]]></flowable:string>
                </flowable:field>
                <flowable:field name="statusCode">
                    <flowable:string><![CDATA[200]]></flowable:string>
                </flowable:field>
                <flowable:field name="headers">
                    <flowable:string><![CDATA[{}]]></flowable:string>
                </flowable:field>
                <flowable:localization locale="en_US" name="Score new data"/>
            </extensionElements>
        </serviceTask>
        <serviceTask flowable:delegateExpression="${restTask}" id="WF8E522432-FF68-4C78-B589-9145B332CBBA" name="Retrain model">
            <extensionElements>
                <flowable:field name="url">
                    <flowable:expression><![CDATA[/SASJobExecution/?_program=${taskTrain}&procid=${procId}]]></flowable:expression>
                </flowable:field>
                <flowable:field name="method">
                    <flowable:string><![CDATA[GET]]></flowable:string>
                </flowable:field>
                <flowable:field name="bodyType">
                    <flowable:string><![CDATA[EMPTY]]></flowable:string>
                </flowable:field>
                <flowable:field name="statusCode">
                    <flowable:string><![CDATA[200]]></flowable:string>
                </flowable:field>
                <flowable:field name="headers">
                    <flowable:string><![CDATA[{}]]></flowable:string>
                </flowable:field>
                <flowable:localization locale="en_US" name="Retrain model"/>
            </extensionElements>
        </serviceTask>
        <serviceTask flowable:delegateExpression="${restTask}" id="WF4AD1DFF5-9A1D-4B5D-95D1-5ECC6D056B91" name="Get process ID">
            <extensionElements>
                <flowable:field name="url">
                    <flowable:expression><![CDATA[/SASJobExecution/?_program=${taskGetProjectID}]]></flowable:expression>
                </flowable:field>
                <flowable:field name="method">
                    <flowable:string><![CDATA[GET]]></flowable:string>
                </flowable:field>
                <flowable:field name="bodyType">
                    <flowable:string><![CDATA[EMPTY]]></flowable:string>
                </flowable:field>
                <flowable:field name="statusCode">
                    <flowable:string><![CDATA[200]]></flowable:string>
                </flowable:field>
                <flowable:field name="headers">
                    <flowable:string><![CDATA[{}]]></flowable:string>
                </flowable:field>
                <flowable:localization locale="en_US" name="Get process ID"/>
            </extensionElements>
        </serviceTask>
        <intermediateCatchEvent id="WF377688DB-CB5B-4CA0-9F8C-BC76EBC7351C" name="Intermediate Timer">
            <timerEventDefinition>
                <timeDuration>PT5S</timeDuration>
            </timerEventDefinition>
        </intermediateCatchEvent>
        <intermediateCatchEvent id="WF60F1C3F3-3A8B-4AC6-9F20-0BCEF38F3C6C" name="Intermediate Timer">
            <timerEventDefinition>
                <timeDuration>PT5S</timeDuration>
            </timerEventDefinition>
        </intermediateCatchEvent>
        <textAnnotation id="WF0B0346A0-9B56-44AD-BA26-050080F4782A">
            <text>Execute script "python score" for new month data</text>
        </textAnnotation>
        <textAnnotation id="WF5834C638-8A10-4C36-8072-DDCB0802B8D4">
            <text>Get variavles performanceManualOk and PerformanceAutoOk </text>
        </textAnnotation>
        <textAnnotation id="WF32FCC3E8-2554-473E-9E29-240E00957549">
            <text>Update testMonth variables's value. 
Load to CAS tables with needed date range (-train, -test, -validate)
Reset PerformanceAutoOk and PerformanceManualOk</text>
        </textAnnotation>
        <textAnnotation id="WF374BB806-351D-4D45-8658-8110C655B182">
            <text>Execute script "python train" </text>
        </textAnnotation>
        <textAnnotation id="WF9BA5FF48-F531-45E8-B6FD-B349E2AF0D1D">
            <text>New month
(for demonstration purposes - 1 minute timer)</text>
        </textAnnotation>
        <textAnnotation id="WFE850159F-8955-4A5C-8AD5-7AEEC5EF983C">
            <text>User confirms that he is ready to start workflow</text>
        </textAnnotation>
        <textAnnotation id="WF8C1B7130-6EE9-428F-B732-18549429645C">
            <text>Get process ID of running workflow
</text>
        </textAnnotation>
    </process>
    <bpmndi:BPMNDiagram id="BPMNDiagram_WFA37BEF26-296E-4E9D-A0DC-C940FEA355D6">
        <bpmndi:BPMNPlane bpmnElement="WFA37BEF26-296E-4E9D-A0DC-C940FEA355D6" id="BPMNPlane_WFA37BEF26-296E-4E9D-A0DC-C940FEA355D6">
            <bpmndi:BPMNShape bpmnElement="WF62779719-FF2A-4276-8312-21AC2EF6F37E" id="BPMNShape_WF62779719-FF2A-4276-8312-21AC2EF6F37E">
                <omgdc:Bounds height="16.0" width="16.0" x="-490.0" y="-340.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF85599C35-6ECB-4D78-A105-9524AE04A12A" id="BPMNShape_WF85599C35-6ECB-4D78-A105-9524AE04A12A">
                <omgdc:Bounds height="80.0" width="120.0" x="-320.0" y="-320.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WFD6347A29-23C0-4A56-927F-3DF26687C18A" id="BPMNShape_WFD6347A29-23C0-4A56-927F-3DF26687C18A">
                <omgdc:Bounds height="16.0" width="16.0" x="-150.0" y="-40.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF2F1C8B89-A541-4A88-A7FA-FE4DAAF9832F" id="BPMNShape_WF2F1C8B89-A541-4A88-A7FA-FE4DAAF9832F">
                <omgdc:Bounds height="16.0" width="16.0" x="300.0" y="-70.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WFEEBE76D6-F895-4276-9CE2-D62A8D92F2D1" id="BPMNShape_WFEEBE76D6-F895-4276-9CE2-D62A8D92F2D1" isExpanded="false">
                <omgdc:Bounds height="80.0" width="145.0" x="300.0" y="-190.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WFBE97D411-85A5-42CB-870D-4DE51100502E" id="BPMNShape_WFBE97D411-85A5-42CB-870D-4DE51100502E">
                <omgdc:Bounds height="80.0" width="125.0" x="-130.0" y="-190.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF235470E9-4A52-4465-A034-BCB9F4755E48" id="BPMNShape_WF235470E9-4A52-4465-A034-BCB9F4755E48">
                <omgdc:Bounds height="80.0" width="120.0" x="80.0" y="-190.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF8E522432-FF68-4C78-B589-9145B332CBBA" id="BPMNShape_WF8E522432-FF68-4C78-B589-9145B332CBBA">
                <omgdc:Bounds height="80.0" width="124.0" x="300.0" y="50.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF4AD1DFF5-9A1D-4B5D-95D1-5ECC6D056B91" id="BPMNShape_WF4AD1DFF5-9A1D-4B5D-95D1-5ECC6D056B91">
                <omgdc:Bounds height="80.0" width="120.0" x="-130.0" y="-320.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF377688DB-CB5B-4CA0-9F8C-BC76EBC7351C" id="BPMNShape_WF377688DB-CB5B-4CA0-9F8C-BC76EBC7351C">
                <omgdc:Bounds height="16.0" width="16.0" x="-40.0" y="-340.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF60F1C3F3-3A8B-4AC6-9F20-0BCEF38F3C6C" id="BPMNShape_WF60F1C3F3-3A8B-4AC6-9F20-0BCEF38F3C6C">
                <omgdc:Bounds height="16.0" width="16.0" x="-40.0" y="-210.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF0B0346A0-9B56-44AD-BA26-050080F4782A" id="BPMNShape_WF0B0346A0-9B56-44AD-BA26-050080F4782A">
                <omgdc:Bounds height="80.0" width="120.0" x="80.0" y="-270.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF5834C638-8A10-4C36-8072-DDCB0802B8D4" id="BPMNShape_WF5834C638-8A10-4C36-8072-DDCB0802B8D4">
                <omgdc:Bounds height="80.0" width="144.0" x="300.0" y="-270.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF32FCC3E8-2554-473E-9E29-240E00957549" id="BPMNShape_WF32FCC3E8-2554-473E-9E29-240E00957549">
                <omgdc:Bounds height="80.0" width="269.0" x="-329.5" y="-190.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF374BB806-351D-4D45-8658-8110C655B182" id="BPMNShape_WF374BB806-351D-4D45-8658-8110C655B182">
                <omgdc:Bounds height="80.0" width="120.0" x="300.0" y="130.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF9BA5FF48-F531-45E8-B6FD-B349E2AF0D1D" id="BPMNShape_WF9BA5FF48-F531-45E8-B6FD-B349E2AF0D1D">
                <omgdc:Bounds height="80.0" width="120.0" x="-260.0" y="-20.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WFE850159F-8955-4A5C-8AD5-7AEEC5EF983C" id="BPMNShape_WFE850159F-8955-4A5C-8AD5-7AEEC5EF983C">
                <omgdc:Bounds height="80.0" width="120.0" x="-320.0" y="-400.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF8C1B7130-6EE9-428F-B732-18549429645C" id="BPMNShape_WF8C1B7130-6EE9-428F-B732-18549429645C">
                <omgdc:Bounds height="80.0" width="120.0" x="-130.0" y="-400.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="WF4A6C1D79-A9EA-4B22-8322-FF3B40F0E99D" id="BPMNEdge_WF4A6C1D79-A9EA-4B22-8322-FF3B40F0E99D">
                <omgdi:waypoint x="300.0" y="-150.0"/>
                <omgdi:waypoint x="300.0" y="-120.0"/>
                <omgdi:waypoint x="300.0" y="-120.0"/>
                <omgdi:waypoint x="300.0" y="-122.0"/>
                <omgdi:waypoint x="300.0" y="-122.0"/>
                <omgdi:waypoint x="300.0" y="-102.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF75139DF1-5396-44A5-B757-0EE8BCAB2312" id="BPMNEdge_WF75139DF1-5396-44A5-B757-0EE8BCAB2312">
                <omgdi:waypoint x="-130.0" y="-40.0"/>
                <omgdi:waypoint x="-130.0" y="-70.0"/>
                <omgdi:waypoint x="-130.0" y="-100.0"/>
                <omgdi:waypoint x="-130.0" y="-100.0"/>
                <omgdi:waypoint x="-130.0" y="-130.0"/>
                <omgdi:waypoint x="-130.0" y="-150.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF757A1923-D2E1-4D82-AA21-766A7EEE463D" id="BPMNEdge_WF757A1923-D2E1-4D82-AA21-766A7EEE463D">
                <omgdi:waypoint x="140.0" y="-190.0"/>
                <omgdi:waypoint x="170.0" y="-190.0"/>
                <omgdi:waypoint x="188.0" y="-190.0"/>
                <omgdi:waypoint x="188.0" y="-190.0"/>
                <omgdi:waypoint x="207.0" y="-190.0"/>
                <omgdi:waypoint x="227.0" y="-190.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF955B744F-54B1-490A-8ECA-897914EF4FE8" id="BPMNEdge_WF955B744F-54B1-490A-8ECA-897914EF4FE8">
                <omgdi:waypoint x="268.0" y="-70.0"/>
                <omgdi:waypoint x="238.0" y="-70.0"/>
                <omgdi:waypoint x="74.0" y="-70.0"/>
                <omgdi:waypoint x="74.0" y="-26.0"/>
                <omgdi:waypoint x="-90.0" y="-26.0"/>
                <omgdi:waypoint x="-110.0" y="-26.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WFE271E85C-38F0-4C77-B1E8-D1AF85BB540B" id="BPMNEdge_WFE271E85C-38F0-4C77-B1E8-D1AF85BB540B">
                <omgdi:waypoint x="238.0" y="50.0"/>
                <omgdi:waypoint x="208.0" y="50.0"/>
                <omgdi:waypoint x="-128.0" y="50.0"/>
                <omgdi:waypoint x="-128.0" y="19.0"/>
                <omgdi:waypoint x="-128.0" y="0.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WFD9A6C766-AB8A-44B9-B9D3-3D78253BB920" id="BPMNEdge_WFD9A6C766-AB8A-44B9-B9D3-3D78253BB920">
                <omgdi:waypoint x="300.0" y="-38.0"/>
                <omgdi:waypoint x="300.0" y="-8.0"/>
                <omgdi:waypoint x="300.0" y="-8.0"/>
                <omgdi:waypoint x="300.0" y="-10.0"/>
                <omgdi:waypoint x="300.0" y="-10.0"/>
                <omgdi:waypoint x="300.0" y="10.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WFC4341DC2-90AE-49E0-B015-4656D30C4DF1" id="BPMNEdge_WFC4341DC2-90AE-49E0-B015-4656D30C4DF1">
                <omgdi:waypoint x="-260.0" y="-320.0"/>
                <omgdi:waypoint x="-230.0" y="-320.0"/>
                <omgdi:waypoint x="-220.0" y="-320.0"/>
                <omgdi:waypoint x="-220.0" y="-320.0"/>
                <omgdi:waypoint x="-210.0" y="-320.0"/>
                <omgdi:waypoint x="-190.0" y="-320.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF40960770-5656-4DDF-9CBD-18D8355DDEA9" id="BPMNEdge_WF40960770-5656-4DDF-9CBD-18D8355DDEA9">
                <omgdi:waypoint x="-450.0" y="-320.0"/>
                <omgdi:waypoint x="-420.0" y="-320.0"/>
                <omgdi:waypoint x="-410.0" y="-320.0"/>
                <omgdi:waypoint x="-410.0" y="-320.0"/>
                <omgdi:waypoint x="-400.0" y="-320.0"/>
                <omgdi:waypoint x="-380.0" y="-320.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF20594082-59CE-477E-93E9-D2ADC6C9B750" id="BPMNEdge_WF20594082-59CE-477E-93E9-D2ADC6C9B750">
                <omgdi:waypoint x="-67.0" y="-190.0"/>
                <omgdi:waypoint x="-37.0" y="-190.0"/>
                <omgdi:waypoint x="-37.0" y="-190.0"/>
                <omgdi:waypoint x="-60.0" y="-190.0"/>
                <omgdi:waypoint x="-60.0" y="-190.0"/>
                <omgdi:waypoint x="-40.0" y="-190.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF1CC97FFE-1B9D-4412-ACC5-C8C471376269" id="BPMNEdge_WF1CC97FFE-1B9D-4412-ACC5-C8C471376269">
                <omgdi:waypoint x="0.0" y="-190.0"/>
                <omgdi:waypoint x="30.0" y="-190.0"/>
                <omgdi:waypoint x="30.0" y="-190.0"/>
                <omgdi:waypoint x="0.0" y="-190.0"/>
                <omgdi:waypoint x="0.0" y="-190.0"/>
                <omgdi:waypoint x="20.0" y="-190.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF52EBB0BE-9BA1-4049-B204-7EDCD6B6C7A3" id="BPMNEdge_WF52EBB0BE-9BA1-4049-B204-7EDCD6B6C7A3">
                <omgdi:waypoint x="-20.0" y="-300.0"/>
                <omgdi:waypoint x="-20.0" y="-270.0"/>
                <omgdi:waypoint x="-20.0" y="-260.0"/>
                <omgdi:waypoint x="-130.0" y="-260.0"/>
                <omgdi:waypoint x="-130.0" y="-250.0"/>
                <omgdi:waypoint x="-130.0" y="-230.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF3AE1A97E-F45E-4BA4-A3E9-4F4021DCF5B8" id="BPMNEdge_WF3AE1A97E-F45E-4BA4-A3E9-4F4021DCF5B8">
                <omgdi:waypoint x="-70.0" y="-320.0"/>
                <omgdi:waypoint x="-40.0" y="-320.0"/>
                <omgdi:waypoint x="-40.0" y="-320.0"/>
                <omgdi:waypoint x="-60.0" y="-320.0"/>
                <omgdi:waypoint x="-60.0" y="-320.0"/>
                <omgdi:waypoint x="-40.0" y="-320.0"/>
            </bpmndi:BPMNEdge>
        </bpmndi:BPMNPlane>
    </bpmndi:BPMNDiagram>
    <bpmndi:BPMNDiagram id="BPMNDiagram_WFEEBE76D6-F895-4276-9CE2-D62A8D92F2D1">
        <bpmndi:BPMNPlane bpmnElement="WFEEBE76D6-F895-4276-9CE2-D62A8D92F2D1" id="BPMNPlane_WFEEBE76D6-F895-4276-9CE2-D62A8D92F2D1">
            <bpmndi:BPMNEdge bpmnElement="WF2450B62D-59E0-4B0A-BE42-C8892E1C973C" id="BPMNEdge_WF2450B62D-59E0-4B0A-BE42-C8892E1C973C">
                <omgdi:waypoint x="-230.0" y="160.0"/>
                <omgdi:waypoint x="-200.0" y="160.0"/>
                <omgdi:waypoint x="-197.0" y="160.0"/>
                <omgdi:waypoint x="-197.0" y="160.0"/>
                <omgdi:waypoint x="-194.0" y="160.0"/>
                <omgdi:waypoint x="-174.0" y="160.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF23FCCC51-6517-45A9-81B9-9603A2AA5B22" id="BPMNEdge_WF23FCCC51-6517-45A9-81B9-9603A2AA5B22">
                <omgdi:waypoint x="537.0" y="160.0"/>
                <omgdi:waypoint x="567.0" y="160.0"/>
                <omgdi:waypoint x="568.0" y="160.0"/>
                <omgdi:waypoint x="568.0" y="160.0"/>
                <omgdi:waypoint x="570.0" y="160.0"/>
                <omgdi:waypoint x="590.0" y="160.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF0A32074A-36DA-46BD-B019-D5BA4764E47E" id="BPMNEdge_WF0A32074A-36DA-46BD-B019-D5BA4764E47E">
                <omgdi:waypoint x="450.0" y="330.0"/>
                <omgdi:waypoint x="450.0" y="300.0"/>
                <omgdi:waypoint x="450.0" y="292.0"/>
                <omgdi:waypoint x="450.0" y="292.0"/>
                <omgdi:waypoint x="450.0" y="236.0"/>
                <omgdi:waypoint x="603.0" y="236.0"/>
                <omgdi:waypoint x="603.0" y="200.0"/>
                <omgdi:waypoint x="603.0" y="180.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WFF263F8B3-2E69-488D-AC68-6E1559380F72" id="BPMNEdge_WFF263F8B3-2E69-488D-AC68-6E1559380F72">
                <omgdi:waypoint x="316.0" y="160.0"/>
                <omgdi:waypoint x="346.0" y="160.0"/>
                <omgdi:waypoint x="346.0" y="160.0"/>
                <omgdi:waypoint x="343.0" y="160.0"/>
                <omgdi:waypoint x="343.0" y="160.0"/>
                <omgdi:waypoint x="363.0" y="160.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF853A76CA-FAFE-4445-A4D4-28FFC66F7ED9" id="BPMNEdge_WF853A76CA-FAFE-4445-A4D4-28FFC66F7ED9">
                <omgdi:waypoint x="140.0" y="160.0"/>
                <omgdi:waypoint x="170.0" y="160.0"/>
                <omgdi:waypoint x="170.0" y="160.0"/>
                <omgdi:waypoint x="163.0" y="160.0"/>
                <omgdi:waypoint x="163.0" y="160.0"/>
                <omgdi:waypoint x="183.0" y="160.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF86A072FC-3729-4820-8A74-5991A75BED9F" id="BPMNEdge_WF86A072FC-3729-4820-8A74-5991A75BED9F">
                <omgdi:waypoint x="-138.0" y="220.0"/>
                <omgdi:waypoint x="-138.0" y="250.0"/>
                <omgdi:waypoint x="90.0" y="250.0"/>
                <omgdi:waypoint x="90.0" y="235.0"/>
                <omgdi:waypoint x="90.0" y="220.0"/>
                <omgdi:waypoint x="90.0" y="200.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF6A962F26-6E3E-46AD-84C8-A126CA68D704" id="BPMNEdge_WF6A962F26-6E3E-46AD-84C8-A126CA68D704">
                <omgdi:waypoint x="539.0" y="581.0"/>
                <omgdi:waypoint x="569.0" y="581.0"/>
                <omgdi:waypoint x="650.0" y="581.0"/>
                <omgdi:waypoint x="650.0" y="370.0"/>
                <omgdi:waypoint x="650.0" y="160.0"/>
                <omgdi:waypoint x="630.0" y="160.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WFAF97833C-E8E9-4211-A2C8-0F49CBD239EF" id="BPMNEdge_WFAF97833C-E8E9-4211-A2C8-0F49CBD239EF">
                <omgdi:waypoint x="316.0" y="370.0"/>
                <omgdi:waypoint x="346.0" y="370.0"/>
                <omgdi:waypoint x="346.0" y="370.0"/>
                <omgdi:waypoint x="343.0" y="370.0"/>
                <omgdi:waypoint x="343.0" y="370.0"/>
                <omgdi:waypoint x="363.0" y="370.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WFE803870D-952B-4FB5-9BA6-F00B1581007F" id="BPMNEdge_WFE803870D-952B-4FB5-9BA6-F00B1581007F">
                <omgdi:waypoint x="-25.0" y="160.0"/>
                <omgdi:waypoint x="4.0" y="160.0"/>
                <omgdi:waypoint x="4.0" y="160.0"/>
                <omgdi:waypoint x="0.0" y="160.0"/>
                <omgdi:waypoint x="0.0" y="160.0"/>
                <omgdi:waypoint x="20.0" y="160.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WFB716AA7D-EAC9-4FBE-BBCE-B0F349BF3528" id="BPMNEdge_WFB716AA7D-EAC9-4FBE-BBCE-B0F349BF3528">
                <omgdi:waypoint x="399.0" y="430.0"/>
                <omgdi:waypoint x="399.0" y="460.0"/>
                <omgdi:waypoint x="399.0" y="460.0"/>
                <omgdi:waypoint x="399.0" y="460.0"/>
                <omgdi:waypoint x="399.0" y="452.0"/>
                <omgdi:waypoint x="340.0" y="452.0"/>
                <omgdi:waypoint x="340.0" y="583.0"/>
                <omgdi:waypoint x="340.0" y="583.0"/>
                <omgdi:waypoint x="360.0" y="583.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="WF81B2E128-7FD8-4802-B80A-291F24E3D72B" id="BPMNEdge_WF81B2E128-7FD8-4802-B80A-291F24E3D72B">
                <omgdi:waypoint x="399.0" y="220.0"/>
                <omgdi:waypoint x="399.0" y="250.0"/>
                <omgdi:waypoint x="169.0" y="250.0"/>
                <omgdi:waypoint x="169.0" y="250.0"/>
                <omgdi:waypoint x="169.0" y="315.0"/>
                <omgdi:waypoint x="183.0" y="330.0"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNShape bpmnElement="WF3E978DE1-90ED-4ADD-93FE-FF64FAA00EB2" id="BPMNShape_WF3E978DE1-90ED-4ADD-93FE-FF64FAA00EB2">
                <omgdc:Bounds height="16.0" width="16.0" x="-270.0" y="140.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF1DA2CF58-95DC-4011-886E-C3582D26D705" id="BPMNShape_WF1DA2CF58-95DC-4011-886E-C3582D26D705">
                <omgdc:Bounds height="16.0" width="16.0" x="36.0" y="80.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WFB9025C1F-2043-44F0-B77B-FD820ACA8084" id="BPMNShape_WFB9025C1F-2043-44F0-B77B-FD820ACA8084">
                <omgdc:Bounds height="80.0" width="149.0" x="-100.0" y="160.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF3ABCA81F-C6F0-4A10-9376-86F0EAEB6944" id="BPMNShape_WF3ABCA81F-C6F0-4A10-9376-86F0EAEB6944">
                <omgdc:Bounds height="80.0" width="133.0" x="250.0" y="160.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF2048BFDF-7826-42AA-93B1-6ACD012B4064" id="BPMNShape_WF2048BFDF-7826-42AA-93B1-6ACD012B4064">
                <omgdc:Bounds height="16.0" width="16.0" x="590.0" y="140.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WFC0B417EB-4F6E-4FF9-B87D-695648AB0643" id="BPMNShape_WFC0B417EB-4F6E-4FF9-B87D-695648AB0643">
                <omgdc:Bounds height="16.0" width="16.0" x="36.0" y="80.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF16988003-2F53-437C-925A-78BABED0A074" id="BPMNShape_WF16988003-2F53-437C-925A-78BABED0A074">
                <omgdc:Bounds height="80.0" width="174.0" x="450.0" y="160.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WFFDB1CD8B-E8E5-4696-99A2-6FE9813336B2" id="BPMNShape_WFFDB1CD8B-E8E5-4696-99A2-6FE9813336B2">
                <omgdc:Bounds height="16.0" width="16.0" x="36.0" y="80.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF1159045C-1444-4ED8-A350-67330CE0FF66" id="BPMNShape_WF1159045C-1444-4ED8-A350-67330CE0FF66">
                <omgdc:Bounds height="80.0" width="173.0" x="450.0" y="370.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF18E5A25A-71D7-4A92-BEE1-5187C06151BB" id="BPMNShape_WF18E5A25A-71D7-4A92-BEE1-5187C06151BB">
                <omgdc:Bounds height="80.0" width="120.0" x="80.0" y="160.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WFE9276C88-5D19-4524-AED7-58546932BF71" id="BPMNShape_WFE9276C88-5D19-4524-AED7-58546932BF71">
                <omgdc:Bounds height="80.0" width="179.0" x="450.0" y="580.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF6D3B4E1E-4C1C-4825-8A71-669E5F38A061" id="BPMNShape_WF6D3B4E1E-4C1C-4825-8A71-669E5F38A061">
                <omgdc:Bounds height="80.0" width="133.0" x="250.0" y="370.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WFC861788C-90EC-4572-AD2E-EE5A5E83B617" id="BPMNShape_WFC861788C-90EC-4572-AD2E-EE5A5E83B617">
                <omgdc:Bounds height="80.0" width="145.0" x="-100.0" y="80.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WFBF981D97-52A4-4C7F-B79D-A9680EB86CED" id="BPMNShape_WFBF981D97-52A4-4C7F-B79D-A9680EB86CED">
                <omgdc:Bounds height="80.0" width="120.0" x="77.5" y="80.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF7584834A-E440-4A3E-9C25-075E285D6AB6" id="BPMNShape_WF7584834A-E440-4A3E-9C25-075E285D6AB6">
                <omgdc:Bounds height="80.0" width="132.0" x="250.0" y="80.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WFDD408AAE-33C3-4033-98D6-5DD8E7B630FF" id="BPMNShape_WFDD408AAE-33C3-4033-98D6-5DD8E7B630FF">
                <omgdc:Bounds height="80.0" width="165.0" x="450.0" y="80.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF9F5B6597-ACCA-4967-82A3-3903F839E76F" id="BPMNShape_WF9F5B6597-ACCA-4967-82A3-3903F839E76F">
                <omgdc:Bounds height="80.0" width="165.0" x="450.0" y="290.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF2C332DF2-48D8-4217-B776-EBF0B9E16238" id="BPMNShape_WF2C332DF2-48D8-4217-B776-EBF0B9E16238">
                <omgdc:Bounds height="80.0" width="176.0" x="450.0" y="500.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF2556B52E-E489-4F6A-BA26-DFB2BD121D24" id="BPMNShape_WF2556B52E-E489-4F6A-BA26-DFB2BD121D24">
                <omgdc:Bounds height="80.0" width="223.0" x="-20.0" y="300.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="WF9523F8FA-B259-497E-8A3B-5BE1869BAA6E" id="BPMNShape_WF9523F8FA-B259-497E-8A3B-5BE1869BAA6E">
                <omgdc:Bounds height="80.0" width="132.0" x="250.0" y="290.0"/>
            </bpmndi:BPMNShape>
        </bpmndi:BPMNPlane>
    </bpmndi:BPMNDiagram>
</definitions>
