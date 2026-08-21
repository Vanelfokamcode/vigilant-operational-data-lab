
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select amount_cents
from "vigilant_ops"."main"."stg_order_events"
where amount_cents is null



  
  
      
    ) dbt_internal_test