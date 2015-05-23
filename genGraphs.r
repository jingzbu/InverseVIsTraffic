### Do some analysis on the traffic experiments

library(ggplot2)
setwd("/Users/VGupta/Documents/Research/Julia Stuff/Traffic/")
dat = read.csv(file="trafficCVal.csv")
names(dat)<- c("Lambda", "C", "deg", "Mean", "SD")
pos = position_dodge(.5)

#The absolute minimum occurs at row 36:
# 1e05, 3.7625, deg 5
ggplot(aes(x=Lambda, y=Mean, color=factor(C), group=factor(C)), 
       data=subset(dat, deg == 6 & C > 1 & C < 4.1)) +
  geom_point(position=pos) + geom_line(position=pos) +
  geom_errorbar(aes(ymin=Mean - SD, ymax=Mean+SD), position=pos) + 
  scale_x_log10()

ggplot(aes(x=C, y=Mean, color=factor(Lambda), group=factor(Lambda)), 
       data=subset(dat, Lambda >=.1 & deg==5)) +
  geom_point(position=pos) + geom_line(position=pos) +
  geom_errorbar(aes(ymin=Mean - SD, ymax=Mean+SD), position=pos)

unique(dat$C)

### Plotting the various fits for different d
library(reshape)
dat.fits = read.csv("fittedFuncs.csv")
str(dat.fits)
dat.fits.melt = melt(dat.fits, id="Flow", variable_name="Degree")

ggplot(aes(x=Flow, color=Degree, linetype=Degree, y=value), 
       data=dat.fits.melt) + 
  geom_line() + 
  theme_bw(base_size=18) + 
  xlab("Scaled Flow") + ylab("") +
  theme(legend.title=element_blank(), 
        legend.position = c(.2, .7))
  


###  Plotting the residuals from traffic
dat.resids = read.csv("resids.csv")
ggplot(aes(x=ResidsRel), data = dat.resids) + 
  geom_histogram(aes(y=..density..), fill="grey") + 
  theme_bw(base_size=18) + 
  ylab("") + 
  xlab("Relative Residuals") 


dat.flows = read.csv("FlowDiffs.csv")
ggplot(aes(x=Rel), data=dat.flows) + 
  geom_histogram(aes(y=..density..), fill="grey") + 
  theme_bw(base_size=18) + 
  ylab("") + 
  xlab("Rel. Prediction Error")


dat.fits2 = read.csv("amgSetsTraffic.csv")
str(dat.fits2)
ggplot(aes(x=Flows, y=True), data =dat.fits2) +
geom_line(size=.5, linetype="dashed") + 
  geom_point(aes(y=Fit), color="black", size=3, shape=15) +
  geom_line(aes(y=Fit), color="black", size=.5) +
  ylab("") + 
  geom_ribbon(aes(ymin=LB, ymax=UB), fill="grey", alpha=.3) +
  coord_cartesian(ylim=c(0, 4)) + 
  theme_bw(base_size=18)


