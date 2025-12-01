"""
Author: pengmy
Date: 2025-12-01
Function: pointcloud processing and registration 
"""
import numpy as np
import open3d as o3d
import copy


def pca_compute_shape(point_cloud):
    """
    Compute principal components and center of a point cloud using PCA.
    
    Args:
        point_cloud: Open3D point cloud
        
    Returns:
        U: 3x3 matrix with principal axes (eigenvectors of covariance matrix)
        shape_center: Center point of the point cloud bounding box
    """
    # Extract points from point cloud
    points = np.asarray(point_cloud.points) 
    
    # Calculate centroid of the point cloud
    centroid = np.mean(points, axis=0)  
    
    # Center the points around the centroid
    centered_points = points - centroid
    
    # Compute covariance matrix of the centered points
    covariance_matrix = np.cov(centered_points.T)
    
    # SVD - decompose covariance matrix to get principal axes
    U, _, _ = np.linalg.svd(covariance_matrix)
    
    # Calculate shape center as midpoint of bounding box
    min_pt = np.min(points, axis=0)
    max_pt = np.max(points, axis=0)
    shape_center = 0.5 * (min_pt + max_pt)
    
    return U, shape_center
def pca_registration_fix(source, target):
    """
    Perform initial alignment of two point clouds using PCA-based registration.
    
    This function aligns two point clouds by computing their principal components
    and creating a transformation that aligns the source point cloud's principal
    axes with the target's principal axes.
    
    Args:
        source: Open3D point cloud to be aligned (will be transformed)
        target: Open3D point cloud used as reference (fixed)
        
    Returns:
        registered: Transformed source point cloud
        T: 4x4 transformation matrix used for alignment
    """  
    # Check if input point clouds are valid
    if len(source.points) == 0 or len(target.points) == 0:
        print("Input point cloud is empty!")
        return None, np.eye(4)
    
    # Compute principal components and centers for both point clouds
    # Up: principal axes of source point cloud
    # Cp: center of source point cloud
    # Ux: principal axes of target point cloud
    # Cx: center of target point cloud
    Up, Cp = pca_compute_shape(source)
    Ux, Cx = pca_compute_shape(target)
    
    # Ensure consistent orientation by checking dot products
    # If dot product is negative, flip the eigenvector
    # This ensures both point clouds have the same orientation
    for i in range(3):
        if np.dot(Up[:, i], Ux[:, i]) < 0:
            Ux[:, i] = -Ux[:, i]
    
    # Compute rotation matrix (align source to target principal axes)
    # R0 = Ux * Up^T where Up and Ux are orthogonal matrices
    # This rotation aligns the principal axes of source with target
    R0 = Ux @ Up.T
    
    # Compute translation vector (align source center to target center)
    # T0 = Cx - R0 * Cp moves the source center to the target center
    T0 = Cx - R0 @ Cp
    
    # Construct 4x4 transformation matrix
    # The transformation combines rotation and translation
    T = np.eye(4)
    T[:3, :3] = R0
    T[:3, 3] = T0
    
    # Apply transformation to source point cloud
    registered = copy.deepcopy(source)
    registered.transform(T)
    
    return registered, T