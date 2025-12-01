"""
Author: pengmy
Date: 2025-12-01
Function: Load or Save data from file 
"""
import numpy as np
import open3d as o3d

def load_pcd(file_path, scale=None):
    """
    Load a point cloud from a file and optionally scale it. 

    Args:
        file_path (str): Path to the point cloud file
        scale (float, optional): Scaling factor to apply to the point cloud. Defaults to None.
        
    Returns:
        open3d.geometry.PointCloud: The loaded (and potentially scaled) point cloud
    """
    raw_pcd = o3d.io.read_point_cloud(file_path)
    if scale:
        raw_pcd.scale(scale, center=(0, 0, 0)) 
    return raw_pcd