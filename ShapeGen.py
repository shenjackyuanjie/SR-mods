import math

f = open("/storage/emulated/0/Android/data/com.jundroo.simplerockets/files/ships/Shape.xml", "w+")


def PodHed():
    f.write("<Ship version=\"1\" liftedOff=\"0\" touchingGround=\"0\">\n")
    f.write("    <DisconnectedParts/>\n")
    f.write("    <Parts>\n")
    f.write(
        "        <Part partType=\"pod-1\" id=\"1\" x=\"0.000000\" y=\"-2.000000\" angle=\"0.000000\" angleV=\"0.000000\" editorAngle=\"0\">\n")
    f.write("            <Pod throttle=\"0.000000\" name=\"\">\n")
    f.write("                <Staging currentStage=\"0\"/>\n")
    f.write("            </Pod>\n")
    f.write("        </Part>\n")


def ConGen(num):
    f.write("    <Connections>\n")
    f.write("        <Connection parentAttachPoint=\"1\" childAttachPoint=\"1\" parentPart=\"1\" childPart=\"2\"/>\n")
    for i in range(3, num + 3):
        f.write(
            "        <Connection parentAttachPoint=\"1\" childAttachPoint=\"1\" parentPart=\"2\" childPart=\"%d\"/>\n" % (
                i))
    f.write("    </Connections>\n")
    f.write("</Ship>\n")
    print("")
    print("Finished.")
    print("File \"Shape.xml\" have generated.")
    print("")


def NukGen(num):
    num *= 4
    PodHed()
    f.write(
        "        <Part partType=\"parachute-1\" id=\"2\" x=\"0.000000\" y=\"0.250000\" angle=\"0.000000\" angleV=\"0.000000\" editorAngle=\"0\" activated=\"0\" exploded=\"0\" flippedX=\"0\" flippedY=\"0\" chuteX=\"0.000000\" chuteY=\"0.250000\" chuteAngle=\"0.000000\" chuteHeight=\"0.000000\" inflation=\"0.100000\" inflate=\"0\" deployed=\"0\" rope=\"0\"/>\n")
    for i in range(3, num, 4):
        f.write(
            "        <Part partType=\"nosecone-1\" id=\"%d\" x=\"0.000000\" y=\"0.500000\" angle=\"0.000000\" angleV=\"0.000000\" editorAngle=\"0\" activated=\"0\" exploded=\"0\" flippedX=\"0\" flippedY=\"0\"/>\n" % (
                i))
        f.write(
            "        <Part partType=\"nosecone-1\" id=\"%d\" x=\"0.000000\" y=\"-0.500000\" angle=\"3.141593\" angleV=\"0.000000\" editorAngle=\"2\" activated=\"0\" exploded=\"0\" flippedX=\"0\" flippedY=\"0\"/>\n" % (
                        i + 1))
        f.write(
            "        <Part partType=\"nosecone-1\" id=\"%d\" x=\"0.500000\" y=\"0.000000\" angle=\"4.712389\" angleV=\"0.000000\" editorAngle=\"3\" activated=\"0\" exploded=\"0\" flippedX=\"0\" flippedY=\"0\"/>\n" % (
                        i + 2))
        f.write(
            "        <Part partType=\"nosecone-1\" id=\"%d\" x=\"-0.500000\" y=\"0.000000\" angle=\"1.570796\" angleV=\"0.000000\" editorAngle=\"1\" activated=\"0\" exploded=\"0\" flippedX=\"0\" flippedY=\"0\"/>\n" % (
                        i + 3))
    f.write("    </Parts>\n")
    ConGen(num)


def RudGen(l, r):
    a = float(l) / float(r)
    m = 2 * math.pi / a
    PodHed()
    i = 2
    x = 0
    y = 0
    al = 0
    PatCho(int(PPa), i, x, y, al)
    for i in range(3, int(m) + 3):
        tmp = i - 2
        alo = a * tmp
        x = float(r) * math.cos(alo)
        y = float(r) * math.sin(alo)
        al = 3 * math.pi / 2 + alo
        PatCho(int(CPa), i, x, y, al)
    f.write("</Parts>\n")
    ConGen(int(m))


def LenCho(num):
    if num == 1:
        l = 1
    elif num == 2:
        l = 8
    elif num == 3:
        l = 2
    elif num == 4:
        l = 2
    elif num == 5:
        l = 1
    return l


def PatNum():
    print("    1 wheel")
    print("    2 strut")
    print("    3 parachute")
    print("    4 nosecone")
    print("    5 dock plug")


def PatCho(num, i, x, y, al):
    if num == 1:
        f.write(
            "        <Part partType=\"wheel-2\" id=\"%d\" x=\"%f\" y=\"%f\" angle=\"%f\" angleV=\"0.000000\" editorAngle=\"0\" activated=\"0\" exploded=\"0\" flippedX=\"0\" flippedY=\"0\"/>\n" % (
            i, x, y, al))
    elif num == 2:
        f.write(
            "        <Part partType=\"strut-1\" id=\"%d\" x=\"%f\" y=\"%f\" angle=\"%f\"angleV=\"0.000000\" editorAngle=\"0\" activated=\"0\" exploded=\"0\" flippedX=\"0\" flippedY=\"0\"/>\n" % (
            i, x, y, al))
    elif num == 3:
        f.write(
            "        <Part partType=\"parachute-1\" id=\"%d\" x=\"%f\" y=\"%f\" angle=\"%f\" angleV=\"0.000000\" editorAngle=\"0\" activated=\"0\" exploded=\"0\" flippedX=\"0\" flippedY=\"0\" chuteX=\"4.000000\" chuteY=\"4.250000\" chuteAngle=\"0.000000\" chuteHeight=\"0.000000\" inflation=\"0.100000\" inflate=\"0\" deployed=\"0\" rope=\"0\"/>\n" % (
            i, x, y, al))
    elif num == 4:
        f.write(
            "        <Part partType=\"nosecone-1\" id=\"%d\" x=\"%f\" y=\"%f\" angle=\"%f\" angleV=\"0.000000\" editorAngle=\"0\" activated=\"0\" exploded=\"0\" flippedX=\"0\" flippedY=\"0\"/>\n" % (
            i, x, y, al))
    elif num == 5:
        f.write(
            "        <Part partType=\"dock-1\" id=\"%d\" x=\"%f\" y=\"%f\" angle=\"%f\" angleV=\"0.000000\" editorAngle=\"0\" activated=\"0\" exploded=\"0\" flippedX=\"0\" flippedY=\"0\"/>\n" % (
            i, x, y, al))


# while 1:
print("")
print("Shape?")
print("    1 round")
print("    2 nuke")
SHP = input()
if int(SHP) == 1:
    print("Ignore Collision box?")
    print("    1 yes")
    print("    2 no")
    ICB = input()
    print("Parent part?")
    PatNum()
    PPa = input()
    print("Child part?")
    PatNum()
    CPa = input()
    print("Radius?")
    r = input()
    if int(ICB) == 1:
        print("Length of side?")
        l = input()
        RudGen(l, r)
    elif int(ICB) == 2:
        RudGen(LenCho(int(CPa)), r)
    else:
        print("ERROR")
elif int(SHP) == 2:
    print("Number?")
    n = input()
    NukGen(int(n))
else:
    print("ERROR no such shape")
f.close()
"""
SimpleRocketsShapeGenerator
version 2.0.1    202011141709
by Oscar
"""
