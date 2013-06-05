# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'webkit_browser_fileapi_sources': [
      '../browser/fileapi/async_file_util.h',
      '../browser/fileapi/async_file_util_adapter.cc',
      '../browser/fileapi/async_file_util_adapter.h',
      '../browser/fileapi/copy_or_move_file_validator.h',
      '../browser/fileapi/copy_or_move_operation_delegate.cc',
      '../browser/fileapi/copy_or_move_operation_delegate.h',
      '../browser/fileapi/external_mount_points.cc',
      '../browser/fileapi/external_mount_points.h',
      '../browser/fileapi/file_observers.h',
      '../browser/fileapi/file_permission_policy.cc',
      '../browser/fileapi/file_permission_policy.h',
      '../browser/fileapi/file_stream_writer.h',
      '../browser/fileapi/file_system_context.cc',
      '../browser/fileapi/file_system_context.h',
      '../browser/fileapi/file_system_dir_url_request_job.cc',
      '../browser/fileapi/file_system_dir_url_request_job.h',
      '../browser/fileapi/file_system_file_stream_reader.cc',
      '../browser/fileapi/file_system_file_stream_reader.h',
      '../browser/fileapi/file_system_file_util.cc',
      '../browser/fileapi/file_system_file_util.h',
      '../browser/fileapi/file_system_mount_point_provider.h',
      '../browser/fileapi/file_system_operation.h',
      '../browser/fileapi/file_system_operation_runner.cc',
      '../browser/fileapi/file_system_operation_runner.h',
      '../browser/fileapi/file_system_operation_context.cc',
      '../browser/fileapi/file_system_operation_context.h',
      '../browser/fileapi/file_system_options.cc',
      '../browser/fileapi/file_system_options.h',
      '../browser/fileapi/file_system_quota_client.cc',
      '../browser/fileapi/file_system_quota_client.h',
      '../browser/fileapi/file_system_quota_util.h',
      '../browser/fileapi/file_system_task_runners.cc',
      '../browser/fileapi/file_system_task_runners.h',
      '../browser/fileapi/file_system_url.cc',
      '../browser/fileapi/file_system_url.h',
      '../browser/fileapi/file_system_url_request_job.cc',
      '../browser/fileapi/file_system_url_request_job.h',
      '../browser/fileapi/file_system_url_request_job_factory.cc',
      '../browser/fileapi/file_system_url_request_job_factory.h',
      '../browser/fileapi/file_system_usage_cache.cc',
      '../browser/fileapi/file_system_usage_cache.h',
      '../browser/fileapi/file_writer_delegate.cc',
      '../browser/fileapi/file_writer_delegate.h',
      '../browser/fileapi/isolated_context.cc',
      '../browser/fileapi/isolated_context.h',
      '../browser/fileapi/isolated_file_util.cc',
      '../browser/fileapi/isolated_file_util.h',
      '../browser/fileapi/isolated_mount_point_provider.cc',
      '../browser/fileapi/isolated_mount_point_provider.h',
      '../browser/fileapi/local_file_stream_writer.cc',
      '../browser/fileapi/local_file_stream_writer.h',
      '../browser/fileapi/local_file_system_operation.cc',
      '../browser/fileapi/local_file_system_operation.h',
      '../browser/fileapi/local_file_util.cc',
      '../browser/fileapi/local_file_util.h',
      '../browser/fileapi/mount_points.cc',
      '../browser/fileapi/mount_points.h',
      '../browser/fileapi/native_file_util.cc',
      '../browser/fileapi/native_file_util.h',
      '../browser/fileapi/obfuscated_file_util.cc',
      '../browser/fileapi/obfuscated_file_util.h',
      '../browser/fileapi/open_file_system_mode.h',
      '../browser/fileapi/recursive_operation_delegate.cc',
      '../browser/fileapi/recursive_operation_delegate.h',
      '../browser/fileapi/remote_file_system_proxy.h',
      '../browser/fileapi/remove_operation_delegate.cc',
      '../browser/fileapi/remove_operation_delegate.h',
      '../browser/fileapi/sandbox_directory_database.cc',
      '../browser/fileapi/sandbox_directory_database.h',
      '../browser/fileapi/sandbox_file_stream_writer.cc',
      '../browser/fileapi/sandbox_file_stream_writer.h',
      '../browser/fileapi/sandbox_isolated_origin_database.cc',
      '../browser/fileapi/sandbox_isolated_origin_database.h',
      '../browser/fileapi/sandbox_mount_point_provider.cc',
      '../browser/fileapi/sandbox_mount_point_provider.h',
      '../browser/fileapi/sandbox_origin_database.cc',
      '../browser/fileapi/sandbox_origin_database.h',
      '../browser/fileapi/sandbox_origin_database_interface.cc',
      '../browser/fileapi/sandbox_origin_database_interface.h',
      '../browser/fileapi/sandbox_quota_observer.cc',
      '../browser/fileapi/sandbox_quota_observer.h',
      '../browser/fileapi/syncable/file_change.cc',
      '../browser/fileapi/syncable/file_change.h',
      '../browser/fileapi/syncable/local_file_change_tracker.cc',
      '../browser/fileapi/syncable/local_file_change_tracker.h',
      '../browser/fileapi/syncable/local_file_sync_context.cc',
      '../browser/fileapi/syncable/local_file_sync_context.h',
      '../browser/fileapi/syncable/local_file_sync_status.cc',
      '../browser/fileapi/syncable/local_file_sync_status.h',
      '../browser/fileapi/syncable/local_origin_change_observer.h',
      '../browser/fileapi/syncable/sync_action.h',
      '../browser/fileapi/syncable/sync_callbacks.h',
      '../browser/fileapi/syncable/sync_direction.h',
      '../browser/fileapi/syncable/sync_file_metadata.cc',
      '../browser/fileapi/syncable/sync_file_metadata.h',
      '../browser/fileapi/syncable/sync_file_status.h',
      '../browser/fileapi/syncable/sync_file_type.h',
      '../browser/fileapi/syncable/sync_status_code.cc',
      '../browser/fileapi/syncable/sync_status_code.h',
      '../browser/fileapi/syncable/syncable_file_operation_runner.cc',
      '../browser/fileapi/syncable/syncable_file_operation_runner.h',
      '../browser/fileapi/syncable/syncable_file_system_operation.cc',
      '../browser/fileapi/syncable/syncable_file_system_operation.h',
      '../browser/fileapi/syncable/syncable_file_system_util.cc',
      '../browser/fileapi/syncable/syncable_file_system_util.h',
      '../browser/fileapi/task_runner_bound_observer_list.h',
      '../browser/fileapi/test_mount_point_provider.cc',
      '../browser/fileapi/test_mount_point_provider.h',
      '../browser/fileapi/transient_file_util.cc',
      '../browser/fileapi/transient_file_util.h',
      '../browser/fileapi/upload_file_system_file_element_reader.cc',
      '../browser/fileapi/upload_file_system_file_element_reader.h',
    ],
    'webkit_browser_fileapi_chromeos_sources': [
      '../browser/chromeos/fileapi/async_file_stream.h',
      '../browser/chromeos/fileapi/cros_mount_point_provider.cc',
      '../browser/chromeos/fileapi/cros_mount_point_provider.h',
      '../browser/chromeos/fileapi/file_access_permissions.cc',
      '../browser/chromeos/fileapi/file_access_permissions.h',
      '../browser/chromeos/fileapi/file_util_async.h',
      '../browser/chromeos/fileapi/remote_file_system_operation.cc',
      '../browser/chromeos/fileapi/remote_file_system_operation.h',
      '../browser/chromeos/fileapi/remote_file_stream_writer.cc',
      '../browser/chromeos/fileapi/remote_file_stream_writer.h',
    ],
  },
  'targets': [
    {
      'target_name': 'dump_file_system',
      'type': 'executable',
      'sources': [
        'dump_file_system.cc',
      ],
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '../support/webkit_support.gyp:webkit_storage',
      ],
    },
  ],
}
