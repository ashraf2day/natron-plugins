# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named L_IcolorExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from L_IcolorExt import *
except ImportError:
    pass

ef getPluginID():
    return "natron.community.plugins.L_Icolor"

def getLabel():
    return "L_Icolor"

def getVersion():
    return 1

def getIconPath():
    return "L_Icolor.png"

def getGrouping():
    return "Community/Color"

    def getPluginDescription():
    return "Tint an image from the A input using another one from the B input."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "L_Icolor")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createDoubleParam("Dissolve1which", "Which")
    param.setMinimum(0, 0)
    param.setMaximum(63, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Dissolve1which = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createChoiceParam("MergeBBoxbbox", "Bounding Box")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.MergeBBoxbbox = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createBooleanParam("operationsInLog", "operationsInLog")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.operationsInLog = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createSeparatorParam("Name", "L_Icolor")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.Name = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createSeparatorParam("line03", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line03 = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createSeparatorParam("CR_FR", "Version NATRON des Gizmos Nuke d�velopp�s par Luma Pictures")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CR_FR = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createStringParam("sep18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep18 = param
    del param

    param = lastNode.createSeparatorParam("CR_EN", "NATRON version of Nuke Gizmos developed by Luma Pictures")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CR_EN = param
    del param

    param = lastNode.createStringParam("sep19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep19 = param
    del param

    param = lastNode.createStringParam("sep20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep20 = param
    del param

    param = lastNode.createSeparatorParam("FF", "(Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FF = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "A"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("A")
    lastNode.setLabel("A")
    lastNode.setPosition(760, -118)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupA = lastNode

    del lastNode
    # End of node "A"

    # Start of node "B"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("B")
    lastNode.setLabel("B")
    lastNode.setPosition(1289, -126)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupB = lastNode

    del lastNode
    # End of node "B"

    # Start of node "Lin2Log1"
    lastNode = app.createNode("net.sf.openfx.Log2Lin", 1, group)
    lastNode.setScriptName("Lin2Log1")
    lastNode.setLabel("Lin2Log1")
    lastNode.setPosition(760, 19)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.48, 0.66, 1)
    groupLin2Log1 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("lin2log")
        del param

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Lin2Log1"

    # Start of node "Lin2Log2"
    lastNode = app.createNode("net.sf.openfx.Log2Lin", 1, group)
    lastNode.setScriptName("Lin2Log2")
    lastNode.setLabel("Lin2Log2")
    lastNode.setPosition(1289, 12)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.48, 0.66, 1)
    groupLin2Log2 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("lin2log")
        del param

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Lin2Log2"

    # Start of node "Multiply1"
    lastNode = app.createNode("net.sf.openfx.MultiplyPlugin", 2, group)
    lastNode.setScriptName("Multiply1")
    lastNode.setLabel("Multiply1")
    lastNode.setPosition(862, 204)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.48, 0.66, 1)
    groupMultiply1 = lastNode

    param = lastNode.getParam("value")
    if param is not None:
        param.setValue(-1, 0)
        param.setValue(-1, 1)
        param.setValue(-1, 2)
        param.setValue(-1, 3)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Multiply1"

    # Start of node "Multiply1_2"
    lastNode = app.createNode("net.sf.openfx.MultiplyPlugin", 2, group)
    lastNode.setScriptName("Multiply1_2")
    lastNode.setLabel("Multiply1_2")
    lastNode.setPosition(1135, 200)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.48, 0.66, 1)
    groupMultiply1_2 = lastNode

    param = lastNode.getParam("value")
    if param is not None:
        param.setValue(-1, 0)
        param.setValue(-1, 1)
        param.setValue(-1, 2)
        param.setValue(-1, 3)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Multiply1_2"

    # Start of node "SeExprSimple1"
    lastNode = app.createNode("fr.inria.openfx.SeExprSimple", 2, group)
    lastNode.setScriptName("SeExprSimple1")
    lastNode.setLabel("SeExprSimple1")
    lastNode.setPosition(1289, 102)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSeExprSimple1 = lastNode

    param = lastNode.getParam("rExpr")
    if param is not None:
        param.setValue("(1/(r*.3+g*.59+b*.11))*r")
        del param

    param = lastNode.getParam("gExpr")
    if param is not None:
        param.setValue("(1/(r*.3+g*.59+b*.11))*g")
        del param

    param = lastNode.getParam("bExpr")
    if param is not None:
        param.setValue("(1/(r*.3+g*.59+b*.11))*b")
        del param

    del lastNode
    # End of node "SeExprSimple1"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(1001, 192)
    lastNode.setSize(80, 73)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("multiply")
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "Merge1_2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1_2")
    lastNode.setLabel("Merge1_2")
    lastNode.setPosition(765, 471)
    lastNode.setSize(80, 73)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1_2 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("multiply")
        del param

    del lastNode
    # End of node "Merge1_2"

    # Start of node "Merge1_3"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1_3")
    lastNode.setLabel("Merge1_3")
    lastNode.setPosition(1001, 471)
    lastNode.setSize(80, 73)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1_3 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("max")
        del param

    del lastNode
    # End of node "Merge1_3"

    # Start of node "MergeBBox"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("MergeBBox")
    lastNode.setLabel("MergeBBox")
    lastNode.setPosition(1289, 491)
    lastNode.setSize(80, 73)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMergeBBox = lastNode

    del lastNode
    # End of node "MergeBBox"

    # Start of node "Dissolve1"
    lastNode = app.createNode("net.sf.openfx.DissolvePlugin", 1, group)
    lastNode.setScriptName("Dissolve1")
    lastNode.setLabel("Dissolve1")
    lastNode.setPosition(630, 567)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupDissolve1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(1, 0)
        del param

    del lastNode
    # End of node "Dissolve1"

    # Start of node "Log2Lin1"
    lastNode = app.createNode("net.sf.openfx.Log2Lin", 1, group)
    lastNode.setScriptName("Log2Lin1")
    lastNode.setLabel("Log2Lin1")
    lastNode.setPosition(630, 767)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.48, 0.66, 1)
    groupLog2Lin1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Log2Lin1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(798, 221)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(1322, 217)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Output1_2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1_2")
    lastNode.setPosition(630, 994)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1_2 = lastNode

    del lastNode
    # End of node "Output1_2"

    # Start of node "Crop1_2"
    lastNode = app.createNode("net.sf.openfx.CropPlugin", 1, group)
    lastNode.setScriptName("Crop1_2")
    lastNode.setLabel("Crop1_2")
    lastNode.setPosition(630, 666)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupCrop1_2 = lastNode

    param = lastNode.getParam("rectangleInteractEnable")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(1950, 0)
        param.setValue(1200, 1)
        del param

    param = lastNode.getParam("reformat")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Crop1_2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupLin2Log1.connectInput(0, groupA)
    groupLin2Log2.connectInput(0, groupB)
    groupMultiply1.connectInput(0, groupDot1)
    groupMultiply1_2.connectInput(0, groupDot2)
    groupSeExprSimple1.connectInput(0, groupLin2Log2)
    groupMerge1.connectInput(0, groupMultiply1)
    groupMerge1.connectInput(1, groupMultiply1_2)
    groupMerge1_2.connectInput(0, groupDot2)
    groupMerge1_2.connectInput(1, groupDot1)
    groupMerge1_3.connectInput(0, groupMerge1_2)
    groupMerge1_3.connectInput(1, groupMerge1)
    groupMergeBBox.connectInput(0, groupDot2)
    groupMergeBBox.connectInput(1, groupLin2Log1)
    groupDissolve1.connectInput(0, groupDot1)
    groupDissolve1.connectInput(1, groupMerge1_3)
    groupLog2Lin1.connectInput(0, groupCrop1_2)
    groupDot1.connectInput(0, groupLin2Log1)
    groupDot2.connectInput(0, groupSeExprSimple1)
    groupOutput1_2.connectInput(0, groupLog2Lin1)
    groupCrop1_2.connectInput(0, groupDissolve1)

    param = groupLin2Log1.getParam("disableNode")
    param.setExpression("not thisGroup.operationsInLog.get()", False, 0)
    del param
    param = groupLin2Log2.getParam("disableNode")
    param.setExpression("not thisGroup.operationsInLog.get()", False, 0)
    del param
    param = groupMergeBBox.getParam("bbox")
    group.getParam("MergeBBoxbbox").setAsAlias(param)
    del param
    param = groupDissolve1.getParam("which")
    group.getParam("Dissolve1which").setAsAlias(param)
    del param
    param = groupLog2Lin1.getParam("disableNode")
    param.setExpression("not thisGroup.operationsInLog.get()", False, 0)
    del param
    param = groupCrop1_2.getParam("size")
    param.setExpression("rod = MergeBBox.getRegionOfDefinition(frame,view)\nret = rod.width()", True, 0)
    param.setExpression("rod = MergeBBox.getRegionOfDefinition(frame,view)\nret = rod.height()", True, 1)
    del param

    try:
        extModule = sys.modules["L_IcolorExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)