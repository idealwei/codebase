import numpy as np
import torch
import os
import termcolor
import visdom

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

# color ouput
def printRed(content): return termcolor.colored(content, "red", attrs=["bold"])
def printGreen(content): return termcolor.colored(content,"green",attrs=["bold"])
def printBlue(content): return termcolor.colored(content,"blue",attrs=["bold"])
def printCyan(content): return termcolor.colored(content,"cyan",attrs=["bold"])
def printYellow(content): return termcolor.colored(content,"yellow",attrs=["bold"])
def printMagenta(content): return termcolor.colored(content,"magenta",attrs=["bold"])


class Visdom():
    def __init__(self, opt):
        self.vis = visdom.Visdom(port=9999)
        self.trainLossInit = True

    def trainLoss(self, opt, iter_num, loss):
        loss = float(loss.cpu().numpy())
        if self.trainLossInit:
            self.vis.line(Y=np.array([loss]), X=np.array([iter_num], win="{0}_trainloss".format("model_name")),
            opts={"title": "{0} (TRAIN_loss)".format("model_name")})
            self.trainLossInit = False
        else:
            self.vis.line(Y=np.array([loss]), X=np.array([iter_num], win="{0}_trainloss".format("model_name")),
            update="append")
