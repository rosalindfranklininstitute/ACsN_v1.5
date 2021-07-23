ACsN v1.5.1 - Python
=====
<div> 
	<table frame=void rules=none>
		<tr>
			<td width="75%">
				<div style="width:650px;float:left" align="justify">
					ACsN (pronounced as <i>action</i>) stands for Automatic Correction of sCMOS-related Noise. It combines an accurate estimation of noise variation with sparse filtering to eliminate the most relevant noise sources in the images of a sCMOS sensor. This results in a drastic reduction of pixel-dependent noise in sCMOS images and an enhanced stability of denoising performance at a competitive computational speed.
				</div>
			</td>
			<td width="25%">
				<div style="width:150px;float:right;">
					<img src="Picture2.jpg" width=150 height=150>
				</div>
			</td>
		</tr>
	</table>	
	<!-- <div style="clear:both"></div>  -->
</div>

## Citation ##
Please, cite our paper on [Nature Communications].

Mandracchia, B., Hua, X., Guo, C. et al. Fast and accurate sCMOS noise correction for fluorescence microscopy. Nat Commun 11, 94 (2020) doi:10.1038/s41467-019-13841-8

## System Requirements ##
### Hardware Requirements ###
ACsN requires a standard computer with enough RAM to support Python >= 3.7. For minimum performance, this will be a computer with about 2 GB of RAM. For optimal performance, we recomend the following specs:

RAM: 16+ GB; 
CPU: 6+ cores, 3.2+ GHz/core.

### Software Requirements ###
Python 3.7+
Windows OS 7+
Partial functionality on Mac OS

## Install ##
### Command Line ###

The instructions here only work when using a conda environment.

With Anaconda or miniconda or miniforge create a new environment (or use exisiting one), with python version >=3.7

For example:

(Optional, depending in system being used)
If using module system, do
`$module load miniconda`

Create new environment
`$conda create --name ACSN python=3.7`

Activate it
`$conda activate ACSN`


With command-line setup and activated to conda environment, install the following. These are needed.

`$conda install openblas`

`$conda install cupy`


Clone this repository and extract/unzip files.

Navigate first to Sparse_Filtering/
`$cd Sparse_Filtering`

And then install it
`$python3 setup.py install`

Then navigate to ACsN_code/
`$cd ../ACsN_code`

And then install it
`$python3 setup.py install`

And it should be ready to run

You can test by running the example in tests folder
`$cd ..`
`$python3 tests/ACSN_Run.py`


And... if you  want to do somthing more, it is perhaps best to reuse ACSN_Run.py file,
copy, rename. Open in a text editor or IDE, change the reference to your own files and
provide output location. Good luck.


## Creators ##
Suraj Rajendran (Python Version) and Biagio Mandracchia
Modified by Luis Perdigao for Python only version
