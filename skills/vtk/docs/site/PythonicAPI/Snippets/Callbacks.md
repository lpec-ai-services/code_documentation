<!-- source: https://examples.vtk.org/site/PythonicAPI/Snippets/Callbacks/ -->

# Callbacks

### Description

If a function is passed to another function as an argument, it is known as a callback.

We define a function to use as the callback with this signature: `def my_callback(obj, ev):`. Then, to pass client data to it, we simply do: `my_callback.my_client_data = my_client_data`. This relies on the fact that Python functions are in fact objects and we are simply adding new attributes such as `my_client_data` in this case.

An alternative method is to define a class passing the needed variables in the `__init__` function and then implement a `__call__` function that does the work.

The simplest implementation of a callback is [CameraPosition](CameraPosition.md) where we do not even pass client data to it.

An implementation passing client data for both a function and a class is [CallBack](../Interaction/CallBack.md), the skeleton code of this is outlined here.

To use the snippet, click the *Copy to clipboard* at the upper right of the code blocks.

### Implementation

```python
def get_orientation(caller, ev):
    """
    Print out the orientation.

    We must do this before we register the callback in the calling function.
    Add the active camera as an attribute:
        get_orientation.cam = ren.active_camera

    :param caller: The caller.
    :param ev: The event.
    :return:
    """
    # Just do this to demonstrate who called callback and the event that triggered it.
    print(f'Caller: {caller.class_name}, Event Id: {ev}')
    # Verify that we have a camera in this case.
    print(f'Camera: {get_orientation.cam.class_name}')
    # Now print the camera orientation.
    # camera_orientation(get_orientation.cam)

class OrientationObserver:
    def __init__(self, cam):
        self.cam = cam

    def __call__(self, caller, ev):
        # Just do this to demonstrate who called callback and the event that triggered it.
        print(f'Caller: {caller.class_name}, Event Id: {ev}')
        # Verify that we have a camera in this case.
        print(f'Camera: {self.cam.class_name}')
        # Now print the camera orientation.
        # camera_orientation(self.cam)
```

### Usage

```python
    # Set up the callback.
    if use_function_callback:
        # We are going to output the camera position when the event
        #   is triggered, so we add the active camera as an attribute.
        get_orientation.cam = ren.active_camera
        # Register the callback with the object that is observing.
        iren.AddObserver('EndInteractionEvent', get_orientation)
    else:
        iren.AddObserver('EndInteractionEvent', OrientationObserver(ren.active_camera))
        # Or:
        # observer = OrientationObserver(ren.active_camera)
        # iren.AddObserver('EndInteractionEvent', observer)
```
