// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interfaces:srv/SensorData.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__SENSOR_DATA__STRUCT_H_
#define CUSTOM_INTERFACES__SRV__DETAIL__SENSOR_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'data'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/SensorData in the package custom_interfaces.
typedef struct custom_interfaces__srv__SensorData_Request
{
  rosidl_runtime_c__double__Sequence data;
} custom_interfaces__srv__SensorData_Request;

// Struct for a sequence of custom_interfaces__srv__SensorData_Request.
typedef struct custom_interfaces__srv__SensorData_Request__Sequence
{
  custom_interfaces__srv__SensorData_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__SensorData_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SensorData in the package custom_interfaces.
typedef struct custom_interfaces__srv__SensorData_Response
{
  bool success;
} custom_interfaces__srv__SensorData_Response;

// Struct for a sequence of custom_interfaces__srv__SensorData_Response.
typedef struct custom_interfaces__srv__SensorData_Response__Sequence
{
  custom_interfaces__srv__SensorData_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__SensorData_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__SENSOR_DATA__STRUCT_H_
