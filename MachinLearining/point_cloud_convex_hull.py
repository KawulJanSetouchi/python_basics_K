import open3d as o3d

# Convex_hull
if __name__ == "__main__":

    print("Displaying pointcloud with convex hull ...")

    mesh = o3d.io.read_triangle_mesh("C:/Users/kawuli/Desktop/new_project3D/study_Point_cloudData/DemoCropPointCloud/BunnyMesh.ply")
    mesh.compute_vertex_normals()

    pcl = mesh.sample_points_poisson_disk(number_of_points=10000)
    hull, _ = pcl.compute_convex_hull()
    hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
    hull_ls.paint_uniform_color((1, 0, 0))
    o3d.visualization.draw([pcl, hull_ls])