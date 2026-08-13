from qgis.core import QgsProject, QgsMapLayerType, QgsWkbTypes, Qgis
from .models.data_classes import FeatureContext

def filter_polygon_features(project: QgsProject):
        result_list = []
        for layer in project.mapLayers().values():    
            if layer.type() == QgsMapLayerType.VectorLayer and layer.geometryType() == QgsWkbTypes.PolygonGeometry:
                  for feature in layer.getFeatures():
                       if feature.geometry().type() == Qgis.GeometryType.Polygon:
                            result_list.append(FeatureContext(layer=layer, feature=feature))
        return result_list