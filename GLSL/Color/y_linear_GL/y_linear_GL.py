# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named y_linear_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from y_linear_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "y_linear_GL"

def getLabel():
    return "y_linear_GL"

def getVersion():
    return 1

def getIconPath():
    return "y_linear_GL.png"

def getGrouping():
    return "Community/GLSL/Color"

def getPluginDescription():
    return "Convert footage to linear and back with ease."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.2941, 0.5294, 1)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
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

    param = lastNode.createSeparatorParam("SETUP", "Setup")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.SETUP = param
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

    param = lastNode.createChoiceParam("colorspaceChoice", "Colorspace : ")
    entries = [ ("Rec 709", ""),
    ("sRGB", ""),
    ("Linear", ""),
    ("2.2 Gamma", ""),
    ("1.8 Gamma", ""),
    ("LogC V3", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.colorspaceChoice = param
    del param

    param = lastNode.createBooleanParam("Shadertoy2paramValueBool1", "Invert : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueBool1 = param
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

    param = lastNode.createSeparatorParam("OPTION", "Option")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.OPTION = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

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
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createBooleanParam("DivMult", "Pre-Div / Post-Mult : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.DivMult = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

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
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "y_linear_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE01", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE01 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(90, 36)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3691)
    lastNode.setSize(90, 36)
    lastNode.setColor(1, 1, 1)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy2")
    lastNode.setLabel("Shadertoy2")
    lastNode.setPosition(4139, 3863)
    lastNode.setSize(90, 36)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy2 = lastNode

    param = lastNode.getParam("paramValueInt0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueBool1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : y_linear Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : y_linear Matchbox for Autodesk Flame\n\n\n// iChannel0:Source,filter=nearest,wrap=clamp\n// BBox: iChannel0\n\n\n\n#define luma(col) dot(col, vec3(0.2126, 0.7152, 0.0722))\n#define PI 3.141592653589793238462643383279502884197969\n\n\nfloat ratio = iResolution.x/iResolution.y;\n\nvec2 res = vec2(iResolution.x, iResolution.y);\nvec2 texel = vec2(1.0) / res;\n\n\nuniform int i_colorspace = 0; // Colorspace (Working colorspace. Set this to the current working colorspace. This insures a linear blur (no dark edges)), min=0, max=6\nuniform bool invert = false; // Invert\n\nvec4 from_sRGB(vec4 col)\n{\n    if (col.r >= 0.0) {\n         col.r = pow((col.r +.055)/ 1.055, 2.4);\n    }\n\n    if (col.g >= 0.0) {\n         col.g = pow((col.g +.055)/ 1.055, 2.4);\n    }\n\n    if (col.b >= 0.0) {\n         col.b = pow((col.b +.055)/ 1.055, 2.4);\n    }\n\n    return col;\n}\n\nvec4 from_rec709(vec4 col)\n{\n    if (col.r < .081) {\n         col.r /= 4.5;\n    } else {\n         col.r = pow((col.r +.099)/ 1.099, 1.0 / .45);\n    }\n\n    if (col.g < .081) {\n         col.g /= 4.5;\n    } else {\n         col.g = pow((col.g +.099)/ 1.099, 1.0 / .45);\n    }\n\n    if (col.b < .081) {\n         col.b /= 4.5;\n    } else {\n         col.b = pow((col.b +.099)/ 1.099, 1.0 / .45);\n    }\n\n    return col;\n}\n\nvec4 to_rec709(vec4 col)\n{\n    if (col.r < .018) {\n         col.r *= 4.5;\n    } else if (col.r >= 0.0) {\n         col.r = (1.099 * pow(col.r, .45)) - .099;\n    }\n\n    if (col.g < .018) {\n         col.g *= 4.5;\n    } else if (col.g >= 0.0) {\n         col.g = (1.099 * pow(col.g, .45)) - .099;\n    }\n\n    if (col.b < .018) {\n         col.b *= 4.5;\n    } else if (col.b >= 0.0) {\n         col.b = (1.099 * pow(col.b, .45)) - .099;\n    }\n\n\n    return col;\n}\n\nvec4 to_sRGB(vec4 col)\n{\n    if (col.r >= 0.0) {\n         col.r = (1.055 * pow(col.r, 1.0 / 2.4)) - .055;\n    }\n\n    if (col.g >= 0.0) {\n         col.g = (1.055 * pow(col.g, 1.0 / 2.4)) - .055;\n    }\n\n    if (col.b >= 0.0) {\n         col.b = (1.055 * pow(col.b, 1.0 / 2.4)) - .055;\n    }\n\n    return col;\n}\n\nvec4 adjust_gamma(vec4 col, float gamma)\n{\n    col.r = pow(col.r, gamma);\n    col.g = pow(col.g, gamma);\n    col.b = pow(col.b, gamma);\n\n    return col;\n}\n\nvec4 from_logc(vec4 col)\n{\n    float cut = .010591;\n    float a = 5.555556;\n    float b = .052272;\n    float c = 0.247190;\n    float d = 0.385537;\n    float e = 5.367655;\n    float f = 0.092809;\n    float e_cut_f = 0.149658;\n\n    if (col.r > e_cut_f) {\n        col.r = (pow(10, (col.r -d) / c) - b) / a;\n    } else {\n        col.r = (col.r - f) / e;\n    }\n \n    if (col.g > e_cut_f) {\n        col.g = (pow(10, (col.g -d) / c) - b) / a;\n    } else {\n        col.g = (col.g - f) / e;\n    }\n \n    if (col.b > e_cut_f) {\n        col.b = (pow(10, (col.b -d) / c) - b) / a;\n    } else {\n        col.b = (col.b - f) / e;\n    }\n    \n    return col;\n}\n\nfloat log10(float c)\n{\n    return log(c) / 2.3026;\n}\n\nvec4 to_logc(vec4 col)\n{\n    float cut = .010591;\n    float a = 5.555556;\n    float b = .052272;\n    float c = 0.247190;\n    float d = 0.385537;\n    float e = 5.367655;\n    float f = 0.092809;\n    float e_cut_f = 0.149658;\n\n    if (col.r > cut) {\n        col.r = c * log10(a * col.r + b) + d;\n    } else {\n        col.r = e * col.r + f;\n    }\n\n    if (col.g > cut) {\n        col.g = c * log10(a * col.g + b) + d;\n    } else {\n        col.g = e * col.g + f;\n    }\n\n    if (col.b > cut) {\n        col.b = c * log10(a * col.b + b) + d;\n    } else {\n        col.b = e * col.b + f;\n    }\n\n    return col;\n}\n\n\nvec4 do_colorspace(vec4 front, int op)\n{\n    if (op == 0)\n    {\n        if (i_colorspace == 0) {\n            front = from_rec709(front);\n        } else if (i_colorspace == 1) {\n            front = from_sRGB(front);\n        } else if (i_colorspace == 2) {\n            //linear\n        } else if (i_colorspace == 3) {\n            front = adjust_gamma(front, 2.2);\n        } else if (i_colorspace == 4) {\n            front = adjust_gamma(front, 1.8);\n        } else if (i_colorspace == 5) {\n            front = from_logc(front);\n        }\n    }\n    else if (op == 1)\n    {\n        if (i_colorspace == 0) {\n            front = to_rec709(front);\n        } else if (i_colorspace == 1) {\n            front = to_sRGB(front);\n        } else if (i_colorspace == 2) {\n            //linear\n        } else if (i_colorspace == 3) {\n            front = adjust_gamma(front, 1.0 / 2.2);\n        } else if (i_colorspace == 4) {\n            front = adjust_gamma(front, 1.0 / 1.8);\n        } else if (i_colorspace == 5) {\n            front = to_logc(front);\n        }\n    }\n\n    return front;\n}\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n    vec2 st = fragCoord.xy / res;\n\n    vec4 front = texture2D(iChannel0, st);\n    if (invert) {\n        front = do_colorspace(front, 1);\n    } else {\n        front = do_colorspace(front, 0);\n    }\n\n    fragColor = front;\n\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("wrap0")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("i_colorspace")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Colorspace")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("Working colorspace. Set this to the current working colorspace. This insures a linear blur (no dark edges)")
        del param

    param = lastNode.getParam("paramMinInt0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxInt0")
    if param is not None:
        param.setValue(6, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("invert")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Invert")
        del param

    del lastNode
    # End of node "Shadertoy2"

    # Start of node "Premult1"
    lastNode = app.createNode("net.sf.openfx.Premult", 2, group)
    lastNode.setScriptName("Premult1")
    lastNode.setLabel("Premult1")
    lastNode.setPosition(4139, 3941)
    lastNode.setSize(90, 36)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupPremult1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Premult1"

    # Start of node "Unpremult1"
    lastNode = app.createNode("net.sf.openfx.Unpremult", 2, group)
    lastNode.setScriptName("Unpremult1")
    lastNode.setLabel("Unpremult1")
    lastNode.setPosition(4139, 3787)
    lastNode.setSize(90, 36)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupUnpremult1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Unpremult1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupPremult1)
    groupShadertoy2.connectInput(0, groupUnpremult1)
    groupPremult1.connectInput(0, groupShadertoy2)
    groupUnpremult1.connectInput(0, groupSource)

    param = groupShadertoy2.getParam("paramValueInt0")
    param.setExpression("thisGroup.colorspaceChoice.get()", False, 0)
    del param
    param = groupShadertoy2.getParam("paramValueBool1")
    group.getParam("Shadertoy2paramValueBool1").setAsAlias(param)
    del param
    param = groupPremult1.getParam("disableNode")
    param.setExpression("not thisGroup.DivMult.get()", False, 0)
    del param
    param = groupUnpremult1.getParam("disableNode")
    param.setExpression("not thisGroup.DivMult.get()", False, 0)
    del param

    try:
        extModule = sys.modules["y_linear_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
