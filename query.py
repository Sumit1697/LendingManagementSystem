class Queries:
    GET_CIF_INFORMATION = "select * from cifapplication_cifuserdetail where "
    GET_PRODUCT_CONFIG = "select * from cifapplication_productconfig where product_id = %s and version = %s"
    INSERT_CIF_DATA = "Insert into cifapplication_cifuserdetail (cif_id,external_id,email_id,mobile_number,pan_number,date_of_birth,profile_type,user_address)" \
                      " values (%s,%s,%s,%s,%s,%s,%s,%s)"