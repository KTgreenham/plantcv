# PlantCV

##Table of Contents:
1.  [Introduction to PlantCV](#introduction)
1.  [Issues with PlantCV](#issueswithplantcv)  
2.  [PlantCV Contributor's Guide](#plantcvcontributorsguide)  
  *  [New Code to PlantCV](#newcode)  
  *  [Maintain PlantCV](#maintainplantcv)  
  *  [New Function Requests](#newfunctionrequesnts)  
  *  [Contribution Style Guide](#styleguide)

---
##<a id="introduction"></a>Introduction to PlantCV

PlantCV is an imaging processing and trait extraction package and specific for plants
that is built upon open-source software platforms <a href="http://opencv.org/">OpenCV</a> <sup>1</sup>,
<a href="http://www.numpy.org/">NumPy</a> <sup>2</sup>, and <a href="http://matplotlib.org/">MatPlotLib</a> <sup>3</sup>.

<p>If you use PlantCV please cite: paper here</p>

*  Installation instructions can be found [here](http://plantcv.danforthcenter.org/pages/documentation/function_docs/installation.html)

*  Further documentation for PlantCV functions and use can be found at the [PlantCV Website](http://plantcv.danforthcenter.org/pages/documentation/)

*  Test image sets can be found via [Figshare](http://figshare.com/account/projects/3081)

*  We recommend reading DOI X, which is the first manuscript to detail PlantCV and provide examples of functionality.

<p>Citations:<br>
  1. Bradski G (2000) The opencv library. Doctor Dobbs Journal 25(11):120-126.<br>
  2. Oliphant TE (2007) Python for Scientific Computing. Computing in Science & Engineering, 9, 10-20.<br>
  3. Hunter JD (2007) Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9, 90-95.</p>

___

## <a id="issueswithplantcv"></a>Issues with PlantCV?

  * Please add any PlantCV suggestions/issues/bugs [here](https://github.com/danforthcenter/plantcv/issues). Please check to see if the issue is already open.  

---

## <a id="plantcvcontributorsguide"></a>PlantCV Contributor's Guide

___

This document aims to give an overview of how to contribute to PlantCV.

Contribute in three ways:  
  1.  Add new code  
  2.  Maintain and improve existing code: fix bugs, improving quality or speed of functions, add more detailed documentation  
  3.  [Open](https://github.com/danforthcenter/plantcv/issues) issues and add suggestions to improve PlantCV  

PlantCV is licensed under a GPL 2.0 share-alike license to promote open-development of plant image processing functions, please see license for more information.

___
###<a id="newcode"></a> New Code to PlantCV

In general, new contributions to PlantCV should benefit multiple users and extend the image processing or trait analysis power of PlantCV.  

What should/should not be added to PlantCV:
  *  New validated image processing functions are highly encouraged for contribution.  
  *  New validated trait extraction algorithms are highly encouraged for contribution.  
  *  Image processing pipeline scripts that are specific for your images should **not** be added to PlantCV, unless they solve an image processing problem that you believe applies to more than one platform/user.

Steps to adding new code are below.  

####  Step 1. Open a new "New Function Proposal" forum or address an exisiting "New Function Request".

  *  If you are interested in adding a completely new function to PlantCV please first add an issue to PlantCV [here](https://github.com/danforthcenter/plantcv/issues) with the label "New Function Proposal". This allow others to comment on the proposed function and lets you gauge if the function will have multiple users.
  *  If someone has requested a new function in the issues forum and you would like to address it, please post a comment on the issue to let others know that you would like to work on it.

#### Step 2. Test, validate, and document new function

  1.  
  2.  
  3.  

#### 3. Add working function to [PlantCV-dev](https://github.com/danforthcenter/plantcv/tree/master/lib/plantcv/dev).  

  *  Add working functions to PlantCV-dev. This allows new code to be tested by multiple users without breaking working PlantCV functions.

#### 4. Move to PlantCV

  *  Functions that move to PlantCV from PlantCV-dev meet the following critera:
    *  

___
### <a id="maintainplantcv"></a> Maintain PlantCV

___
### <a id="newfunctionrequests"></a> New Function Requests

___
###<a id="styleguide"></a> Contribution Style Guide

