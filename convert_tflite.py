import tensorflow as tf

saved_model_dir = '/home/anhnt653/Downloads/PyTorch-ONNX-TFLite-master/conversion/best_tf'
tflite_model_path = 'best4.tflite'

# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)

converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS, # enable TensorFlow Lite ops.
    tf.lite.OpsSet.SELECT_TF_OPS # enable TensorFlow ops.
    ]


converter.optimizations = [tf.lite.Optimize.DEFAULT]
