"""
Author: pengmy
Date: 2025-12-01
Function: show pointcloud
"""
import os
import warnings
import open3d as o3d
import copy

# 忽略警告信息
warnings.filterwarnings("ignore")

# 设置 XDG_RUNTIME_DIR 环境变量
if 'XDG_RUNTIME_DIR' not in os.environ:
    os.environ['XDG_RUNTIME_DIR'] = f'/tmp/runtime-{os.getuid()}'
    os.makedirs(os.environ['XDG_RUNTIME_DIR'], mode=0o700, exist_ok=True)


def show_pcd_2(source, target, ro1=None, ro2=None,name="pcd"): 
    """
    Display two point clouds in the same visualization window with optional transformations.
    
    Args:
        source: The source point cloud to display (will be colored red)
        target: The target point cloud to display (will be colored blue)
        ro1: Transformation matrix to apply to the source point cloud (optional)
        ro2: Transformation matrix to apply to the target point cloud (optional)
        name: Name of the visualization window (default: "pcd")
    """
    source_points = copy.deepcopy(source)
    target_points = copy.deepcopy(target)
    source_points.paint_uniform_color([1, 0, 0])  # Red color for source
    target_points.paint_uniform_color([0, 0, 1])  # Blue color for target
    if ro1 is not None: 
        source_points.transform(ro1)
        target_points.transform(ro2)
    coor = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1, origin=[0,0,0])
    o3d.visualization.draw_geometries([source_points,target_points, coor],window_name=name)
 
def show_pcd_1(source, name="pcd"): 
    """
    Display a single point cloud in a visualization window.
    
    Args:
        source: The point cloud to display (will be colored red)
        name: Name of the visualization window (default: "pcd")
    """
    source_points = copy.deepcopy(source) 
    source_points.paint_uniform_color([1, 0, 0])  # Red color for source 
    coor = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1, origin=[0,0,0])
    o3d.visualization.draw_geometries([source_points, coor],window_name=name)