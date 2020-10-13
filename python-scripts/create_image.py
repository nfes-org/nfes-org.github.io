import matplotlib.pyplot as plt

fig = plt.figure()
fig.patch.set_facecolor('xkcd:mint green')
plt.axis([0, 10, 0, 10])
plt.axis('off')

t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
# plt.text(4, 1, t, ha='left', rotation=15, wrap=True)
# plt.text(6, 5, t, ha='left', rotation=15, wrap=True)
# plt.text(5, 5, t, ha='right', rotation=-15, wrap=True)
plt.text(5, 10, t, fontsize=25, style='normal',
         # weight='light',
         ha='center',
         va='top', wrap=True, linespacing=2,
         # backgroundcolor='purple',
         color='purple')
# plt.text(3, 4, t, family='serif', style='italic', ha='right', wrap=True)
# plt.text(-1, 0, t, ha='left', rotation=-15, wrap=True)
ax = plt.gca()
ax.set_facecolor('xkcd:salmon')
ax.set_facecolor((1.0, 0.47, 0.42))

plt.show()
