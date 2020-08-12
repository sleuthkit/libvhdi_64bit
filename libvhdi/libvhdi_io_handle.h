/*
 * Input/Output (IO) handle functions
 *
 * Copyright (C) 2012-2020, Joachim Metz <joachim.metz@gmail.com>
 *
 * Refer to AUTHORS for acknowledgements.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

#if !defined( _LIBVHDI_IO_HANDLE_H )
#define _LIBVHDI_IO_HANDLE_H

#include <common.h>
#include <types.h>

#include "libvhdi_libbfio.h"
#include "libvhdi_libcerror.h"
#include "libvhdi_libfdata.h"
#include "libvhdi_types.h"

#if defined( __cplusplus )
extern "C" {
#endif

extern const uint8_t *vhdi_file_signature;

typedef struct libvhdi_io_handle libvhdi_io_handle_t;

struct libvhdi_io_handle
{
	/* The block data offset
 	 */
	off64_t block_data_offset;

	/* The block bitmap size
	 */
	uint32_t block_bitmap_size;

	/* Value to indicate if abort was signalled
	 */
	int abort;
};

int libvhdi_io_handle_initialize(
     libvhdi_io_handle_t **io_handle,
     libcerror_error_t **error );

int libvhdi_io_handle_free(
     libvhdi_io_handle_t **io_handle,
     libcerror_error_t **error );

int libvhdi_io_handle_clear(
     libvhdi_io_handle_t *io_handle,
     libcerror_error_t **error );

int libvhdi_io_handle_read_data_block(
     libvhdi_io_handle_t *io_handle,
     libbfio_handle_t *file_io_handle,
     libfdata_vector_t *vector,
     libfdata_cache_t *cache,
     int element_index,
     int element_data_file_index,
     off64_t element_data_offset,
     size64_t element_data_size,
     uint32_t element_data_flags,
     uint8_t read_flags,
     libcerror_error_t **error );

#if defined( __cplusplus )
}
#endif

#endif /* !defined( _LIBVHDI_IO_HANDLE_H ) */

