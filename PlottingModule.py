import matplotlib.pyplot as plt
import ListModule as lst
# here x is indices
# plt.plot([0, 55, 88, 99])
# plt.show()
#
# plt.plot([0, 55, 88, 99], "oy")
# plt.show()
#
# plt.plot([0, 55, 88, 99], ":b")
# plt.show()

xx = lst.listRange
yy = lst.simpleList

# error code
# plt.plot(xx, yy, ":c")
# plt.set(xlabel="X label", ylabel="Y labels", title="this is rough")
# plt.show()

fig, ax = plt.subplots()

ax.plot(xx, yy, "-c",
        xx, yy, "ok")
ax.set(xlabel="X label", ylabel="Y labels", title="this is rough")
plt.show()