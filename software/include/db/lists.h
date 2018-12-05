//  lists.h
//
//  structures function prototypes for storing and
//  manipulating sensor data records

#ifndef _CYBORG_DB_LISTS_H_
#define _CYBORG_DB_LISTS_H_ 1

#include "sensors.h"

// ****************************************************************
// sensor list definition stuff
//

typedef struct sensorIdList {
    /// sensor type
    SENSOR_ID         type;
    /// pointer to next lower level (sensor sub id records)
    SENSOR_SUBID_LIST   *sensors;
    /// pointer to next sensor id list record
    struct sensorIdList  *next;
} SENSOR_ID_LIST;

typedef struct sensorList {
    /// sensor type
    SENSOR_TYPE         type;
    /// pointer to next lower level (starting with sensor id records)
    SENSOR_ID_LIST      *sensors;
    /// pointer to next sensor list record
    struct sensorList   *next;
} SENSOR_LIST;



typedef struct camRecord {
    /// arrival of camera message (actually insertion time in list)
    struct timeval       time;
    /// source camera identifier (right or left)
    char                camera;
    /// x coordinate of object
    int                 x;
    /// y coordinate of object
    int                 y;
    /// width of bounding box
    int                 w;
    /// height of bounding box
    int                 h;
    /// pointer to next camera record
    struct camRecord    *next;
} CAMERA_RECORD;

typedef struct camListHdr {
    /// Identifier of the object being reported
    char                *id;
    /// \brief pointer to individual camera records about this object
    ///
    /// object records from R / L cameras are on separate lists
    CAMERA_RECORD       *recs[NUM_OF_CAMERAS];
    /// pointer to next object header
    struct camListHdr   *next;
} CAMERA_LIST_HDR;


/// Get cam list record for a specific object id
CAMERA_LIST_HDR    *camListGetHdrById(char *);


/// ID, camera, x, y, w, h - add a new object (if needed) and camera record (always; newest at front of list)
int  camRecAdd(char *, char, int, int, int, int);

/// ID, TTL - delete old records for only a specific object id (all cameras)
void  camRecPruneById(char *, int);

/// TTL - prune all camera records older than TTL (regardless of camera or object id)
void  camRecPruneAll(int);

/// ID - delete all records for an id (all cameras)
int  camRecDeleteById(char *);

/// get latest record for an id (both cameras)
///
/// pointer to a 2-element CAMERA_RECORD array
///
/// CAMERA_RECORD array is zeroed
int camRecGetLatest(char *, CAMERA_RECORD *);

/// get average x, y, w, h, values for a specific (both cameras)
int camRecGetAvg(char *, CAMERA_RECORD *);

/// zero-out a CAMERA_RECORD object
void zeroCamRecord(CAMERA_RECORD *);

/// dump an individual CAMERA_RECORD
void dumpCamRecord(CAMERA_RECORD *);

/// zero an individual CAMERA_RECORD
void zeroCamRecord(CAMERA_RECORD *);




// ****************************************************************
// general sensor stuff
//

typedef struct sensorRangeRec {
    /// distance (in cm) for ranging sensor type
    int                 range;
} SENSOR_RANGE_RECORD;

typedef struct sensorGRec {
    /// acceleration X axis
    int                 x;
    /// acceleration Y axis
    int                 y;
    /// acceleration Z axis
    int                 z;
} SENSOR_G_RECORD;

typedef struct sensorRollRec {
    /// roll rate X axis
    int                 x;
    /// roll rate Y axis
    int                 y;
    /// roll rate Z axis
    int                 z;
} SENSOR_ROLL_RECORD;


typedef struct sensorMagRec {
    /// mag inclination X axis
    int                 x;
    /// mag inclination Y axis
    int                 y;
    /// mag inclination Z axis
    int                 z;
} SENSOR_MAG_RECORD;


typedef struct sensorRecord {
    /// arrival of sensor message (actually insertion time in list)
    struct timeval      time;
    /// union of all non-camera sensor records
    union {
        SENSOR_RANGE_RECORD    range;
        SENSOR_G_RECORD        gForce;
        SENSOR_ROLL_RECORD     roll;
        SENSOR_MAG_RECORD      mag;
    } sensorData;
    /// pointer to next sensor record
    void                *next;
} SENSOR_RECORD;


typedef struct sensorIdRecord {
    /// source sensor identifier
    char *                      *id;
    /// pointer to actual sensor data records
    SENSOR_RECORD               *recs;
    /// pointer to next sensor id record
    struct sensorIdRecord       *next;
} SENSOR_ID_RECORD;


typedef struct sensorListHdr {
    /// type of sensor (see sensors.h)
    SENSOR_TYPE                 sensorType;
    ///  pointer to individual sensor records about this object
    SENSOR_ID_RECORD            *recs;
    /// pointer to next object header
    struct sensorListHdr        *next;
} SENSOR_LIST_HDR;


/// type, ID, i1, i2, i3, i4 - add a new sensor type (if needed)
/// and sensor record (always; newest at front of list)
int  sensorRecAdd(SENSOR_TYPE, char *, int, int, int, int);

/// ID, TTL - delete old records for only a specific tytpe of sensor
/// (all instantiations of that sensor)
void  sensorRecPruneBySensorType(SENSOR_TYPE, int);

/// TTL - prune all sensor records older than TTL
/// (all instantiations)
void  sensorRecPruneAll(int);

/// ID - delete all records for a sensor type and ID
void  sensorRecDeleteById(SENSOR_TYPE, char *);

/// get latest record for a specific sensor in all instantiations
/// of a specific sensor type
///
/// pointer to an array of sensor records will be returned
/// (must be freed when no longer needed)
///
/// count is number of sensor instantiations returned
int sensorRecGetLatest(SENSOR_TYPE, char *, void *);

/// get average values for a specific sensor in all instantiations
/// of a specific sensor type
///
/// pointer to where an array of sensor records will be returned
/// (must be freed when no longer needed)
///
/// count is number of sensor instantiations returned
/// get average x, y, w, h, values for a specific (both cameras)
int sensorRecGetAvg(SENSOR_TYPE, char *, void *);

/// zero an individual sensor record
///
/// sensor type and pointer to record
////
/// zeroes only the fields applicable for that sensor and
/// sets sensor type
void zeroSensorRecord(SENSOR_TYPE, void *);





// ****************************************************************
// general list stuff
//

/// walks and dumps entire object and camera lists
void dumpLists();


#define LOCK_MAX_ATTEMPTS   20

#define LOCK_USLEEP_TIME    100

#endif  /* lists.h */
