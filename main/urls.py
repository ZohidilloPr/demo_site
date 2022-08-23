from django.urls import path
from .views import (
    Ish,
    Home,
    Other,
    Resume,
    SearchAllStudents,
    Table,
    Maktab,
    Kollej,
    KollejD,
    Schools,
    DataAdd,
    OTM_Enter,
    Districts,
    MaktabAdd,
    KollejAdd,
    OTM_Finish,
    OTM_all_stu,
    load_kollej,
    load_maktab,
    load_mahalla,
    UniversitetB,
    AllDistricts,
    AllKollejBit,
    ResumeKollej,
    ResumeMaktab,
    UniversitetAdd,
    ResumeKollejTable,
    ResumeMaktabTable,
    ResumeUniversitet,
    MaktabNameAddView,
    KollejNameAddView,
    MahallaNameAddView,
    QiziqishNameAddView,
    ChetTiliNameAddView,
    ImkonyatNameAddView,
    ResumeUniversitetTable,
    UniversitetNameAddView,
    TumanVaShaharNameAddView,
    load_type_kollej,
)
urlpatterns = [

    path("ish/", Ish, name="I"),
    path("other/", Other, name="O"),

    # new 

    path("", Home, name="H"),
    path("search/", SearchAllStudents, name="SEA"),
    path("table/", Table, name="T"),
    path("maktab/", Maktab, name="M"),
    path("kollej/", Kollej, name="K"),
    path("enter/", OTM_Enter, name="E"),
    path("finish/", OTM_Finish, name="F"),
    path("tuman/<pk>/", Districts, name="D"),
    path("data/new/add/", DataAdd, name="DA"),
    path("tumanlar/all/", AllDistricts, name="AD"),
    path("tumanlar/maktablar/<pk>/", Schools, name="S"),
    path("tumanlar/kollejlar/<pk>/", KollejD, name="KD"),
# ajax section
    path("ajax/load/kollej/list", load_kollej, name="ALK"),
    path("ajax/load/maktab/list", load_maktab, name="ALMa"),
    path("ajax/load/mahalla/list", load_mahalla, name="ALM"),
    path("ajax/load/type/kollej/list", load_type_kollej, name="ALTK"),
# end ajax section
    path("bitiruvchi/maktab/new/add/", MaktabAdd, name="MBA"),
    path("tumanlar/universitet/<pk>/", UniversitetB, name="UB"),
    path("tuman/maktab/bitiruvchi/<pk>/", ResumeMaktab, name="RM"),
    path("tuman/kollej/bitiruvchi/<pk>/", ResumeKollej, name="RK"),
    path("bitiruvchi/kollej/new/add/", KollejAdd.as_view(), name="KBA"),
    path("bitiruvchi/universitet/new/add/", UniversitetAdd, name="UBA"),
    path("jadval/maktab/bitiruvchi/<pk>/", ResumeMaktabTable, name="RMT"),
    path("jadval/kollej/bitiruvchi/<pk>/", ResumeKollejTable, name="RKT"),
    path("data/new/add/maktab/", MaktabNameAddView.as_view(), name="MaNAV"),
    path("data/new/add/kollej/", KollejNameAddView.as_view(), name="KNAV"),
    path("data/new/add/mahalla/", MahallaNameAddView.as_view(), name="MNAV"),
    path("tuman/universitet/bitiruvchi/<pk>/", ResumeUniversitet, name="RU"),
    path("data/new/add/qiziqish/", QiziqishNameAddView.as_view(), name="QNAV"),
    path("data/new/add/imkonyat/", ImkonyatNameAddView.as_view(), name="INAV"),
    path("data/new/add/chettili/", ChetTiliNameAddView.as_view(), name="FNAV"),
    path("jadval/universitet/bitiruvchi/<pk>/", ResumeUniversitetTable, name="RUT"),
    path("data/new/add/universitet/", UniversitetNameAddView.as_view(), name="UNAV"),
    path("data/new/add/tumanvashahar/", TumanVaShaharNameAddView.as_view(), name="TvSNAV"),

    path("bitiruvchilar/tumanlar/kollej/<pk>/", AllKollejBit, name="AKB"),
    path("bitiruvchilar/tumanlar/otm/<pk>/", OTM_all_stu, name="AOB"),
    path("bitiruvchilar/resume/<pk>/", Resume, name="RE"),

]