# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named ZCombineExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from ZCombineExt import *
except ImportError:
    pass

def getPluginID():
    return "CommunityPyPlug.Zcombine"

def getLabel():
    return "ZCombine"

def getVersion():
    return 1

def getIconPath():
    return "ZCombine.png"

def getGrouping():
    return "Merge"

def getPluginDescription():
    return "Merge Color A and Color B according to their Z pass.\nUse the Z channel Selector to define were to pick Z from. \nYou can output the combined Z pass, note that won\'t work if you\'re using mask or mix."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createChoiceParam("ZChannel", "Channel used for Z")
    entries = [ ("RGBA.R", ""),
    ("RGBA.G", ""),
    ("RGBA.B", ""),
    ("RGBA.A", "")]
    param.setOptions(entries)
    del entries
    param.setDefaultValue("RGBA.A")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("The Channel were to pick Z from")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.set("RGBA.R")
    lastNode.ZChannel = param
    del param

    param = lastNode.createBooleanParam("OutputZ", "Output Z")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Output Z instead of Color")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.OutputZ = param
    del param

    param = lastNode.createBooleanParam("Invert", "Invert Operation")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Invert the combine operation")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Invert = param
    del param

    param = lastNode.createSeparatorParam("Sep", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistant(False)
    param.setEvaluateOnChange(False)
    lastNode.Sep = param
    del param

    param = lastNode.createBooleanParam("Merge1enableMask_Mask", "Mask")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.Merge1enableMask_Mask = param
    del param

    param = lastNode.createChoiceParam("Merge1maskChannel_Mask", "")
    param.setDefaultValue(4)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.Merge1maskChannel_Mask = param
    del param

    param = lastNode.createBooleanParam("Merge1maskInvert", "Invert Mask")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.Merge1maskInvert = param
    del param

    param = lastNode.createDoubleParam("Merge1mix", "Mix")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Merge1mix = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Node', 'Settings', 'Info'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Zcombine_exp"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Zcombine_exp")
    lastNode.setLabel("Zcombine_exp")
    lastNode.setPosition(738, 274)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupZcombine_exp = lastNode

    param = lastNode.getParam("paramValueInt0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueBool1")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueInt1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueInt2")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("uniform int Channel = 0; // What channel is used as Z pass ?\nuniform int Invert = 0 ; // Invert the operation\nuniform int Zout = 0 ; // Output Z instead of color\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tvec2 uv = fragCoord.xy / iResolution.xy;\n\tvec4 ima = texture2D(iChannel1, uv.xy).rgba;\n\tvec4 imb = texture2D(iChannel3, uv.xy).rgba;\n\tfloat za=0.0;\n\tfloat zb=0.0;\n\nif (Channel == 0) {\n\t\tza = texture2D(iChannel0, uv.xy).r;\n\t\tzb = texture2D(iChannel2, uv.xy).r;\n\t\t}\n\nif (Channel == 1) {\n\t\tza = texture2D(iChannel0, uv.xy).g;\n\t\tzb = texture2D(iChannel2, uv.xy).g;\n\t\t}\n\nif (Channel == 2) {\n\t\tza = texture2D(iChannel0, uv.xy).b;\n\t\tzb = texture2D(iChannel2, uv.xy).b;\n\t\t}\n\nif (Channel == 3) {\n\t\tza = texture2D(iChannel0, uv.xy).a;\n\t\tzb = texture2D(iChannel2, uv.xy).a;\n\t\t}\n\n\tvec4 col=imb;\n\tfloat z=zb;\n\nif (Invert == 1)  {if (za > zb) col=ima;};\nif (Invert == 0)  {if (za < zb) col=ima;};\n\nif (Invert == 1)  {if (za > zb) z=za;};\nif (Invert == 0)  {if (za < zb) z=za;};\n\nif (Zout==1) col=vec4(z,z,z,1.);\n\n    fragColor =col ;\n}")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("Channel")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("What channel is used as Z pass ?")
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("Invert")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Invert the operation")
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("Zout")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Output Z instead of color")
        del param

    del lastNode
    # End of node "Zcombine_exp"

    # Start of node "Z_A"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Z_A")
    lastNode.setLabel("Z_A")
    lastNode.setPosition(1096, 54)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupZ_A = lastNode

    del lastNode
    # End of node "Z_A"

    # Start of node "Color_A"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Color_A")
    lastNode.setLabel("Color_A")
    lastNode.setPosition(889, 63)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupColor_A = lastNode

    del lastNode
    # End of node "Color_A"

    # Start of node "Z_B"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Z_B")
    lastNode.setLabel("Z_B")
    lastNode.setPosition(703, 56)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupZ_B = lastNode

    del lastNode
    # End of node "Z_B"

    # Start of node "Color_B"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Color_B")
    lastNode.setLabel("Color_B")
    lastNode.setPosition(500, 68)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupColor_B = lastNode

    del lastNode
    # End of node "Color_B"

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setScriptName("Output2")
    lastNode.setLabel("Output2")
    lastNode.setPosition(726, 825)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(726, 454)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("copy")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("copy")
        del param

    param = lastNode.getParam("maskInvert")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(545, 389)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Mask")
    lastNode.setLabel("Mask")
    lastNode.setPosition(1109, 466)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupMask = lastNode

    param = lastNode.getParam("optional")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("isMask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Mask"

    # Start of node "Switch1"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch1")
    lastNode.setLabel("Switch1")
    lastNode.setPosition(500, 267)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupZcombine_exp.connectInput(0, groupZ_A)
    groupZcombine_exp.connectInput(1, groupColor_A)
    groupZcombine_exp.connectInput(2, groupZ_B)
    groupZcombine_exp.connectInput(3, groupColor_B)
    groupOutput2.connectInput(0, groupMerge1)
    groupMerge1.connectInput(0, groupDot1)
    groupMerge1.connectInput(1, groupZcombine_exp)
    groupMerge1.connectInput(2, groupMask)
    groupDot1.connectInput(0, groupSwitch1)
    groupSwitch1.connectInput(0, groupColor_B)
    groupSwitch1.connectInput(1, groupZ_B)

    param = groupZcombine_exp.getParam("paramValueInt0")
    param.setExpression("thisGroup.ZChannel.get()", False, 0)
    del param
    param = groupZcombine_exp.getParam("paramValueInt1")
    param.setExpression("thisGroup.Invert.get()", False, 0)
    del param
    param = groupZcombine_exp.getParam("paramValueInt2")
    param.setExpression("thisGroup.OutputZ.get()", False, 0)
    del param
    param = groupMerge1.getParam("maskInvert")
    group.getParam("Merge1maskInvert").setAsAlias(param)
    del param
    param = groupMerge1.getParam("mix")
    group.getParam("Merge1mix").setAsAlias(param)
    del param
    param = groupMerge1.getParam("enableMask_Mask")
    group.getParam("Merge1enableMask_Mask").setAsAlias(param)
    del param
    param = groupMerge1.getParam("maskChannel_Mask")
    group.getParam("Merge1maskChannel_Mask").setAsAlias(param)
    del param
    param = groupSwitch1.getParam("which")
    param.setExpression("thisGroup.OutputZ.get()", False, 0)
    del param

    try:
        extModule = sys.modules["ZCombineExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
