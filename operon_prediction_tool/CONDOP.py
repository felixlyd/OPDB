import os

from align_tool.rockhopper_align import rockhopper_align
from align_tool.segemehl import segemehl_align
from format_handle.extract_col import extract
from format_handle.samtool_handle import samtools


def CONDOP_operon_predict(srr_n, x, _dir, process_n, align="segemehl"):
    # align
    if align == "segemehl":
        segemehl_align(srr_n, x, _dir, process_n)
    else:
        rockhopper_align(srr_n, x, _dir, process_n)
    # samtools:conut coverage depth
    samtools(srr_n, _dir)
    extract(_dir[2] + "/" + srr_n + "_count", _dir[2] + "/" + srr_n + "_table")
    os.system("rm " + _dir[2] + "/" + srr_n + "_count")
    os.system("Rscript scripts/CONDOP_script.R " + srr_n + " " + _dir[1] + " " + _dir[2])
    os.system("mv " + _dir[2] + "/COP.CONDOP.txt " + _dir[2] + "/CONDOP/" + srr_n + "_operons.txt")
    # demonstrating the result
    os.system("less " + _dir[2] + "/CONDOP/*operons.txt")