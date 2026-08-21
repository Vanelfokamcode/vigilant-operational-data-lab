
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select event_at
from "vigilant_ops"."main"."stg_order_events"
where event_at is null



  
  
      
    ) dbt_internal_test