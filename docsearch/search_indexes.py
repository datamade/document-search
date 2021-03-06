from haystack import indexes, fields

from docsearch import models


class IntegerMultiValueField(fields.MultiValueField):
    field_type = 'integer'


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    township_arr = IntegerMultiValueField(null=True, faceted=True)
    range_arr = IntegerMultiValueField(null=True, faceted=True)
    section_arr = IntegerMultiValueField(null=True, faceted=True)

    def get_model(self):
        return models.Book

    def _convert_range_to_array(self, obj, fieldname):
        range_ = getattr(obj, fieldname)
        if range_:
            return list(range(range_.lower, range_.upper))
        else:
            return range_

    def prepare_township_arr(self, obj):
        return self._convert_range_to_array(obj, 'township')

    def prepare_range_arr(self, obj):
        return self._convert_range_to_array(obj, 'range')

    def prepare_section_arr(self, obj):
        return self._convert_range_to_array(obj, 'section')


class ControlMonumentMapIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    township = indexes.CharField(model_attr='township', null=True, faceted=True)
    range = indexes.CharField(model_attr='range', null=True, faceted=True)
    section_arr = IntegerMultiValueField(model_attr='section', null=True, faceted=True)
    part_of_section = indexes.CharField(model_attr='part_of_section', null=True, faceted=True)

    def get_model(self):
        return models.ControlMonumentMap


class SurplusParcelIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    surplus_parcel = indexes.CharField(model_attr='surplus_parcel', null=True, faceted=True)
    description = indexes.CharField(model_attr='description', null=True)

    def get_model(self):
        return models.SurplusParcel


class DeepTunnelIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    description = indexes.CharField(model_attr='description', faceted=True)

    def get_model(self):
        return models.DeepTunnel


class DossierIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    file_number = indexes.CharField(model_attr='file_number', faceted=True)
    document_number = indexes.CharField(model_attr='document_number', faceted=True)

    def get_model(self):
        return models.Dossier


class EasementIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    easement_number = indexes.CharField(model_attr='easement_number', null=True, faceted=True)
    description = indexes.CharField(model_attr='description', null=True, faceted=True)

    def get_model(self):
        return models.Easement


class FlatDrawingIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    area = indexes.IntegerField(model_attr='area', null=True, faceted=True)
    section = indexes.IntegerField(model_attr='section', null=True, faceted=True)
    map_number = indexes.CharField(model_attr='map_number', null=True, faceted=True)
    location = indexes.CharField(model_attr='location', null=True, faceted=True)
    building_id = indexes.IntegerField(model_attr='building_id', null=True, faceted=True)
    description = indexes.CharField(model_attr='description', null=True, faceted=True)
    job_number = indexes.CharField(model_attr='job_number', null=True, faceted=True)
    number_of_sheets = indexes.CharField(model_attr='number_of_sheets', null=True, faceted=True)
    date = indexes.CharField(model_attr='date', null=True, faceted=True)
    cross_ref_area = indexes.IntegerField(model_attr='cross_ref_area', null=True, faceted=True)
    cross_ref_section = indexes.IntegerField(model_attr='cross_ref_section', null=True, faceted=True)
    cross_ref_map_number = indexes.CharField(model_attr='cross_ref_map_number', null=True, faceted=True)

    def get_model(self):
        return models.FlatDrawing


class IndexCardIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    monument_number = indexes.CharField(model_attr='monument_number', null=True, faceted=True)
    township = indexes.CharField(model_attr='township', faceted=True)
    section = indexes.CharField(model_attr='section', null=True, faceted=True)
    corner = indexes.CharField(model_attr='corner', null=True, faceted=True)

    def get_model(self):
        return models.IndexCard


class LicenseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    license_number = indexes.CharField(model_attr='license_number', null=True, faceted=True)
    description = indexes.CharField(model_attr='description', null=True, faceted=True)
    geometry = indexes.CharField(use_template=True, indexed=False)
    township_arr = IntegerMultiValueField(model_attr='township', null=True, faceted=True)
    range_arr = IntegerMultiValueField(model_attr='range', null=True, faceted=True)
    section_arr = IntegerMultiValueField(model_attr='section', null=True, faceted=True)
    township_arr = IntegerMultiValueField(model_attr='township', null=True, faceted=True)
    type = indexes.CharField(model_attr='type', null=True, faceted=True)
    entity = indexes.CharField(model_attr='entity', null=True, faceted=True)
    diameter = indexes.CharField(model_attr='diameter', null=True, faceted=True)
    material = indexes.CharField(model_attr='material', null=True, faceted=True)
    end_date = indexes.CharField(model_attr='end_date', null=True, faceted=True)
    status = indexes.CharField(model_attr='status', null=True, faceted=True)
    agreement_type = indexes.CharField(model_attr='agreement_type', null=True, faceted=True)

    def get_model(self):
        return models.License


class ProjectFileIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    area = indexes.IntegerField(model_attr='area', null=True, faceted=True)
    section = indexes.IntegerField(model_attr='section', null=True, faceted=True)
    job_number = indexes.CharField(model_attr='job_number', null=True, faceted=True)
    job_name = indexes.CharField(model_attr='job_name', null=True, faceted=True)
    description = indexes.CharField(model_attr='description', null=True, faceted=True)
    cabinet_number = indexes.CharField(model_attr='cabinet_number', null=True, faceted=True)
    drawer_number = indexes.CharField(model_attr='drawer_number', null=True, faceted=True)

    def get_model(self):
        return models.ProjectFile


class RightOfWayIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    folder_tab = indexes.CharField(model_attr='folder_tab', faceted=True)

    def get_model(self):
        return models.RightOfWay


class SurveyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    township_arr = IntegerMultiValueField(model_attr='township', null=True, faceted=True)
    range_arr = IntegerMultiValueField(model_attr='range', null=True, faceted=True)
    section_arr = IntegerMultiValueField(model_attr='section', null=True, faceted=True)
    map_number = indexes.CharField(model_attr='map_number', null=True, faceted=True)
    location = indexes.CharField(model_attr='location', null=True, faceted=True)
    description = indexes.CharField(model_attr='description', null=True, faceted=True)
    job_number = indexes.CharField(model_attr='job_number', null=True, faceted=True)
    number_of_sheets = indexes.CharField(model_attr='number_of_sheets', null=True, faceted=True)
    date = indexes.CharField(model_attr='date', null=True, faceted=True)

    def get_model(self):
        return models.Survey


class TitleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    control_number = indexes.CharField(model_attr='control_number', faceted=True)

    def get_model(self):
        return models.Title
