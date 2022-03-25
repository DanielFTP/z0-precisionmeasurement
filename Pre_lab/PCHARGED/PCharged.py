import numpy as np
import scipy.optimize
import scipy.stats
import matplotlib.pyplot as plt
from ROOT import *

canvas = TCanvas()
histo = TH1F("", "P Histogram", 30, 0, 120)  # elctron
histo2 = TH1F("", "P Histogram", 30, 0, 120) # muon
histo3 = TH1F("", "P Histogram", 30, 0, 120) # tau
histo4 = TH1F("", "P Histogram", 30, 0, 120) # hadron

histo.GetXaxis().SetTitle("Total momentum charged tracks")
histo.SetLineColor(2)
histo2.SetLineColor(3)
histo3.SetLineColor(4)
histo4.SetLineColor(5)

with open("P_electron.txt", "r") as peaks_file:
    for line in peaks_file:
        if len(line.strip()) == 0:
            continue
        x_i = float(line)
        histo.Fill(x_i)

with open("P_muon.txt", "r") as peaks_file2:
    for line in peaks_file2:
        if len(line.strip()) == 0:
            continue
        x_i2 = float(line)
        histo2.Fill(x_i2)

with open("P_tau.txt", "r") as peaks_file3:
    for line in peaks_file3:
        if len(line.strip()) == 0:
            continue
        x_i3 = float(line)
        histo3.Fill(x_i3)

with open("P_hadron.txt", "r") as peaks_file4:
    for line in peaks_file4:
        if len(line.strip()) == 0:
            continue
        x_i4 = float(line)
        histo4.Fill(x_i4)

histo.Draw()
histo2.Draw("same")
histo3.Draw("same")
histo4.Draw("same")

legend = TLegend(0.16, 0.63, 0.35, 0.81)
legend.AddEntry(histo, "electron", "l")
legend.AddEntry(histo2, "muon", "l")
legend.AddEntry(histo3, "tau", "l")
legend.AddEntry(histo4, "hadron", "l")
#legend.SetTextSize(0.065)
legend.Draw()

canvas.SaveAs("PCharged.pdf")

