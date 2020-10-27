import matplotlib.pyplot as plt

fig = plt.figure()
fig.patch.set_facecolor('xkcd:mint green')
plt.axis([0, 10, 0, 10])
plt.axis('off')

t = "The Next Stavanger Monthly Technical Meeting will be at 11:00 on Wednesday, November 4, 2020 at the Solastranden Gård. "
     # "Title: EVALUATING PETROPHYSICAL PROPERTIES AND VOLUMETRICS UNCERTAINTIES OF SAND INJECTITE RESERVOIRS – NORWEGIAN NORTH SEA (Artur Kotwicki, Aker BP)"
# plt.text(4, 1, t, ha='left', rotation=15, wrap=True)
# plt.text(6, 5, t, ha='left', rotation=15, wrap=True)
# plt.text(5, 5, t, ha='right', rotation=-15, wrap=True)
plt.text(5, 5, t, fontsize=25, style='normal',
         weight = 'bold',
         # weight='light',
         ha='center',
         va='center', wrap=True, linespacing=1.5,
         # backgroundcolor='purple',
         color='purple')
# plt.text(3, 4, t, family='serif', style='italic', ha='right', wrap=True)
# plt.text(-1, 0, t, ha='left', rotation=-15, wrap=True)
ax = plt.gca()
ax.set_facecolor('xkcd:salmon')
ax.set_facecolor((1.0, 0.47, 0.42))

plt.savefig("next.png", dpi=600)
# plt.show()
