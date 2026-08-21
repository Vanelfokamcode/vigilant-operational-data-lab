select
    cast(event_id as uuid) as event_id,
    event_type,
    cast(event_version as integer) as event_version,
    cast(event_at as timestamptz) as event_at,
    source,
    cast(order_id as uuid) as order_id,
    cast(customer_id as uuid) as customer_id,
    cast(amount_cents as bigint) as amount_cents,
    currency,
    order_status
from {{ source('raw', 'raw_order_events') }}
