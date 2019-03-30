Dataviz in R
==============
css: slides.css
transition: fade
transition-speed: fast
Scripting, post-processing & interactive web

Brown bag lunch, June 18, 2015

<a href="http://markuskainu.fi">Markus Kainu</a></br> 
ESS, Team F 


<div class="github-fork-ribbon-wrapper right">
<div class="github-fork-ribbon">
<a href="https://github.com/UNFAOstatistics/" style="color:white;">Fork me on GitHub</a>
</div>
</div>

<div class="banner-wrapper">
<img src="img/fao-logo.png"> 
</div>


<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>





<!-- ---| notes begin |--------------------------------

---------| notes end |-----------------------------  --> 

Case Statistical Yearbook
===================================

![](img/sybprocess.png)



 
Content
===================================

- Basics of graphics - bitmap vs. vector
- Why to use R for graphics - scripting vs. point & click
- Static graphics in R
- Post-processing R graphs
- The WEB: interactive graphics and web applications


Vector graphics vs. bitmap graphics
===========================================

|                  |               bitmap              |                       vector                       |
|------------------|-----------------------------------|----------------------------------------------------|
| file extensions  | .jpg, .png, .gif                  | .eps, .pdf, .svg, .ai                              |
| common example   | digital photo                     | google maps                                        |
| consists of      | million of pixels                 | points, lines and polygons                         |
| file size        | large                             | small                                              |
| software         | [Gimp](www.gimp.org/) (Photoshop) | [Inkscape](https://inkscape.org/en/) (Illustrator) |
| good for         | web, printing (in high-res)       | print, post-processing                             |
| exclusively used | digital photography               | maps and graphs                                    |
 
 **You can make vector graphics into bitmap graphics, but not the other way around**
 
 
===================================

![](http://i.imgur.com/Q8kV8.png)
 


===================================
type: subsection

# Case 1: Static graphics for print & web

 
 
Population data from FAOSTAT
===================================


```r
library(FAOSTAT)
library(knitr)
library(dplyr)
library(ggplot2)
dat <- getFAOtoSYB(domainCode = "OA", elementCode = 551,itemCode = 3010) # Download rural population
dat1 <- dat$entity
dat <- getFAOtoSYB(domainCode = "OA", elementCode = 561,itemCode = 3010) # Download urban population
dat2 <- dat$entity
dat <- merge(dat1,dat2,by=c("FAOST_CODE","Year"))
```


```r
dim(dat)
```

```
[1] 19854     4
```

```r
kable(head(dat)) # print 5 first rows
```



| FAOST_CODE| Year| OA_3010_551| OA_3010_561|
|----------:|----:|-----------:|-----------:|
|        100| 1961|      375928|       82699|
|        100| 1962|      382709|       85253|
|        100| 1963|      389708|       87908|
|        100| 1964|      396938|       90670|
|        100| 1965|      404412|       93541|
|        100| 1966|      412128|       96528|


Population data from FAOSTAT
===================================


```r
names(dat) <- c("FAOST_CODE","Year","rural_pop","urban_pop")
dat$total_pop <- dat$rural_pop + dat$urban_pop # Compute total population
dat$rural_share <- round(dat$rural_pop / dat$total_pop * 100,1) # Compute rural population share of total population
library(countrycode) # Add the country name & continent using countrycode-package
dat$FAOST_CODE[dat$FAOST_CODE == 41] <- 351
dat$cntry <- countrycode(dat$FAOST_CODE, origin = "fao", destination = "country.name")
dat$cont <- countrycode(dat$FAOST_CODE, origin = "fao", destination = "continent")
dat <- na.omit(dat)
```


```r
dim(dat)
```

```
[1] 16475     8
```

```r
kable(head(dat)) # print 5 first rows
```



| FAOST_CODE| Year| rural_pop| urban_pop| total_pop| rural_share|cntry |cont |
|----------:|----:|---------:|---------:|---------:|-----------:|:-----|:----|
|        100| 1961|    375928|     82699|    458627|        82.0|India |Asia |
|        100| 1962|    382709|     85253|    467962|        81.8|India |Asia |
|        100| 1963|    389708|     87908|    477616|        81.6|India |Asia |
|        100| 1964|    396938|     90670|    487608|        81.4|India |Asia |
|        100| 1965|    404412|     93541|    497953|        81.2|India |Asia |
|        100| 1966|    412128|     96528|    508656|        81.0|India |Asia |



======================================================= 


```r
library(ggplot2)
library(dplyr)
p <- ggplot(data=dat, 
            aes(x=rural_pop,y=urban_pop))
p + geom_point()
```

![plot of chunk unnamed-chunk-5](dataviz-in-R-figure/unnamed-chunk-5-1.png) 



```r
pie_data <- dat %>% filter(Year == 2015) %>% 
  group_by(cont) %>% summarise(share = sum(rural_pop))
pie_data <- pie_data %>% mutate(sum = sum(share)) 
p <- ggplot(pie_data, aes(x=sum/2, y = share, fill =cont, width = sum))
p <- p + geom_bar(position="fill", stat="identity") 
p + coord_polar("y")
```

![plot of chunk unnamed-chunk-6](dataviz-in-R-figure/unnamed-chunk-6-1.png) 

***


```r
plot_data <- dat[dat$Year == 2015,]
p <- ggplot(data=plot_data, 
            aes(x=cntry,y=rural_share))
p + geom_bar(stat="identity")
```

![plot of chunk unnamed-chunk-7](dataviz-in-R-figure/unnamed-chunk-7-1.png) 



```r
p <- ggplot(data=dat, 
            aes(x=Year,y=rural_share,group=cntry))
p + geom_point() + geom_line()
```

![plot of chunk unnamed-chunk-8](dataviz-in-R-figure/unnamed-chunk-8-1.png) 

Share of rural population
=====================================================


```r
plot_data <- dat %>% filter(Year == 2015)
p <- ggplot(data=plot_data, 
            aes(x=cntry,y=rural_share))
p + geom_bar(stat="identity")
```

![plot of chunk unnamed-chunk-9](dataviz-in-R-figure/unnamed-chunk-9-1.png) 


Share of rural population
=====================================================


```r
plot_data$cntry <- factor(plot_data$cntry, levels=arrange(plot_data, -rural_share)$cntry)
p <- ggplot(data=plot_data, 
            aes(x=cntry,y=rural_share))
p + geom_bar(stat="identity")
```

![plot of chunk unnamed-chunk-10](dataviz-in-R-figure/unnamed-chunk-10-1.png) 


Share of rural population
=====================================================


```r
plot_data <- arrange(plot_data, -rural_share)[1:20,] # top 20
p <- ggplot(data=plot_data, aes(x=cntry,y=rural_share,fill=cont))
p + geom_bar(stat="identity")
```

![plot of chunk unnamed-chunk-11](dataviz-in-R-figure/unnamed-chunk-11-1.png) 

Share of rural population
=====================================================


```r
p <- ggplot(data=plot_data, aes(x=cntry,y=rural_share,fill=cont))
p <- p + geom_bar(stat="identity")
p + coord_flip()
```

![plot of chunk unnamed-chunk-12](dataviz-in-R-figure/unnamed-chunk-12-1.png) 



=====================================================


```r
p <- ggplot(data=plot_data, aes(x=cntry,y=rural_share,fill=cont))
p <- p + geom_bar(stat="identity")
p <- p + coord_flip()
p <- p + scale_fill_manual(values=c("#1b9e77","#d95f02","#7570b3","#e7298a","#66a61e"))
p <- p + theme_minimal()
p <- p + theme(text = element_text(family = "Open Sans"),
               title = element_text(size = 20),
               axis.title = element_text(size=14),
               legend.position = "top")
p <- p + labs(title="Share of rural population", x=NULL,y="Share of rural population (%)")
p <- p + guides(fill = guide_legend(title = "Continent", title.position = "left", title.hjust=.5))
p
```

![plot of chunk unnamed-chunk-13](dataviz-in-R-figure/unnamed-chunk-13-1.png) 




=====================================================



```r
library(gisfao)
library(scales)
shape <- fao_world
FAOST_CODE <- as.character(shape$FAOST_CODE)
df.d <- data.frame(FAOST_CODE, rep(NA, nrow(shape)))
dat$FAOST_CODE[dat$FAOST_CODE == 351] <- 41
mapdata <- merge(dat %>% filter(Year == 2015), df.d, by.x = "FAOST_CODE", all.y = TRUE)
row.names(mapdata) <- mapdata$FAOST_CODE
row.names(shape) <- as.character(shape$FAO_CODE)
mapdata <- mapdata[order(row.names(mapdata)), ]
shape <- shape[order(row.names(shape)), ]
shape2 <- maptools::spCbind(shape, mapdata)
shape2$id <- rownames(shape2@data)
map.points <- fortify(shape2, region = "id")
map.df <- merge(map.points, shape2, by = "id")

map <- ggplot(data=map.df, aes(long,lat,group=group))
map <- map  + geom_polygon(aes(fill = rural_share),colour=alpha("white", 3/4),size=.2)
map <- map + theme(legend.position = c(0.15,0.45), 
                          legend.background=element_rect(colour=NA, fill=NA),
                          axis.text = element_blank(), axis.title = element_blank(), axis.ticks = element_blank())
map
```

![plot of chunk unnamed-chunk-14](dataviz-in-R-figure/unnamed-chunk-14-1.png) 


Exporting for post-processing
===================================================


```r
# barplot
ggsave(p, file="output/barplot.svg", width=14, height=8)
ggsave(p, file="output/barplot.pdf", width=14, height=8)
ggsave(p, file="output/barplot.png")

ggsave(map, file="output/map.svg", width=14, height=8)
ggsave(map, file="output/map.pdf", width=14, height=8)
ggsave(map, file="output/map.png")
```

## -> post-processing in Inkscape & Gimp


===================================
type: subsection

# Case 2: interactive graphics & applications for the web


Interactive graphics
==================================


|                 |            interactive graphics            |    interactive web applications    |
| --------------- | ------------------------------------------ | ---------------------------------- |
| typical example | javascript plot                            | Trade data explorer                |
| look and feel   | amazing but limited                        | amazing and unlimited              |
| depends         | online libraries, shipped with data        | Needs a full R instance            |
| R               | [htmlwidgets](http://www.htmlwidgets.org/) | [shiny](http://shiny.rstudio.com/) |
| good for        | showing off &                              | showing off & explorative wiz      |
|                 |                                            |                                    |



Interactive maps
=========================================


```r
library(gisfao)
library(dplyr)
library(sp)
library(leaflet)


shape <- fao_world
FAOST_CODE <- as.character(shape$FAOST_CODE)
VarX <- rep(NA, nrow(shape))
df.d <- data.frame(FAOST_CODE, VarX)
dat2 <- merge(dat, df.d, by.x = "FAOST_CODE", all.y = TRUE)
row.names(dat2) <- dat2$FAOST_CODE
row.names(shape) <- as.character(shape$FAO_CODE)
dat2 <- dat2[order(row.names(dat2)), ]
shape <- shape[order(row.names(shape)), ]
shape2 <- maptools::spCbind(shape, dat2)

# Define the region and color variables and title:
main <- "Rural population"
color = "rural_share"

# Define color palette
palette <- leaflet::colorNumeric(c("#fef0d9","#fdcc8a","#fc8d59","#e34a33","#b30000"), 
                                 domain = shape2$rural_share)

# Define the text for popup box
state_popup <- paste0("<strong>Country: </strong>", shape2$ADM0_NAME, 
                      "<br><strong>", main, ": </strong>", 
                      round(shape2@data[,c(color)], digits=2))

# Generate interactive visualization
leaflet(data = shape2) %>% 
  addTiles() %>% 
  setView(lng = 12.30, lat = 41.54, zoom = 3) %>% 
  addPolygons(fillColor = ~palette(get(color)), 
              fillOpacity = 0.7, 
              color = "#000000", 
              weight = 1,
              popup = state_popup) %>% 
  addLegend("bottomright", pal = palette, values = ~rural_share,
    title = "Share of rural population",
    labFormat = labelFormat(prefix = "%")
  )
```



Interactive maps
=========================================


<iframe src="http://unfaostatistics.github.io/brown-bag-dataviz/leaflet/try1.html" style="border: none; width: 1100px; height: 900px"></iframe> 


Interactive time-series
=========================================







R for dataviz
===================================================

## Pros

- R has good graphics
- Scripting makes your ideas/graphs re-usable
- organising your code is important
- growing expertise in ESS/FAO 

***

## Cons

- scripting is slow the first time

